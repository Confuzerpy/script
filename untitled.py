from bs4 import BeautifulSoup as bs
from urllib.request import *

btc_url = 'https://api.cryptonator.com/api/ticker/btc-rub'
eth_url = 'https://api.cryptonator.com/api/ticker/eth-rub'
xpr_url = 'https://api.cryptonator.com/api/ticker/xrp-rub'

def get_html(btc_url, eth_url, xpr_url):
	btc_req = requests.get(btc_url)
	eth_req = requests.get(eth_url)
	xrp_req = requests.get(xpr_url)

	#	btc_html = urlopen(btc_req).read()
	#	eth_html = urlopen(eth_req).read()
	#	xrp_html = urlopen(xrp_req).read()
	
	return btc_req.text, eth_req.text, xrp_req.text


def main():
	btc_soup = bs(btc_html, 'html.parser')
	eth_soup = bs(eth_html, 'html.parser')
	xrp_soup = bs(xrp_html, 'html.parser')

	btc_list = btc_soup.find(style_='word-wrap: break-word; white-space: pre-wrap;')
	eth_list = eth_soup.find(style_='word-wrap: break-word; white-space: pre-wrap;')
	xrp_list = xrp_soup.find(style_='word-wrap: break-word; white-space: pre-wrap;')

	print(btc_list, eth_list, xrp_list)


if __name__ == '__main__':
	main()