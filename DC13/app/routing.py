from django.urls import path
from .consumers import MyJsonWebsocketConsumer,MyAsyncJsonWebsocketConsumer

websocket_urlpatterns = [
    path('ws/jwc/<groupName>/',MyJsonWebsocketConsumer.as_asgi()),
    path('ws/ajwc/<groupName>/',MyAsyncJsonWebsocketConsumer.as_asgi()),
]