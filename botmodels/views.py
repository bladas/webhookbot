import requests
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Message
from django.conf import settings
TELEGRAM_URL = "https://api.telegram.org/bot"
import json


class BotView(APIView):
    def post(self, request):
        r = request.data['message']
        chat_id = r['chat']['id']
        customer_name = r['chat']['first_name'] + ' ' + r['chat']['last_name']
        text = r['text']
        c, _ = Customer.objects.get_or_create(
            customer_id=chat_id,
            defaults={
                'name': customer_name
            }
        )
        add_message = Message.objects.create(
            text=text,
            customer=c,
            json=r
        )
        reply_text = r'Привіт , як ся маєш )?\n' + text
        self.send_message(reply_text,chat_id)
        return Response('Ok', status=200)

    def get(self, request):
        return Response('Ok', status=200)

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{TELEGRAM_URL}{settings.TOKEN}/sendMessage", data=data
        )