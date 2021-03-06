import socket
import threading
import os
import sys


clients = []
nicknames = []

    
    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((str('localhost'), int(5000)))
server.listen(10)

print("[*] Waiting por any message.")



def Broadcast(message):
    for client in clients:
        client.send(message)


def write():
    while True:

        try:
            
            message_to_all = input("Indica un mensaje para todos:")
            
            if message_to_all == "exit":
                
                server.close()
                sys.exit()

            else:

                for client in clients:
                    client.send(message_to_all.encode('ascii'))
            

        except Exception as e:
            print("Error by: ", str(e))
            break


def Handled(client):
    while True:

        try:
            message =  client.recv(1024)
            Broadcast(message)
        except:

            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            Broadcast('{} dejó el chat'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print("[*] Connection successfully in {}".format(str(address)))


        client.send('NICK:'.encode('ascii'))

        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)

        clients.append(client)

        Broadcast('{} joined the chat '.format(nickname).encode('ascii'))

        client.send('Connected to the server'.encode('ascii'))
        
        thread = threading.Thread(target=Handled, args= (client,))
        thread.start()
        
        if len(clients) > 1:
            write()
        else:
            pass

receive()
