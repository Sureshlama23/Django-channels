from django.urls import path
from .consumers import MyAsyncWebsocketConsumer,MyWebsocketConsumer
websocket_urlpatterns = [
    path('ws/wsc/<str:groupName>/',MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/<str:groupName>/',MyAsyncWebsocketConsumer.as_asgi()),
]