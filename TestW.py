from telebot import types
import telebot
import time


tk = "6364474936:AAGaPIUm6nrwoszfl5l7_ce2CxsfKCBErk4"
bot = telebot.TeleBot(tk) 

@bot.message_handler(content_types=['text'])
def get_text_message(message):
  bot.send_message(message.from_user.id,message.text)
# echo-функция, которая отвечает на любое текстовое сообщение таким же текстом   

bot.polling(non_stop=True, interval=0) #запуск бота