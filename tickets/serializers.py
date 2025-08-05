from rest_framework import serializers
from .models import Movie, Guest, Reservation

class MovieSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk', 'reservation', 'name', 'mobile',] 


