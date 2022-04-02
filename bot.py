
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#Command Handlers
def start(update, context):
    update.message.reply_text('Greetings, my KING, how can I be of service today?')

#function to respond to help cmd
def help(update, context):
    update.message.reply_text('Unfortunately, you are too GREAT, there is nothing I can really help you with...')

#function to echo the users message
def echo(update, context):
    update.message.reply_text(update.message.text + '' + '' +  ' Hahaha!...By the way, ALEJANDRO IS THE GREATEST PERSON IN THE UNIVERSE!')

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def age(update, context):
    update.message.reply_text("I am", 999999, "years old, but nowhere near as WISE as the great ALEJANDRO!")

def Name(update, context):
    update.message.reply_text("I am the amazing Anime God bot! Second only to my KING, Dr.Sir Master Sensei ALEJANDRO phD MD etc.!")

def CoolStatus(update, context):
    update.message.reply_text("You are pretty cool, but insignificant compared to my master, AlEJANDRO!")

def Hi(update, context):
    update.message.reply_text("Hello there, how can I help you today?")

def Bye(update, context):
    update.message.reply_text("Farewell, and don't bother me again, unless you are ALEJANDRO!")


def main():
    updater = Updater("5068378625:AAFClLSl1fth5B4_XZvoVXzsLohRNpDQKMs", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()