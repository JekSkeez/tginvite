import telebot
from telebot import types

# Вставьте ваш токен, полученный от BotFather
TOKEN = '6748620180:AAFTsjqJbfc4Cs02RAZKs7BM6WXanT9IQ0Q'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    channel_button = types.InlineKeyboardButton(text='<3', url='https://t.me/+7-3CfYgA0s1jMGYy')
    markup.add(channel_button)
    
    if message.from_user.is_bot:
        bot.reply_to(message, "Извините, боты не могут получить доступ к каналу")
    else:
        bot.reply_to(message, "Вот тут кнопочка, вступи как раз :3", reply_markup=markup)

bot.polling()

@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    if message.chat.type == "private":
        bot.reply_to(message, "Эта команда доступна только в групповых чатах или каналах.")
    else:
        chat_id = message.chat.id
        broadcast_text = "Пример рассылки: Это сообщение отправлено всем участникам чата или канала"
        for member in bot.get_chat_administrators(chat_id):
            user_id = member.user.id
            try:
                bot.send_message(user_id, broadcast_text)
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {user_id}. Ошибка: {e}")
        bot.reply_to(message, "Рассылка завершена.")

bot.polling()
