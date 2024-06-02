# Topic - Chat App with a Static Group Name
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.consumer import StopConsumer
from asgiref.sync import async_to_sync
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocket connect...',event)
        print('channels layer',self.channel_layer) # Get default channel layer from the project
        print('channels name...',self.channel_name) # get default channel name
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print('group name is..',self.group_name)
        # add a channel to a new or exiting group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, # group name
            self.channel_name)
        self.send({
            'type': 'websocket.accept'
        })
    def websocket_receive(self,event):
        print('message received...',event['text'])
        print(type(event['text']))
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type': 'chat.message',
            'message': event['text']
        })
    def chat_message(self,event):
        print('message...',event)
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
    
    def websocket_disconnect(self,event):
        print('websocket disconnect...',event)
        print('channels layer',self.channel_layer) # Get default channel layer from the project
        print('channels name...',self.channel_name) # get default channel name
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
        raise StopConsumer()
    
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('Websocket connect...',event)
        print('channels layer',self.channel_layer) # Get default channel layer from the project
        print('channels name...',self.channel_name) # get default channel name
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        # add a channel to a new or exiting group
        await self.channel_layer.group_add(
            self.group_name, # group name
            self.channel_name)
        await self.send({
            'type': 'websocket.accept'
        })
    async def websocket_receive(self,event):
        print('message received...',event['text'])
        print(type(event['text']))
        await self.channel_layer.group_send(self.group_name,{
            'type': 'chat.message',
            'message': event['text']
        })
    async def chat_message(self,event):
        print('message...',event)
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
    
    async def websocket_disconnect(self,event):
        print('websocket disconnect...',event)
        print('channels layer',self.channel_layer) # Get default channel layer from the project
        print('channels name...',self.channel_name) # get default channel name
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
        raise StopConsumer()
