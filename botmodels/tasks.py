import requests

from botmodels.models import Customer
from celery import shared_task, task
from django.conf import settings

TELEGRAM_URL = "https://api.telegram.org/bot"


@task()
def periodic_send():
    message = 'Перевірте рівень кисню в крові і надішліть результати у %'
    customers = Customer.objects.filter(check=False)
    for item in customers:
        send_message(message, item.chat_id)


def send_message(message, chat_id):
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    response = requests.post(
        f"{TELEGRAM_URL}{settings.TOKEN}/sendMessage", data=data
    )
