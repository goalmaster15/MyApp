from datetime import datetime
import telebot
from telebot import types
from pycbrf import ExchangeRates

'''Библиотеки: DateTime + pycbrf'''

bot = telebot.TeleBot("5102404417:AAEJ92AyK8i1ncMLGBlovW1FA4h3RrympBE")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.row("USD", 'EUR', 'лаунчпады', "/help")
    bot.send_message(message.chat.id, 'Привет! Спроси, что я умею', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\nПоказывать курс валютной пары USD-RUB\nПоказывать курс валютной пары EUR-RUB\nПоказывать рейтинг лаунчпадов для мира криптовалют')

@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id, text=f'<b>Текущий курс {message_norm.upper()}-RUB: {float(rates[message_norm.upper()].rate)}</b>', parse_mode='html')

    elif message_norm == "лаунчпады":
        bot.send_message(message.chat.id, 'Рейтинг лаунчпадов собран здесь – https://cryptorank.io/fundraising-platforms')
    else:
        bot.send_message(message.chat.id, 'Такой команды нет, напиши /help')

bot.polling(none_stop=True)