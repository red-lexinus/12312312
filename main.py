import telebot

API_TOKEN = '1857804044:AAGCJitUgCZJ24mLsgE6kkM9lLT1svezXEY'

bot = telebot.TeleBot(API_TOKEN)

channel = '@proverkamybothub'


@bot.message_handler(func=lambda call: True)
def start(message):
    bot.send_message(channel, message.text)


bot.polling()
