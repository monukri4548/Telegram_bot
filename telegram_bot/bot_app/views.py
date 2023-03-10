from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater
from .models import User, BotSettings

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        bot = Bot(token="token=BotSettings.objects.first().token")
        updater = Updater(bot=bot)
        update = Update.de_json(request.body, bot)
        updater.dispatcher.process_update(update)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def start(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id
    if User.objects.filter(telegram_id=user.id).exists():
        context.bot.send_message(chat_id=chat_id, text="You are already subscribed.")
    else:
        User.objects.create(telegram_id=user.id, first_name=user.first_name, last_name=user.last_name, username=user.username, subscribed=True)
        context.bot.send_message(chat_id=chat_id, text="You are now subscribed.")

def stop(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id
    if User.objects.filter(telegram_id=user.id).exists():
        User.objects.filter(telegram_id=user.id).update(subscribed=False)
        context.bot.send_message(chat_id=chat_id, text="You have unsubscribed.")
    else:
        context.bot.send_message(chat_id=chat_id, text="You are not subscribed.")
