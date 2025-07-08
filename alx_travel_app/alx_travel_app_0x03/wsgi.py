import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app_0x03.settings')

application = get_wsgi_application()
