# Topic - Websocket consumer web api - JavaScript
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from time import sleep
import json

class MySyncConsumer(SyncConsumer):
    # This handler is called when initailly open a connection and is about to finished the WebSocket handshake.
    def websocket_connect(self,event):
        print('websocket connected...',event)
        self.send({
            'type': 'websocket.accept'
        })
    # This handler is called when data recieved from client
    def websocket_receive(self,event):
        print('Message recieved...',event)
        print(f"Message is {event['text']}")
        for i in range(0,50):
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({'count':i})
            })
            sleep(1)
    
    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    def websocket_disconnect(self,event):
        print('Websocket disconnected...',event)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    # This handler is called when initailly open a connection and is about to finished the WebSocket handshake.
    async def websocket_connect(self,event):
        print('websocket connected...',event)
        await self.send({
            'type': 'websocket.accept'
        })

    # This handler is called when data recieved from client
    async def websocket_receive(self,event):
        print('Message recieved...',event)
        print(f'Message is {event['text']}')
        for i in range(0,50):
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({'count':i})
            })
            await asyncio.sleep(1)
    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    async def websocket_disconnect(self,event):
        print('Websocket disconnected...',event)
        raise StopConsumer()

    