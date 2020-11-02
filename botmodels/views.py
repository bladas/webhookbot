from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from  .models import Customer,Message
from telegram import Bot
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
                'name':customer_name
            }
        )
        add_message = Message.objects.create(
            text=text,
            customer=c
        )

        return Response('Ok', status=200)

    def get(self, request):
        return Response('Ok', status=200)
