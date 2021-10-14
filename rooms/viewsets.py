from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer
from rooms import serializers


class RoomViewSets(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
