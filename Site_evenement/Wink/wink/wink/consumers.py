import asyncio
import json 
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


from profil.models import *



class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connected", event)
        other_user = Winker.objects.get(id=int(self.scope['url_route']['kwargs']['idUser']))
        me = self.scope['user']

        chat_room = 'a_unique_chat_room'
        self.chat_room = chat_room
        
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )

        await self.send({
            "type":"websocket.accept"
        })

       
    async def websocket_receive(self, event): # recoit le message que l'on a envoyé dans socket.onopen et envoie un msg à socket.onmessage .
        #Le message est capturé dans event
        # when a message is received from the websocket
        print("receive",event)
        front_text = event.get('text',None)
        if front_text is not None:
            loaded_data = json.loads(front_text)
            me = self.scope['user'].username
            msg = loaded_data.get('message')

            myResponse = {
                'message':msg,
                'username':me,
            }

            await self.channel_layer.group_send(
                "a_unique_chat_room",
                {
                    "type":"chat_message",
                    "message": json.dumps(myResponse),
                }
            )
    
    async def chat_message(self,event):
        print("voici l'event ! : ", event)
        await self.send({
            "type":"websocket.send",
            "text":event['message']
        })
        

    async def websocket_disconnect(self, event):
        # when the socket connects
        print("disconnected",event)