from django.urls import reverse
from channels.generic.websocket import WebsocketConsumer
import json
import requests


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        # Getting the API url
        url_origin = text_data_json['url_origin']
        api_url = url_origin + reverse('chatbotAPI')
        
        # Getting the question and finding an answer using the API
        message = text_data_json['message'] 
        response = requests.post(api_url, data = {'question': message})
        response = (response.json())['answer']
        message = "You: " + message
        message +=  '\n' + "Bot: " + response
        
        self.send(text_data=json.dumps({
            'message': message
        }))
