from re import L
from rest_framework.generics import ListCreateAPIView
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer


class ChatListCreateView(ListCreateAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        return Chat.objects.prefetch_related('members')


class MessageListCreateView(ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.select_related('chat', 'from_user').all()
