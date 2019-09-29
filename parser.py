import requests
from bs4 import BeautifulSoup as bs
import json
from time import sleep 

url = 'https://api.cryptonator.com/api/ticker/'

dop = ['btc-rub', 'eth-rub', 'xrp-rub']

# sleep(111)

def get_html(url):
	request = requests.get(url)
	return request.text


def main():
	for d in dop:
		html = get_html(url + d)
		soup = bs(html, 'html.parser').prettify()
		result = json.loads(soup)
		result = result.get('ticker')

		if result.get('base') == 'BTC':
			print(['Price BTC', result.get('price')])

		elif result.get('base') == 'ETH':
			print(['Price ETH', result.get('price')])

		else:
			print(['Price XRP', result.get('price')])
		
while True:
	main()
	sleep(3600)

			#sleep(2)
		#return main()


if __name__ == '__main__':
	main()