# calc v2

from colorama import init # Для работы на винде
from colorama import Fore, Back, Style 

init() # Для работы на винде

print(Back.GREEN)
what = input("Что делаем? (+,-): ")

try:

	print(Back.CYAN)
	a = float(input("Введите первое число: "))
	b = float(input("Введите второе число: "))
	
	print(Back.MAGENTA)
	if what == "+":
		print("Ответ: ", a + b)

	elif what == "-":
		print("Ответ: ", a - b)

	else:
		print("Я не знаю такой комнды. Попробуйте снова.")

except ValueError:
	print("Попробуйте снова.")

input