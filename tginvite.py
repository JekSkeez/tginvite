import telebot
from telebot import types

# �������� ��� �����, ���������� �� BotFather
TOKEN = '6748620180:AAFTsjqJbfc4Cs02RAZKs7BM6WXanT9IQ0Q'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    channel_button = types.InlineKeyboardButton(text='������� � �����', url='https://t.me/+7-3CfYgA0s1jMGYy')
    markup.add(channel_button)
    
    if message.from_user.is_bot:
        bot.reply_to(message, "��������, ���� �� ����� �������� ������ � ������")
    else:
        bot.reply_to(message, "������� �� ������, ����� ������� � �����", reply_markup=markup)

bot.polling()
