import socket
import socks
import asyncio
import aiohttp
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

async def response_http_socks(socks_address, socks_port):
    session = aiohttp.ClientSession()

    socks_conn = aiohttp.ProxyConnector.from_url(f'socks5://{socks_address}:{socks_port}')
    async with aiohttp.ClientSession(connector=socks_conn) as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    print(Fore.GREEN + Style.BRIGHT + "Request Successful")
                else:
                    print(Fore.RED + Style.BRIGHT + "Request Failed")
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + "Error: ", e)

        print(Fore.YELLOW + Style.BRIGHT + "socks_address: ", socks_address)
        print(Fore.YELLOW + Style.BRIGHT + "socks_port: ", socks_port)

tasks = []

for socks_address in sock_list:
    socks_address, socks_port = socks_address.split(':')

    task = asyncio.ensure_future(response_http_socks(socks_address, socks_port))

    tasks.append(task)

start_time = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"elapsed_time: {elapsed_time}")
