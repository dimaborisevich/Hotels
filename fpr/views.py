from rest_framework import viewsets, status, permissions
# from rest_framework.generics import
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hotel, RoomType, Reservation
from .serializers import HotelSerializer, RoomTypeSerializer, ReservationSerializer
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


# APIView - низкоуровневым (ровно один эндпоинт на работу)
# GenericView - среденеуровневым (ровно один эндпоинт на работу)
# ModelVIewSet - высокоуровневый (сразу два эндпоинта для работы: list get\post | retrive get\ put, patch \ delete)

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAuthenticated]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    # @csrf_exempt
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserReservationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs['user_id']
        return Reservation.objects.filter(user_id=user_id)


# class ReservationView(APIView):

# def get(self, request):
#     reservations = Reservation.objects.all()
#     serializer = ReservationSerializer(reservations, many=True)
#     return Response(serializer.data)

# def post(self, request):
#     serializer = ReservationSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Для работы html
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels': hotels})


def hotel_details(request, hotel_id):
    # hotel = Hotel.objects.get(id=hotel_id)
    hotel = get_object_or_404(Hotel, id=hotel_id)

    context = {
        'hotel': hotel,
    }

    return render(request, 'hotel_details.html', context)


def room_type_list(request):
    room_types = RoomType.objects.all()
    return render(request, 'room_types.html', {'room_types': room_types})


def room_type_details(request, room_type_id):
    room_type = RoomType.objects.get(id=room_type_id)
    return render(request, 'room_type_details.html', {'room_type': room_type})
