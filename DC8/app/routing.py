from django.urls import path
from .consumers import MyAsyncWebsocketConsumer,MyWebsocketConsumer
websocket_urlpatterns = [
    path('ws/wsc/',MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/',MyAsyncWebsocketConsumer.as_asgi()),
]