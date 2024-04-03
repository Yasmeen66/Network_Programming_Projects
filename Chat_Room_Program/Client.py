from socket import *
from threading import *

# Get the nickname from user input
nickname = input("Enter your nickname: ")

# Create a socket object
client = socket(AF_INET, SOCK_STREAM)
host='127.0.0.1'
port=7006
# Connect to the server
client.connect((host,port ))

# Function to receive messages from the server
def receive():
    while True:
        try:
            # Receive message from the server
            message = client.recv(1024).decode('ascii')
            # If the message is 'NICK', send the nickname to the server
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                # Otherwise, print the message
                print(message)
        except:
            # If an error occurs, handle it
            print("Error receiving message!")
            client.close()
            break
        
# Function to send messages to the server
def write():
    while True:
        # Get message from user input
        message = input()
        # Send message to the server with the user's nickname
        client.send('{}: {}'.format(nickname, message).encode('ascii'))
        
# Start a thread to receive messages from the server
receive_thread = Thread(target=receive)
receive_thread.start()

# Start a thread to send messages to the server
write_thread = Thread(target=write)
write_thread.start()
