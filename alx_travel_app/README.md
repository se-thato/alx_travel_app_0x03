# alx_travel_app_0x03

This project is a duplicate of `alx_travel_app_0x02`, enhanced with **Celery** and **RabbitMQ** to handle background tasks, specifically for sending **booking confirmation emails** asynchronously.

---

##  Features

- Asynchronous email sending using Celery
- RabbitMQ as the message broker
- BookingViewSet triggers email notification in the background
- Console email backend (can be upgraded to SMTP)

---

## Project Setup

### 1.Duplicate the Base Project

Clone or copy `alx_travel_app_0x02` into `alx_travel_app_0x03`:

```bash
cp -r alx_travel_app_0x02 alx_travel_app_0x03
cd alx_travel_app_0x03
