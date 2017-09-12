import telegram
import logging
from telegram.ext import Updater, CommandHandler


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def on_start(bot, update):
    try:
        mes = update.message
        print(mes)
        user = mes.from_user;
        print(user)
        mes.reply_text(f"Hello, {user.name}")
    except Exception as ex:
        print(ex)

token = ''
updater = Updater(token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', on_start))
updater.start_polling()
updater.idle()