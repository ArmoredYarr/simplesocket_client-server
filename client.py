import socket

HOST = '127.0.0.1'
PORT = 4242

#The client (usually) only needs one socket. There are reasons to have more of course.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

client.send("Ahoy".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))