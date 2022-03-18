import telebot
from telebot import types

bot = telebot.TeleBot ('5118182002:AAGd9IaaQ78P2vYLAerIoj3-_fDflRxCsX8')

@bot.message_handler(command=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("Помошь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id, text="Привет, {0.first_name}! Я тестовый бот для курса "
                                   "программирования на языке Пайтон".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "Вернутся в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "/dog" or ms_text == "Прислать собаку":
        bot.send_message(chat_id, text="ещё не готово...")

    

