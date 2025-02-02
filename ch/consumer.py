from channels.generic.websocket import websocketConsumer
from asgiref.sync import async_to_sync
import json
class MainConsumer(websocketConsumer):
    
    def connect(self,**kwargs):
        self.room_name = "main_room"
        self.group_name="main_group"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,self.channel_name)
        self.accept()
        self.send(text_data=json.dumps({"message":"dfg"}))
    def receive(self, text_data=None, bytes_data=None):
       pass
    def disconnect(self, close_code):
        pass