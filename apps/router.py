from django.urls import path, include

urlpatterns = [
    path("hotels/", include('apps.hotels.urls')),
    path("user/", include('apps.user.urls')),
    path("reservation/", include('apps.reservations.urls')),
    path("api/", include('apps.api.urls')),
]
