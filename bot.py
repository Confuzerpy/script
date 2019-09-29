# weather_bot v4.0

import telebot
import pyowm
from telebot import apihelper

owm = pyowm.OWM('tok', language = 'ru')

apihelper.proxy = {'https': '176.105.100.62:3128'}

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start', 'help'])
def start_message(message):

	if message.text == '/start':
		bot.send_message(message.chat.id, 'Привет, я бот, который скажет тебе погоду. Введи город, в котором хочешь узнать погоду.')

	elif message.text == '/help':
		bot.send_message(message.chat.id, 'Напиши /start')


@bot.message_handler(content_types=['text'])
def send_weath(message):
	print(message.text)
	#print(message)
	try:
	
		observation = owm.weather_at_place(message.text)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')['temp']
		bot.send_message(message.chat.id, 'В городе ' + message.text.capitalize() + ' сейчас ' + w.get_detailed_status() + ', температура воздуха ' + str(temp))

		if temp < 10:
			bot.send_message(message.chat.id, 'Сейчас ппц как холодно, одевайся как танк.')

		elif temp < 20:
			bot.send_message(message.chat.id, 'Сейчас прохладно, одевайся потеплее.')

		else:
			bot.send_message(message.chat.id, 'Сейчас тепло, иди в трусах))')

	
	#	if w.get_detailed_status() == 'дождь':
	#		bot.send_message(message.chat.id, 'Не забудь взять зонт.')
#
#		elif w.get_detailed_status() == 'лёгкий дождь':
#			bot.send_message(message.chat.id, 'Не забудь взять зонт.')
	
	except:
		bot.send_message(message.chat.id, 'Я не знаю такого города, попробуй ещё раз.')

bot.polling(none_stop=True)

