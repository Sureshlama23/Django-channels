from django.urls import path
from .consumers import MyJsonWebsocketConsumer,MyAsyncJsonWebsocketConsumer

websocket_urlpatterns = [
    path('ws/jwc/',MyJsonWebsocketConsumer.as_asgi()),
    path('ws/ajwc/',MyAsyncJsonWebsocketConsumer.as_asgi()),
]