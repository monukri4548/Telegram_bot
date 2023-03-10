from telegram import Bot
from telegram.ext import CommandHandler, Updater
from bot_app.models import BotSettings
from bot_app.views import start, stop

bot = Bot(token=BotSettings.objects.first().token)
updater = Updater(bot=bot)

start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(stop_handler)


updater.start_polling()


# import telegram.ext 
# from telegram.ext import Updater, CommandHandler

# def start(update, context):
#     update.message.reply_text("Hello! Welcome to Simplilearn")
    
# def help(update,context):
#     update.message.reply_text("""
#     The following commands are avilable:
    
#     /start -> Welcome to the channel
#     /help -> This message
#     /Subcribe -> Subscribe to get daily updates on iPhone price
#      """)
    
# def start(update: Update, context):
#     chat_id = update.effective_chat.id
#     context.bot.send_message(chat_id=chat_id, text="Welcome to the iPhone price updates bot!")

# def subscribe(update: Update, context):
#     chat_id = update.effective_chat.id
#     # TODO: Add logic to subscribe to daily updates on iPhone price
#     context.bot.send_message(chat_id=chat_id, text="You have successfully subscribed for daily updates on iPhone price!")

# Token = ("5963047842:AAE6MLwEZn90hoqPDJoSETmwL7vi_ChHXms")
# #print(bot.get_me())
# updater = telegram.ext.Updater("5963047842:AAE6MLwEZn90hoqPDJoSETmwL7vi_ChHXms", use_context=True)
# disp = updater.dispatcher

# disp.add_handler(telegram.ext.CommandHandler('start',start))
# disp.add_handler(telegram.ext.CommandHandler('help',help))
# disp.add_handler(telegram.ext.CommandHandler('subscribe',subscribe))
# disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
# updater.start_polling()
# updater.idle()
