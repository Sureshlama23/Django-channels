# Topic - Websocket consumser WebSocketConsumser and AsyncWebSocketConsumer
# Real-time data Example
# Real-time data Example and frontend
# Database activity
# Authentication
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import json
from channels.consumer import async_to_sync
from channels.db import database_sync_to_async
from .models import Group,Chat

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        self.group = self.scope['url_route']['kwargs']['groupName']
        async_to_sync(self.channel_layer.group_add)(self.group,self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['chat']
        data['user'] = self.scope['user'].username
        if self.scope['user'].is_authenticated:
            group_id = Group.objects.get(name=self.group)
            Chat.objects.create(content=message,group=group_id)
            async_to_sync(self.channel_layer.group_send)(self.group,{
                'type': 'chat.message',
                'message': message
            })
        else:
            self.send(text_data=json.dumps({
                'chat': 'Login Required..','user': 'Guest'
            }))
    def chat_message(self,event):
        self.send(text_data=json.dumps({
            "chat": event['message']
        }))
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group,self.channel_name)


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group = self.scope['url_route']['kwargs']['groupName']
        await self.channel_layer.group_add(self.group,self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['chat']
        data['user'] = self.scope['user'].username
        if self.scope['user'].is_authenticated:
            group_id = await database_sync_to_async(Group.objects.get)(name=self.group)
            await database_sync_to_async(Chat.objects.create)(content=message,group=group_id)
            await self.channel_layer.group_send(self.group,{
                'type': 'chat.message',
                'chat': json.dumps(data)
            }
            )
        else:
            await self.send(text_data=json.dumps({
                'chat': 'login required...','user': 'Guest'
            }))
    async def chat_message(self,event):
        await self.send(text_data=event['chat'])

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group,self.channel_name)
