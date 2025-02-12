import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 3535

serverSocket.bind((host, port))

serverSocket.listen(5)

while True:
    clientSocket, addr = serverSocket.accept()
    
    print("Got a connection from %s" % str(addr))
    clientSocket.send("Thank you for connecting")

    clientSocket.close()