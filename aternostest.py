
from telebot import types
import telebot
import time
from python_aternos import Client, atserver
nm = "Nexusssz1"
ps = "cfif123465"
tk = "6364474936:AAGaPIUm6nrwoszfl5l7_ce2CxsfKCBErk4"
bot = telebot.TeleBot(tk) 
atclient = Client()
atclient.login(nm, ps)
aternos = atclient.account
servs = aternos.list_servers()
myserv = servs[0] 
@bot.message_handler(commands=['start'])
def start(message):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Start server")
      markup.add(btn1)
      bot.send_message(message.chat.id, text="Server start".format(message.from_user), reply_markup=markup)
  

@bot.message_handler(content_types=['text'])  
def func(message):
      if(message.text == "Start server"):
          bot.send_message(message.chat.id, text="Check server status...")
          myserv.fetch()
          domain = "Domain: " + myserv.domain + "\n" + "Port: " + str(myserv.port)
          if(myserv.status=="online"):
           bot.send_message(message.chat.id, text="Server is already running")
           bot.send_message(message.chat.id, text=domain)
          if(myserv.status=="offline"):
           bot.send_message(message.chat.id, text="Server starting...Wait")
           myserv.start()
           time.sleep(1)
           while(myserv.status!="online"):
             myserv.fetch()
             time.sleep(5)
             print(myserv.status)
           bot.send_message(message.chat.id, text="Server is running")
           bot.send_message(message.chat.id, text=domain)
          if(myserv.status=="preparing"):
              bot.send_message(message.chat.id, text="Server is preparing...Wait")
              bot.send_message(message.chat.id, text=domain)
            
             
          
bot.polling(none_stop=True, interval=0)