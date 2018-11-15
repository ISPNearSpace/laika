from home.models import Message
from rest_framework import viewsets
from home.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
