from time import sleep

import requests
from rest_framework.response import Response
from rest_framework.views import APIView

from pybot.celery import app
from .models import Customer, Message
from django.conf import settings

# from celery import shared_task

TELEGRAM_URL = "https://api.telegram.org/bot"


class BotView(APIView):
    def post(self, request):
        r = request.data['message']
        chat_id = r['chat']['id']
        customer_name = r['chat']['first_name'] + ' ' + r['chat']['last_name']
        text = r
        c, _ = Customer.objects.get_or_create(
            customer_id=chat_id,
            defaults={
                'name': customer_name
            }
        )
        try:
            if int(r):
                self.send_message("дякую", chat_id)
                c.check = True
                c.save()

        except:
            self.send_message("Напишіть число", chat_id)
            c.check = True
            c.save()

        add_message = Message.objects.create(
            text=text,
            customer=c,
            json=r
        )
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
