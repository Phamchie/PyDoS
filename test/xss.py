import requests
import os 

os.system('cls')
print("")
print("XSS")
print("")

url = input("url : ")

request = requests.get(url)

if request.status_code == 200:

    inputs = {"search", "q", "query", "Search"}

    payloads_attack = ['<h1>Cheked XSS By Chien</h1>']


    for params in inputs:

        for payload in payloads_attack:

            data_send = {params: payload}
            request = requests.post(url, data_send=data_send)

            if payload in request.text:
                print(f"[+] {url} May Be Vulnerable")
            else:
                print(f"[-] {url} Not Vulnerable")

else:
    print(f"{url} not response ")
