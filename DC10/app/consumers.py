#Topic - Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer
# Real-time data Example
# Real-time data Example and frontend
# Database activity
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
from .models import Group,Chat
import asyncio
from channels.db import database_sync_to_async
from channels.consumer import async_to_sync
import json
class MyWebsocketConsumer(WebsocketConsumer):
    # This handler is called when initailly open a connection and is about to finished the WebSocket handshake.
    def connect(self):
        print('websocket connected...')
        print('channels layer...',self.channel_layer)
        self.group = self.scope['url_route']['kwargs']['groupName']
        print('channels name...',self.channel_name)
        async_to_sync(self.channel_layer.group_add)(self.group,self.channel_name)
        self.accept()   # To accept connection

    # This handler is called when data recieved from client
    def receive(self, text_data=None, bytes_data=None):
        print('Message received from client',text_data)
        group_id = Group.objects.get(name=self.group)
        data = json.loads(text_data)
        message = data['chat']
        Chat.objects.create(content=message,group=group_id)
        print('Chating group is...',self.group)
        async_to_sync(self.channel_layer.group_send)(self.group,{
            'type': 'chat.message',
            'message': message
        }
        )
    def chat_message(self,event):
        print(event)
        print(event['message'])
        self.send(text_data=json.dumps({
            'chat': event['message']
        }))
        # self.send(text_data=text_data) # To send data to client

    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    def disconnect(self, close_code):
        print('Websocket disconnected...',close_code)
        print('channels layer...',self.channel_layer)
        print('channels name...',self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.group,self.channel_name)
        


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    # This handler is called when initailly open a connection and is about to finished the WebSocket handshake.
    async def connect(self):
        print('websocket connected...')
        print('channels layer...',self.channel_layer)
        print('channels name...',self.channel_name)
        self.group = self.scope['url_route']['kwargs']['groupName']
        await self.channel_layer.group_add(self.group,self.channel_name)
        await self.accept()   # To accept connection

    # This handler is called when data recieved from client
    async def receive(self, text_data=None, bytes_data=None):
        print('Message received from client',text_data)
        self.group = self.scope['url_route']['kwargs']['groupName']
        group_id = await database_sync_to_async(Group.objects.get)(name=self.group)
        data = json.loads(text_data)
        await database_sync_to_async(Chat.objects.create)(content=data['chat'],group=group_id)
        await self.send(text_data=text_data) # To send data to client
        message = data['chat']
        print('Chating group is...',self.group)
        await self.channel_layer.group_send(self.group,{
            'type': 'chat.message',
            'message': message
        }
        )
    async def chat_message(self,event):
        print(event)
        print(event['message'])
        await self.send(text_data=json.dumps({
            'chat': event['message']
        }))
    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    async def disconnect(self, close_code):
        print('Websocket disconnected...',close_code)
        print('channels layer...',self.channel_layer)
        print('channels name...',self.channel_name)
        await self.channel_layer.group_discard(self.group,self.channel_name)

        