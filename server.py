# A socket server. 
# A socket is an endpoint for communication.
# There are many kinds of sockets. AF_INET, AF_BLUETOOTH, etc.
# They aren't always on TCP/IP. We're focusing on those here though.
# Sock Stream = TCP, Sock DGRAM = UDP.
# TCP: more overhead, but is more accurate, less lossy. Connection-Based. More reliable. Detects packet loss. Sequential, packets are in order. Byte Stream. Keeps up a connection.
# UDP: less overhead but can be prone to loss. Function-Based. Faster but less reliable. Does not detect packet loss. Packets show up in any order. Connects, does a thing, terminates. 
# Can handle packet loss with UDP, but would need to build some things on top of it.

import socket

HOST = '127.0.0.1' #Replace with LAN IP if you want, or if on a dedicated server use one of it's IPs, this is localhost.
PORT = 4242

#TCP Internet socket over IPV4.
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# We need to bind to a host and port.
serv.bind((HOST, PORT)) #Passed as a Tuple.

serv.listen() #Can limit possible connections by passing an int of how many connections. (Queue)
print("Server listening...")

server_live = True

while server_live:
    #When a client tries to connect, create a secondary socket for handling communication.
    #This will only work for a single connection, you would have to multithread it in order to handle multiple connections.
    #The scope of this is to to explore basic sockets.
    communication_socket, address = serv.accept()
    print(f'{address} has connected')
    message = communication_socket.recv(1024).decode('utf-8') #Buffer size is 1024 bytes.
    print(f'{address}: {message}')
    communication_socket.send('200'.encode('utf-8')) #200, like a web server. It can be anything you want. 
    communication_socket.close()

print(f'Connection to {address} closed.')