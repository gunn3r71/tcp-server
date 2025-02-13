#!/usr/bin/python3

import socket
import os

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = int(os.getenv('PORT', 3535))

allowedNumberOfConnections = int(os.getenv('ALLOWED_NUMBER_OF_CONNECTIONS', 5))

serverSocket.bind((host, port))

serverSocket.listen(allowedNumberOfConnections)

encoding = os.getenv('ENCODING', 'ascii')

while True:
    clientSocket, addr = serverSocket.accept()
    
    print("Got a connection from %s" % str(addr))

    clientSocket.send("Thank you for connecting".encode(encoding))

    clientSocket.close()