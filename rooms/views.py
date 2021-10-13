from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer
from rest_framework.generics import ListAPIView

    
@api_view(["GET"])
class ListRoomsView(ListAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer