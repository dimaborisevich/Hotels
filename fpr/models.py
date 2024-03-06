from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=100)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    price = models.IntegerField()
    bed_number = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(max_length=1500, blank=True, null=True)

    # Проверка на перекрытие дат
    def clean(self):
        if self.start_date < date.today():
            raise ValidationError("Нельзя бронировать на прошедшие даты.")

        overlapping_reservation = Reservation.objects.filter(
            room_type=self.room_type,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        )
        if overlapping_reservation:
            raise ValidationError("Комната уже занята в указанное время.")
