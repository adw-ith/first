from rest_framework.decorators import api_view
from rest_framework.response import Response
from basic.models import Room, Message, Topic, User
from .serializers import RoomSerializer, MessageSerializer, TopicSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api'
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/messages',
        'GET /api/topics'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMessage(request, pk):
    message = Message.objects.filter(id=pk)
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)
