# импорт библиотеки и подключение токена бота
import telebot;
bot = telebot.TeleBot('token')

# метод получения сообщений
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_message(message):
	# ответы
	if message.text == "Привет" or "Hi":
		bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
	elif mess.text == '/help':
		bot.send_message(message.from_user.id, "Напиши: 'Привет', или 'Hi'")
	