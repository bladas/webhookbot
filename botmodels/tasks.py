import requests
from django.conf import settings

from pybot.celery import app

TELEGRAM_URL = "https://api.telegram.org/bot"


@app.task(name='add-every-minute')
def periodic_send():
    message = 'Перевірте рівень кисню в крові і надішліть результати у %'
    send_message(message, "391459806")


def send_message(message, chat_id):
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    requests.post(
        f"{TELEGRAM_URL}{settings.TOKEN}/sendMessage", data=data
    )
    return requests