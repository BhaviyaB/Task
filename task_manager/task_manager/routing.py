from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from tasks.consumers import TaskConsumer

websocket_urlpatterns = [
    path('ws/tasks/', TaskConsumer.as_asgi()),
]
