from rest_framework import serializers
from .models import Listing, Booking



class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ('id', 'host', 'created_at', 'updated_at')



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')