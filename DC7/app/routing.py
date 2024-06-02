from django.urls import path
from .consumers import MyAsyncConsumer,MySyncConsumer
websocket_urlpatterns = [
    path('ws/sc/<str:groupname>/',MySyncConsumer.as_asgi()),
    path('ws/ac/<str:groupname>/',MyAsyncConsumer.as_asgi()),
]