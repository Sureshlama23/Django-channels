#Topic - Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer

class MyWebsocketConsumer(WebsocketConsumer):
    # This handler is called when initailly open a connection and is about to finished the WebSocket handshake.
    def connect(self):
        print('websocket connected...')
        # print('channels layer...',self.channel_layer)
        # print('channels name...',self.channel_name)
        self.accept()   # To accept connection
        # self.close()  # To force - close the connection

    # This handler is called when data recieved from client
    def receive(self, text_data=None, bytes_data=None):
        print('Message received from client',text_data)
        self.send(text_data='message from server to client.') # To send data to client
        # self.send(bytes_data=data) To send Binany frame to client

    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    def disconnect(self, close_code):
        print('Websocket disconnected...',close_code)
        # self.close()          # To force - close the connection
        # self.close(code=2232) # To add custom connection websocket error code


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    # This handler is called when initailly open a connection and is about to finished the WebSocket handshake.
    async def connect(self):
        print('websocket connected...')
        # print('channels layer...',self.channel_layer)
        # print('channels name...',self.channel_name)
        await self.accept()   # To accept connection
        # await self.close()  # To force - close the connection

    # This handler is called when data recieved from client
    async def receive(self, text_data=None, bytes_data=None):
        print('Message received from client',text_data)
        await self.send(text_data='message from server to client.') # To send data to client
        # await self.send(bytes_data=data) To send Binany frame to client

    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    async def disconnect(self, close_code):
        print('Websocket disconnected...',close_code)
        # await self.close()          # To force - close the connection
        # await self.close(code=2232) # To add custom connection websocket error code

        