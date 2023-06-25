import requests
import os 

os.system('cls')
print("")
print("XSS")
print("")

url = input("url : ")

request = requests.get(url)

data_send = '<h1>Checked By Chien</h1>'

data = {"search": data_send, "Search": data_send}
request = requests.post(url, data=data)

if request.status_code == "Checked By Chien" not in request_http.text:
    print(f"[*] {url} May Be Vulnerable")
else:
    print(f"[x] {url} Not Vulnerable ")
