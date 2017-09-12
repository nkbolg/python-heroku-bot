import telegram
from telegram.ext import Updater, CommandHandler

def on_start(bot, update):
    update.message.reply_text("Hello, ", update.message.from_user.name)

token = ''
update = Updater(token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', on_start))
