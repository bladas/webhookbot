from django.core.management.base import BaseCommand
from telegram import Bot
from telegram import Update
from telegram.ext import Updater, Filters, CallbackContext
from telegram.ext import MessageHandler
from django.conf import settings
from telegram.utils.request import Request
from botmodels.models import Customer, Message


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Помилка: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    print(chat_id)
    c, _ = Customer.objects.get_or_create(
        customer_id=chat_id,
        defaults = {
            'name': update.message.from_user.username
        }
    )
    add_message = Message.objects.create(
        text = update.message.text,
        customer=c
    )

    add_message.save()
    reply_text = f'id user {c.pk}\nЩас буде прикол \n{add_message.text[::-1]} \n {update.message.from_user.first_name} {update.message.from_user.last_name}'
    update.message.reply_text(text=reply_text)
    # update.message.reply_markup()
    # update.message.audio(audio = update.message.audio)


class Command(BaseCommand):
    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,

        )

        updater = Updater(
            bot=bot,
            use_context=True
        )
        message_handler = MessageHandler(Filters.text,do_echo)
        updater.dispatcher.add_handler(message_handler)

        updater.start_webhook()
        updater.idle()
