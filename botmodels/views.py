from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from  .models import Customer,Message
from telegram import Bot
import json


class BotView(APIView):
    def post(self, request):
        r = request.data
        c = Customer.objects.get(pk = 1)
        Message.objects.create(
            text = r,
            customer=c
        )
        return Response('Ok', status=200)

    def get(self, request):
        return Response('Ok', status=200)
