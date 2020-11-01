from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from telegram import Bot
import json

class BotView(APIView):
    def post(self,request):
        r = request.data
        print(r)
        return Response('Ok',status = 200)


    def get(self, request):
        return Response('Fuck u',status=200)