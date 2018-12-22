import socket
import os
from threading import *
import time
import signal

def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host,port))
	print('server started.....')
	s.listen(10)

	clients = []

	while True:
		c, addr = s.accept()
		rollnumber = c.recv(1024)
		if not rollnumber:
			print("ROLLNUMBER NOT FOUND")
			break



if __name__ == '__main__':
	Main()

