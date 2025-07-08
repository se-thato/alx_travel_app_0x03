from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as swagger_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny



schema_view = swagger_view(
    openapi.Info(
        title="Travel-App API",
        default_version= 'v1',
        description="The API documentation for bookings and listings",
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
