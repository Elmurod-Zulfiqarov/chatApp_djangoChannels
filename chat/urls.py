from django.urls import path
from .views import ChatListCreateView, MessageListCreateView

urlpatterns = [
    path('', ChatListCreateView.as_view(), name="chat"),
    path('message/', MessageListCreateView.as_view(), name="message")
]
