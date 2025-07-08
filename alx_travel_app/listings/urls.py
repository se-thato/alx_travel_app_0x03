from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewset, InitiatePaymentView, VerifyPaymentView

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('payments/initiate/<int:booking_id>/', InitiatePaymentView.as_view(), name='initiate-payment'),
    path('payments/verify/', VerifyPaymentView.as_view(), name='verify-payment'),
]
