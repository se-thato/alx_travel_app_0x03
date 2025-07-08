from django.shortcuts import render
import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Booking, Payment
from django.conf import settings
from rest_framework import viewsets
from .serializers import ListingSerializer, BookingSerializer
from .models import Listing, Booking
from .tasks import send_booking_email



class ListingViewSet(viewsets.ModelViewSet):
    """
    Handles retrieving all listings
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewset(viewsets.ModelViewSet):
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer

        def perform_create(self, serializer):
            booking = serializer.save()
            user_email = booking.user.email
            send_booking_email.delay(user_email, booking.id)
        


class InitiatePaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found.'}, status=status.HTTP_404_NOT_FOUND)

        chapa_url = "https://api.chapa.co/v1/transaction/initialize"
        headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
        data = {
            "amount": str(booking.total_price),
            "currency": "ETB",
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "tx_ref": f"booking_{booking.id}",
            "callback_url": "https://yourdomain.com/api/payments/verify/",
            "return_url": "https://yourdomain.com/payment-success/"
        }
        chapa_response = requests.post(chapa_url, json=data, headers=headers)
        if chapa_response.status_code == 200:
            resp_data = chapa_response.json()
            payment, created = Payment.objects.get_or_create(
                booking=booking,
                defaults={
                    "amount": booking.total_price,
                    "transaction_id": resp_data['data']['tx_ref'],
                    "status": "Pending"
                }
            )
            return Response({"checkout_url": resp_data['data']['checkout_url'], "tx_ref": resp_data['data']['tx_ref']})
        return Response({"error": "Failed to initiate payment."}, status=status.HTTP_400_BAD_REQUEST)

class VerifyPaymentView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        tx_ref = request.query_params.get('tx_ref')
        chapa_url = f"https://api.chapa.co/v1/transaction/verify/{tx_ref}"
        headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
        chapa_response = requests.get(chapa_url, headers=headers)
        if chapa_response.status_code == 200:
            resp_data = chapa_response.json()
            try:
                payment = Payment.objects.get(transaction_id=tx_ref)
                if resp_data['data']['status'] == 'success':
                    payment.status = 'Completed'
                    # TODO: trigger Celery email task here
                else:
                    payment.status = 'Failed'
                payment.save()
                return Response({"status": payment.status})
            except Payment.DoesNotExist:
                return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Failed to verify payment."}, status=status.HTTP_400_BAD_REQUEST)
