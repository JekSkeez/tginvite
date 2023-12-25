import telebot
from telebot import types

# Вставьте ваш токен, полученный от BotFather
TOKEN = '6748620180:AAFTsjqJbfc4Cs02RAZKs7BM6WXanT9IQ0Q'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    channel_button = types.InlineKeyboardButton(text='Перейти в канал', url='https://t.me/+7-3CfYgA0s1jMGYy')
    markup.add(channel_button)
    
    if message.from_user.is_bot:
        bot.reply_to(message, "Извините, боты не могут получить доступ к каналу")
    else:
        bot.reply_to(message, "Нажмите на кнопку, чтобы перейти в канал", reply_markup=markup)

bot.polling()
