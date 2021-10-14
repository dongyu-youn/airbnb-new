from django.urls import path
from rest_framework import urlpatterns
from . import views
from . import viewsets
from rest_framework.routers import DefaultRouter

app_name = "rooms"

urlpatterns = [path("list/", views.ListRoomsView.as_view()), path("<int:pk>/", views.SeeRoomView.as_view())]

# router = DefaultRouter()
# router.register("", viewsets.RoomViewSets)

# urlpatterns = router.urls

