from django.contrib import admin
from .models import Hotel, RoomType, Reservation

# admin.site.register(Hotel)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):

    def upper_hotels_name(self, request, queryset):
        for obj in queryset:
            obj.name = obj.name.upper()
            obj.save()

    upper_hotels_name.short_description = 'В верхний регистр'

    actions = [
        'upper_hotels_name',
    ]

    search_fields = ("name", "adress", "phone", "email")
    list_display = ("name", "adress", "phone", "email")
    list_filter = ("name", "adress", "phone", "email")


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    search_fields = ("name", "hotel", "price", "bed_number")
    list_display = ("name", "hotel", "price", "bed_number")
    list_filter = ("name", "hotel", "price", "bed_number")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    search_fields = ("user", "hotel", "room_type", "start_date", "end_date", "status")
    list_display = ("user", "hotel", "room_type", "start_date", "end_date", "status")
    list_filter = ("user", "hotel", "room_type", "start_date", "end_date", "status")

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     if obj and obj.hotel:
    #         form.base_fields['room_type'].queryset = RoomType.objects.filter(hotel=obj.hotel)
    #     else:
    #         form.base_fields['room_type'].queryset = RoomType.objects.none()
    #     return form
