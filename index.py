import telebot
from telebot import types
import sys
admin_id=[1402188400,1424154451,1437940886,1402188400,1402188400]
admin_points=[2,2,1,0,0]

current_task="Создать дизайн маленьких букв"

bot = telebot.TeleBot("5147908412:AAGYjKQDeFBphdPaPqDfcjUJD7PHVmCJfuI")
markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
item2=types.KeyboardButton("Для создателей ⚒")
item3=types.KeyboardButton("Обо мне 🧷")

markup1=types.ReplyKeyboardMarkup(resize_keyboard=True)
item11=types.KeyboardButton("Текущее задание")
item21=types.KeyboardButton("количество баллов")
item31=types.KeyboardButton("Обратно ←")
item41=types.KeyboardButton("Обо мне 🧷")

markup1.add(item41)
markup1.add(item21)
markup1.add(item31)

markup.add(item2)
markup.add(item3)
GROUP_ID = -1001723903542
@bot.message_handler(commands=['start'])

def send_welcome(message):
	bot.send_message(message.chat.id,'Добро пожаловать!',reply_markup=markup)
	bot.send_message(message.chat.id,'выберите нужный пункт',reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Инфо 📌":
        bot.send_message(message.chat.id,'Инфо')
    elif message.text=="Для создателей ⚒":
        bot.send_message(message.chat.id,'Надо подтвердить личность')
        lichnost_p=False
        for i in range(len(admin_id)):
            if admin_id[i]==message.chat.id:
                bot.send_message(message.chat.id,'Личность успешно подтверждена',reply_markup=markup1)
                lichnost_p=True
                break
        if lichnost_p==False:
            bot.send_message(message.chat.id,'Не удалось подтвердить личность')
    elif message.text=="Обо мне 🧷":
        try:
            bot.send_message(message.chat.id,'О вас:')
            bot.send_message(message.chat.id,'ID: '+str(message.chat.id))
            bot.send_message(message.chat.id,'NAME: '+message.chat.first_name)
            #bot.send_message(message.chat.id,str(message))
        except BaseException:
            a=1
        
        try:
            bot.send_message(message.chat.id,'SURNAME: '+str(message.chat.last_name))
        except BaseException:
            a=1
        try:
            bot.send_message(message.chat.id,'USERNAME: '+str("@"+message.chat.username))
            
        except BaseException:
            a=1
        try:
            bot.send_message(message.chat.id,'COUNT OF MESSAGES: '+str(message.message_id))
        except BaseException:
            a=1
        
        
    elif message.text=="Текущее задание":
        try:
            for i in range(len(admin_id)):
                if admin_id[i]==message.chat.id:
                    bot.send_message(message.chat.id,current_task,reply_markup=markup1)
                    lichnost_p=True
                break
            if lichnost_p==False:
                bot.send_message(message.chat.id,'Не удалось подтвердить личность')
        except BaseException:
            a=1
    elif message.text=="Обратно ←":
        try:
            for i in range(len(admin_id)):
                if admin_id[i]==message.chat.id:
                    bot.send_message(message.chat.id,"Успешно",reply_markup=markup)
                    lichnost_p=True
                break
            if lichnost_p==False:
                bot.send_message(message.chat.id,'Не удалось подтвердить личность')
        except BaseException:
            a=1
    elif message.text=="количество баллов":
        try:
            for i in range(len(admin_id)):
                if admin_id[i]==message.chat.id:
                    bot.send_message(message.chat.id,str(admin_points[i]),reply_markup=markup1)
                    lichnost_p1=True
                break
            if lichnost_p1==False:
                bot.send_message(message.chat.id,'Не удалось подтвердить личность')
        except BaseException:
            a=1
            
        
    


bot.polling()
