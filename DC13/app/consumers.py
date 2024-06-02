# Topic - Generic Websocket - JsonWebsocketConsumer and AsyncJsonWebsocketConsumer
# Real time data
# Real time data & frontend
# Authentication 
from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from channels.consumer import async_to_sync,database_sync_to_async
from .models import Chat,Group


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print('websocket connected...')
        print('channels layer...',self.channel_layer)
        print('channels name...',self.channel_name)
        self.group = self.scope['url_route']['kwargs']['groupName']
        print('Group is.... ',self.group)
        async_to_sync(self.channel_layer.group_add)(self.group,self.channel_name)
        self.accept()

    def receive_json(self, content, **kwargs):
        print('Message received from client',content)
        print('Message received from client',type(content))
        content['user'] = self.scope['user'].username
        if self.scope['user'].is_authenticated:
            group_id = Group.objects.get(name=self.group)
            Chat.objects.create(content=content['chat'],group=group_id)
            async_to_sync(self.channel_layer.group_send)(self.group,{
                'type': 'chat.message',
                'chat': content['chat']
            })
        else:
            self.send_json(content={'chat': 'Login Requied...'})
    def chat_message(self,event):
        self.send_json(content=event)

    def disconnect(self, close_code):
        print('Websocket disconnect...',close_code)
        async_to_sync(self.channel_layer.group_discard)(self.group,self.channel_name)

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('websocket connected...')
        print('channels layer...',self.channel_layer)
        print('channels name...',self.channel_name)
        self.group = self.scope['url_route']['kwargs']['groupName']
        print('Group is.... ',self.group)
        await self.channel_layer.group_add(self.group,self.channel_name)
        await self.accept()

    async def receive_json(self, content, **kwargs):
        print('Message received from client',content)
        print('Message received from client',type(content))
        content['user'] = self.scope['user'].username
        if self.scope['user'].is_authenticated:
            group_id = await database_sync_to_async(Group.objects.get)(name=self.group)
            await database_sync_to_async(Chat.objects.create)(content=content['chat'],group=group_id)
            await self.channel_layer.group_send(self.group,{
                'type': 'chat.message',
                'chat': content
            })
        else:
            await self.send_json(content={'user': 'Guest','chat': 'Login Requied...'})

    async def chat_message(self,event):
        await self.send_json(content=event)

    async def disconnect(self, close_code):
        print('websocket disconnect...',close_code)
        print('channels layer...',self.channel_layer)
        print('channels name...',self.channel_name)
        await self.channel_layer.group_discard(self.group,self.channel_name)
