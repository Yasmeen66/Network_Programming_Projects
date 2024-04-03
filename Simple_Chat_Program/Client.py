from socket import *

s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7006
s.connect((host, port))

while True:
    # Input message
    y = input("Client: ")

    # Send the length of the message
    length = len(y)
    s.sendall(length.to_bytes(4, byteorder='big'))

    # Send the message
    s.sendall(y.encode('utf-8'))

    # Receive acknowledgment from server
    ack = s.recv(8).decode('utf-8')

    # Exit loop if server sends 'exit'
    if y.strip().lower() == 'exit':
        break

    # Receive response from server
    x_length = int.from_bytes(s.recv(4), byteorder='big')
    x = s.recv(x_length).decode('utf-8')
    print("Server:", x)

s.close()
