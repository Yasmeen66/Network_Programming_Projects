from socket import *
from threading import *

host = '127.0.0.1'
port = 7006

# Create a socket object
server = socket(AF_INET, SOCK_STREAM)
# Bind the socket to the address and port
server.bind((host, port))
# Listen for incoming connections
server.listen()

# Lists to store connected clients and their nicknames
clients = []
nicknames = []

# Function to broadcast messages to all clients
def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            client.send(message)
        
# Function to handle each client
def handle(client):
    while True:
        try:
            # Receive message from client
            message = client.recv(1024)
            # Broadcast message to all clients
            broadcast(message, client)
        except:
            # If an error occurs, handle disconnection
            index = clients.index(client)
            clients.remove(client)
            client.close()
            # Get the nickname of the disconnected client
            nickname = nicknames[index]
            print(f"Disconnected: {nickname}")
            # Broadcast a message about the disconnection to all clients
            broadcast(f"{nickname} left the chat!".encode('ascii'), client)
            nicknames.remove(nickname)
            break
        
# Function to accept incoming connections
def receive():
    while True:
        # Accept connection from client
        client, address = server.accept()
        print(f"New connection from {address}")
        # Request nickname from client
        client.send('NICK'.encode('ascii'))
        # Receive nickname from client
        nickname = client.recv(1024).decode('ascii')
        # Add client and nickname to lists
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname set as: {nickname}")
        # Broadcast a message about new client joining to all clients
        broadcast(f"{nickname} joined the chat!".encode('ascii'), client)
        # Send confirmation message to the new client
        client.send('Connected to the server!'.encode('ascii'))
        # Start a new thread to handle the client
        thread = Thread(target=handle, args=(client,))
        thread.start()
        
receive()
