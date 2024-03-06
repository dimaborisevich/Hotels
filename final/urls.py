from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from fpr.views import HotelViewSet, RoomTypeViewSet, ReservationViewSet, UserReservationViewSet
from fpr.views import hotel_list, hotel_details, room_type_list, room_type_details


router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'room-types', RoomTypeViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'user-bookings/(?P<user_id>\d+)', UserReservationViewSet, basename='user-bookings')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include(router.urls)),
    # path('reservations/', ReservationView.as_view(), name='reservation-list'),
    path('hotels/', hotel_list, name='hotel_list'),
    path('hotels/<int:hotel_id>/', hotel_details, name='hotel_details'),
    path('room-types/', room_type_list, name='room_type_list'),
    path('room-types/<int:room_type_id>/', room_type_details, name='room_type_details'),
    ]

