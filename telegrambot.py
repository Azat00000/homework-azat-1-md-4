import config
import telebot

bot = telebot.TeleBot("5118182002:AAGd9IaaQ78P2vYLAerIoj3-_fDflRxCsX8")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()