#  alxtravelapp

##  About the Project

**alxtravelapp** is a real-world Django application that serves as the foundation for a travel listing platform. This project focuses on initializing the project with scalable architecture, configuring a robust MySQL database, and integrating tools for automatic API documentation and maintainable configuration.


##  Key Highlights

###  Dependency Management
Install the following essential packages:

- `django`: Core web framework.
- `djangorestframework`: Toolkit for building RESTful APIs.
- `django-cors-headers`: Manage CORS policies for APIs.
- `drf-yasg`: Swagger/OpenAPI generation for DRF.
- `celery` & `rabbitmq`: For background task processing (future setup).

###  Settings Configuration
- Use `django-environ` to handle environment variables via `.env` files.
- Configure **MySQL** as the primary database engine.
- Set up REST Framework and CORS headers for API access.

###  Swagger Integration
- Use `drf-yasg` to generate automatic API documentation.
- Make Swagger UI available at `/swagger/`.

###  Version Control & Submission
- Initialize a Git repository with a clean, modular structure.
- Commit and push your project to a GitHub repository named `alxtravelapp`.


###  Create Models
- In `listings/models.py`, define `Listing`, `Booking`, and `Review` models based on the provided structure.
- Ensure each model includes appropriate fields, relationships (e.g., ForeignKey, ManyToMany), and constraints for data integrity.

###  Set Up Serializers
- Create serializers in `listings/serializers.py` for the `Listing` and `Booking` models.
- These serializers will be used to convert model instances to and from JSON for API operations.

###  Implement Seeders
- Create a custom Django management command in `listings/management/commands/seed.py`.
- This script will populate the database with sample listings data to facilitate development and testing.



# Chapa Payment Integration

## Payment Workflow

- Users initiate payment for a booking via `/api/payments/initiate/<booking_id>/`.
- The API returns a Chapa checkout URL for the user to complete payment.
- After payment, Chapa redirects to your callback, and `/api/payments/verify/?tx_ref=...` verifies the payment.
- Payment status is updated in the `Payment` model (`Pending`, `Completed`, `Failed`).

## Environment Variables

- Set `CHAPA_SECRET_KEY` in your environment.

## Testing

- Use Chapa’s sandbox for test payments.
- Check the `Payment` model for status updates after verification.