from rest_framework import serializers
from .models import Hotel, RoomType, Reservation
from django.contrib.auth.models import User
from datetime import date


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    # hotel = serializers.SlugRelatedField(slug_field='name', read_only=True)
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = RoomType
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
 
    # user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # room_type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # hotel = serializers.SlugRelatedField(slug_field='name', read_only=True)

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    hotel = HotelSerializer(read_only=True)
    room_type = RoomTypeSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        status = ''
        comment = ''

        if start_date < date.today():
            raise serializers.ValidationError("Нельзя указывать прошедшую дату в поле start_date")

        if end_date < date.today():
            raise serializers.ValidationError("Нельзя указывать прошедшую дату в поле end_date")

        if start_date > end_date:
            raise serializers.ValidationError("Дата начала не может быть позже даты окончания")

        return data

