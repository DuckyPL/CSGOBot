import requests, art, time, json, termplot, pdb

from os import name, system
from colorama import init, Fore, Style


init(autoreset=True)

down = Fore.RED
up = Fore.GREEN
reset = Style.RESET_ALL

reverse = str("\033[;7m")
green = str("\033[0;32m")
blue = str("\033[1;34m")
cyan = str("\033[1;36m")
reset = str("\033[0;0m")
yellow = str("\033[33m")
header = str("\033[95m")
red = str("\033[1;31m")
bold = str("\033[;1m")

v = 0


def clearScreen(): 
    if name == 'nt': 
        _ = system('cls')
        
    else: 
        _ = system('clear')


def login():

	data = f'donotcache=1613953857045&username={s_username}'
	headers = {
		'Host':'store.steampowered.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
		'Accept':'*/*',
		'Accept-Language':'en-GB,en;q=0.5',
		'Accept-Encoding':'gzip, deflate',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'X-Requested-With':'XMLHttpRequest',
		'Content-Length':'43',
		'Origin':'https://store.steampowered.com',
		'Connection':'close',
		'Referer':'https://store.steampowered.com/login/?redir=login/&redir_ssl=1&snr=1_60_4__global-header',
		'Cookie':f'browserid=2478638733977264157; steamMachineAuth76561199016612572=1A4EB96373589D03290B080898981FE447F2C8A9; timezoneOffset=0,0; steamMachineAuth76561199139906882=EEBFC93D889BEC5D21D8956B7A79CE7BBDAE6FA2; recentapps=%7B%221247570%22%3A1613139894%7D; steamCountry=GB%7Cd43cb30c42aaab59e7914feedbb01560; sessionid={s_id}; deep_dive_carousel_focused_app=730; deep_dive_carousel_method=default; dp_user_sessionid=ccc17f421f4418440d943d6a75a85dd2; dp_user_language=1; cc86.145.49.93=GB; cc2a00:23c7:5d66:8001:24d0:8986:bea6:c4f4=GB',
		'Sec-GPC':'1'

	}
	login_req = requests.post(url='https://steamcommunity.com/login/getrsakey/', data=data, headers=headers)

	data = f'donotcache=1613953857854&password={s_password}&username={s_username}&twofactorcode={s_2fa}&emailauth=&loginfriendlyname=&captchagid=-1&captcha_text=&emailsteamid=&rsatimestamp=435760750000&remember_login=false'
	headers = {
		'Host':'store.steampowered.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
		'Accept':'*/*',
		'Accept-Language':'en-GB,en;q=0.5',
		'Accept-Encoding':'gzip, deflate',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'X-Requested-With':'XMLHttpRequest',
		'Content-Length':'549',
		'Origin':'https://store.steampowered.com',
		'Connection':'close',
		'Referer':'https://store.steampowered.com/login/?redir=login/&redir_ssl=1&snr=1_60_4__global-header',
		'Cookie':f'browserid=2478638733977264157; steamMachineAuth76561199016612572=1A4EB96373589D03290B080898981FE447F2C8A9; timezoneOffset=0,0; steamMachineAuth76561199139906882=EEBFC93D889BEC5D21D8956B7A79CE7BBDAE6FA2; recentapps=%7B%221247570%22%3A1613139894%7D; steamCountry=GB%7Cd43cb30c42aaab59e7914feedbb01560; sessionid={s_id}; deep_dive_carousel_focused_app=730; deep_dive_carousel_method=default; dp_user_sessionid=ccc17f421f4418440d943d6a75a85dd2; dp_user_language=1; cc86.145.49.93=GB; cc2a00:23c7:5d66:8001:24d0:8986:bea6:c4f4=GB',
		'Sec-GPC':'1'

			}
	login_req1 = requests.post(url='https://steamcommunity.com/login/dologin/', data=data, headers=headers)

	headers = {
		'Host':'store.steampowered.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		'Accept-Language':'en-GB,en;q=0.5',
		'Accept-Encoding':'gzip, deflate',
		'Connection':'close',
		'Referer':'https://store.steampowered.com/login/?redir=login/&redir_ssl=1&snr=1_60_4__global-header',
		'Cookie':f'browserid=2478638733977264157; steamMachineAuth76561199016612572=1A4EB96373589D03290B080898981FE447F2C8A9; timezoneOffset=0,0; steamMachineAuth76561199139906882=EEBFC93D889BEC5D21D8956B7A79CE7BBDAE6FA2; recentapps=%7B%221247570%22%3A1613139894%7D; steamCountry=GB%7Cd43cb30c42aaab59e7914feedbb01560; sessionid={s_id}; deep_dive_carousel_focused_app=730; deep_dive_carousel_method=default; dp_user_sessionid=ccc17f421f4418440d943d6a75a85dd2; dp_user_language=1; cc86.145.49.93=GB; cc2a00:23c7:5d66:8001:24d0:8986:bea6:c4f4=GB; steamLoginSecure=76561199139906882%7C%7CD503073083EA8E06EAC5BBD20F8FEF95179300B7; steamRememberLogin=76561199139906882%7C%7C3a165b1a1839cdb11d42b4436a68c3bf',
		'Upgrade-Insecure-Requests':'1',
		'Sec-GPC':'1'
	}
	login_req2 = requests.get(url='https://steamcommunity.com/login/', headers=headers)

	login_req_clean = login_req.text
	login_req1_clean = login_req1.text
	login_req2_clean = login_req2.text

	lreq = json.loads(login_req_clean)
	lreq1 = json.loads(login_req1_clean)
	lreq2 = json.loads(login_req2_clean)

	if lreq['success'] == 'true':
		if lreq1['success'] == 'true':
			if lreq2['success'] == 'true':
				v = 0

	else:
		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		print("ERROR while logging in.. trying again in 5 seconds..")
		login()


def sell():
	while stock > 0:
		if settings[0].endswith("/"):
			sell_req = requests.post(url=f"{settings[0]}", data=data, headers=headers)
		else:
			sell_req = requests.post(url=f"{settings[0]}/", data=data, headers=headers)
		i -= stock


def buy(amount):
	while amount > 0:
		if settings[0].endswith("/"):
			buy_req = requests.post(url=f"{settings[0]}", data=data, headers=headers)
		else:
			buy_req = requests.post(url=f"{settings[0]}/", data=data, headers=headers)
		i -= json_price['average_price']
		stock += 1


def check_price(amount):

	raw_item_price = requests.get(url=f"http://csgobackpack.net/api/GetItemPrice/?currency=USD&id={settings[2]}")

	item_price = raw_item_price.text
	json_price = json.loads(item_price)

	try:
		stock_fluct.append(float(json_price['average_price']))
	except:
		print(f"{red}Invalid item name {blue}OR {red}Ratelimited (please wait)")

	stock_fluct_last = stock_fluct[(len(stock_fluct) - 2)]
	stock_fluct_check = len(stock_fluct) - 1

	if stock_fluct_last != stock_fluct[stock_fluct_check]:
		termplot.plot(stock_fluct)
		print(f"{cyan}Current average price of {blue}{exact_item_name_no_uni}{cyan}: ${json_price['average_price']}")
	else:
		v = 0

	amount = int(float(settings[1]) / float(json_price['average_price']))

	if json_price['average_price'] >= settings[4]:
		sell()
	elif json_price['average_price'] < settings[3]:
		buy()



def main():

	clearScreen()
	art.tprint("CSGO Bot                                     v3.2.4")

	login()

	while True:
		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		check_price()


if __name__ == '__main__':

	clearScreen()
	art.tprint("CSGO Bot                                     v3.2.4")
	csgo_url = input(f"{yellow}Direct URL to item you want to automatically buy and sell: {bold}")

	if "https://steamcommunity.com/market/" not in csgo_url:
		print(f"\n{red}Invalid steam URL, please try again...")
		time.sleep(2)
		clearScreen()
		quit()

	else:

		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		max_budget = input(f"{yellow}Enter your budget ($): {bold}")

		if max_budget == "":
			print(f"\n{red}Nothing entered.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		else:
			v = 0

		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		exact_item_name = input(f"{yellow}Exact item name (e.g. \"AK-47 | Wasteland Rebel (Battle-Scarred)\"): {bold}")
		exact_item_name_no_uni = exact_item_name
		exact_item_name = exact_item_name.replace(" ", "%20")

		if exact_item_name_no_uni == "":
			print(f"\n{red}Nothing entered.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		elif "(" not in exact_item_name_no_uni:
			print(f"\n{red}Invalid item name.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		else:
			v = 0

		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		price_to_buy = input(f"{yellow}At what price should the bot start buying stock? (e.g. $0.12): {bold}")

		if price_to_buy == "":
			print(f"\n{red}Nothing entered.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		elif price_to_buy >= max_budget:
			print(f"\n{red}Amount must be less than your max budget..")
			time.sleep(5)
			quit()
		else:
			v = 0

		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		price_to_sell = input(f"{yellow}At what price should the bot start selling stock? (e.g. $2.40): {bold}")
		price_to_sell = float(price_to_sell) - (float(price_to_sell) * (15/100))

		if price_to_sell == "":
			print(f"\n{red}Nothing entered.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		else:
			v = 0

		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		s_username = input(f"{yellow}Your steam username (e.g. Peenman69420): {bold}")

		if s_username == "":
			print(f"\n{red}Nothing entered.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		else:
			v = 0

		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		s_password = input(f"{yellow}Your steam password (e.g. p455w0rd): {bold}")

		if s_password == "":
			print(f"\n{red}Nothing entered.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		else:
			v = 0

		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		s_id = input(f"{yellow}Enter your Steam session id (e.g. 54b797c5q7469g8a0b4677c8: {bold}")

		if s_id == "":
			print(f"\n{red}Nothing entered.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		else:
			v = 0

		clearScreen()
		art.tprint("CSGO Bot                                     v3.2.4")
		s_2fa = input(f"{yellow}Enter your Steam 2fa (mobile) code (e.g. QF8TF): {bold}").upper()
		if len(s_2fa) < 4:
			print(f"\n{red}Invalid 2FA Code.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()

		if s_2fa == "":
			print(f"\n{red}Nothing entered.. Quitting in 5 seconds..")
			time.sleep(5)
			quit()
		else:
			v = 0

		settings = [
			str(csgo_url),
			str(max_budget),
			str(exact_item_name),
			str(price_to_buy),
			str(price_to_sell),
			str(s_username),
			str(s_password),
			str(s_id),
			str(s_2fa)
		]

		stock_fluct = []
		stock_fluct = list()

		stock = 0

		main()
