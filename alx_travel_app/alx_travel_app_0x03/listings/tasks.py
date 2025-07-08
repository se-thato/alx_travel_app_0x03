from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_email(to_email, booking_id):
    subject = "Booking Confirmation"
    message = f"Your booking (ID: {booking_id}) was successful!"
    from_email = "noreply@travel.com"
    recipient_list = [to_email]

    send_mail(subject, message, from_email, recipient_list)