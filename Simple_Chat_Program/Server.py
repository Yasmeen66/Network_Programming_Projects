from socket import *

s = socket(AF_INET, SOCK_STREAM)
print("Socket Created Successfully")
host = '127.0.0.1'
port = 7006
s.bind((host, port))
print("Socket is binded to:", port)
s.listen(5)
print("Socket is Listening")

Client_Session, Client_address = s.accept()
print("Session is created with client:", Client_address[0])

while True:
    # Receive the length of the message
    length_bytes = Client_Session.recv(4)
    length = int.from_bytes(length_bytes, byteorder='big')
    
    # Receive the message based on its length
    Recv_Msg = Client_Session.recv(length).decode('utf-8')
    print("Client:", Recv_Msg)
    
    # Sending acknowledgment to the client
    Client_Session.send("Received".encode('utf-8'))

    # Exit loop if client sends 'exit'
    if Recv_Msg.strip().lower() == 'exit':
        break

    # Send response
    Send_Msg = input('Server: ')
    Send_Msg_length = len(Send_Msg)
    Client_Session.sendall(Send_Msg_length.to_bytes(4, byteorder='big') + Send_Msg.encode('utf-8'))

Client_Session.close()
