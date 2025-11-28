import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('example.com', 80))
socket.sendall('GET http://data.pr4e.org/intro-short.txt HTTP/1.0'.encode())

while True:
    data = socket.recv(4096)
    if not data:
        break
    print(data.decode())
    
socket.close()