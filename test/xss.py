import requests
import os 

os.system('cls')
print("")
print("XSS")
print("")

url = input("Nhập URL: ")

response = requests.get(url)

if response.status_code == 200:
    inputs = ["search", "q", "query"]
    
    payloads = ['<script>alert("XSS")</script>', '<img src=x onerror=alert("XSS")>']
    
    for param in inputs:
        for payload in payloads:
            data = {param: payload}
            response = requests.post(url, data=data)
            
            if payload in response.text:
                print(f"[+] {param} is vulnerable to XSS")
else:
    print("[-] The website is not available")
