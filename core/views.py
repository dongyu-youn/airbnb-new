from rooms.models import Room
from django.http import HttpResponse
import json
from django.core import serializers

# Create your views here.

def list_rooms(request):
    # o 여기서 나는 모든 데이터를 출력하고 싶다  
    # o room을 json으로 변환시키고 싶다 
    # o 고객한테 야 저기야 그 이거 json데이터로 좀 변환시켜주라
    # o 오케이 이거를 Json으로 변화를 시켰으니깐 이제 정확한 데이터 있지?
    # o dump는 객체를 데이터 포멧으로 나눈다
    # o serialize를 써야한다고 하거든?
    

    data = serializers.serialize("json", Room.objects.all())
    # room = Room.objects.all()
    # rooms_json = []
    # for rooms in room:
    #     rooms_json.append(json.dumps(rooms))
    # json_rooms = json.dumps(room)
    response = HttpResponse(content=data)
    # o 이렇게 하는 이유는 쿼리셋을 만들수없다 쿼리셋은 나열된 json이 아니기 때문ㄷ 따라서 빈배열을 만들자
    return response
    print(room)

