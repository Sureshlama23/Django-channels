# Topic - Generic Websocket - JsonWebsocketConsumer and AsyncJsonWebsocketConsumer
from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print('websocket connected...')
        self.accept()

    def receive_json(self, content, **kwargs):
        print('Message received from client',content)
        print('Message received from client',type(content))
        self.send_json(content=content)

    def disconnect(self, close_code):
        print('Websocket disconnect...')

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('websocket connected...')
        await self.accept()

    async def receive_json(self, content, **kwargs):
        print('message received from client...',content)
        await self.send_json(content=content)

    async def disconnect(self, close_code):
        print('websocket disconnect...')