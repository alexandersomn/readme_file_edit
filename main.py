import telebot
import requests
from googletrans import Translator

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

translator = Translator()

src = 'ru'
dest = 'en'

TOKEN = "5942869272:AAFfNTJH-VIIla8ETrCHmQf0C2Y3cRyJr60"
bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Поменять язык перевода на русский'))
keyboard.add(KeyboardButton('Поменять язык перевода на английский'))


@bot.message_handler(commands=['help', 'start'])
def get_started(message):
    bot.send_message(message.chat.id, text=f'Привет, я бот-переводчик', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def translate_text(message):
    src = 'ru'
    dest = 'en'
    if message.text == "Поменять язык перевода на русский":
        src = 'en'
        dest = 'ru'
    elif message.text == "Поменять язык перевода на английский":
        src = 'ru'
        dest = 'en'
    else:
        translated = translator.translate(message.text, src=src, dest=dest).text
        bot.send_message(message.chat.id, translated)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Поменять язык перевода на русский"):
        src = 'en'
        dest = 'ru'
    elif(message.text == "Поменять язык перевода на английский"):
        src = 'ru'
        dest = 'en'

bot.infinity_polling()