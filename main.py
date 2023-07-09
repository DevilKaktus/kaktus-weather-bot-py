import telebot
import requests
import json
from config.config import TOKEN, API
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/current_weather":
        response = requests.get(API)
        response_dict = json.loads(response.text)
        # print(response_dict)
        weather = response_dict['list'][0]
        bot.send_message(message.from_user.id, f'{weather["dt_txt"]} {weather["main"]["temp"]}')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
