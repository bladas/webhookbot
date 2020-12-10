import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Message
from django.conf import settings
from celery import Celery, app
from celery.schedules import crontab

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

        add_message = Message.objects.create(
            text=text,
            customer=c,
            json=r
        )
        return Response('Ok', status=200)

    def get(self, request):
        return Response('Ok', status=200)

    def periodic_send(self):
        message = 'Перевірте рівень кисню в крові і надішліть результати у %'
        customers = Customer.objects.filter(check=False)
        for item in customers:
            self.send_message(message, item.chat_id)

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


bot = BotView


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10 * 60, bot.periodic_send())
