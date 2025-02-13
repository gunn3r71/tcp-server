#!/user/bin/python3
import os
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = int(os.getenv('PORT', 3535))

clientSocket.connect((host, port))

bufferSize = int(os.getenv('BUFFER_SIZE', 1024))

message = clientSocket.recv(bufferSize)

clientSocket.close()

encoding = os.getenv('ENCODING', 'ascii')

print(message.decode(encoding))