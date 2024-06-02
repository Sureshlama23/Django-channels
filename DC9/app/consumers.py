#Topic - Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer
# Real-time data Example
# Real-time data Example and frontend
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio
class MyWebsocketConsumer(WebsocketConsumer):
    # This handler is called when initailly open a connection and is about to finished the WebSocket handshake.
    def connect(self):
        print('websocket connected...')
        # print('channels layer...',self.channel_layer)
        # print('channels name...',self.channel_name)
        self.accept()   # To accept connection
    # This handler is called when data recieved from client
    def receive(self, text_data=None, bytes_data=None):
        print('Message received from client',text_data)
        for i in range(20):
            self.send(text_data=str(i)) # To send data to client
            sleep(1)

    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    def disconnect(self, close_code):
        print('Websocket disconnected...',close_code)


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    # This handler is called when initailly open a connection and is about to finished the WebSocket handshake.
    async def connect(self):
        print('websocket connected...')
        # print('channels layer...',self.channel_layer)
        # print('channels name...',self.channel_name)
        await self.accept()   # To accept connection

    # This handler is called when data recieved from client
    async def receive(self, text_data=None, bytes_data=None):
        print('Message received from client',text_data)
        for i in range(20):
            await self.send(text_data=str(i)) # To send data to client
            await asyncio.sleep(1)
    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    async def disconnect(self, close_code):
        print('Websocket disconnected...',close_code)

        