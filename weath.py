# weather v2.0

from colorama import init
from colorama import Fore, Back, Style
import pyowm

init()

owm = pyowm.OWM('token', language = 'ru')

print(Back.GREEN)
place = input('В каком городе хотите узнать погоду?: ')

observation = owm.weather_at_place(place)
w = observation.get_weather()
print(w)
temp = w.get_temperature('celsius')['temp']

print(Back.CYAN)
print('В городе ' + place + ' сейчас ' + w.get_detailed_status() + ', температура воздуха ' + str(temp))
print(w.get_detailed_status())

print(Back.MAGENTA)
if temp < 10:
	print('Сейчас ппц как холодно, одевайся как танк.')

elif temp < 20:
	print('Сейчас прохладно, одевайся потеплее.')

else:
	print('Сейчас тепло, иди в трусах))')

	
init()
print(Back.RED)
input('Press ENTER to exit')