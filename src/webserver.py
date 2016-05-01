import socket

def main():
	(HOST,PORT) = ('', 8080)

	lSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	lSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	lSocket.bind((HOST,PORT))
	lSocket.listen(1)

	print "Socket ready on port: "+str(PORT)
	i = 0
	while i<5:
		(cConnect, cAddr) = lSocket.accept()
		i+=1
		request = cConnect.recv(4096) 
		print(request)
		
		response = """\
HTTP/1.1 200 OK

Hello, World!"""

		cConnect.sendall(response)
		cConnect.close()
		
if __name__ == "__main__":
	main()
