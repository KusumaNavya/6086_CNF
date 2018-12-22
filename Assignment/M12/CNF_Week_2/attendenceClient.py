import socket
from threading import *
import os
import signal

def main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.connect((host, port))
	rollnumber = input("Mark attendence for rollnumber: ")
	while True:
		data = s.recv(1024).decode()
		if (data == 'ROLLNUMBER NOT FOUND'):
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
			break
		print(data)
            
        secretq = s.recv(1024).decode()
        print(secretq)
        ans = input(" answer : ")
        ans = s.send().encode()
        data2 = s.recv(1024).decode()
        if (data2 == ATTENDANCE FAILURE):
        	os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
		print(data)
		else:
			print(data)
		s.close()

if __name__ == '__main__':
	Main()




			


