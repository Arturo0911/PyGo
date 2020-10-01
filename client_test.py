import socket
import os
import threading
import sys




nickname = input('put up your nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((str('localhost'), int(5000)))

#message = b"Hola desde el lado del cliente!!!"
def receive():
    while True:
        
        try:
            
            
            message = client.recv(1024).decode('ascii')

            if  message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
            
        except Exception as e:
            print("Error by: ", str(e))
            client.close()
            sys.exit()
            break


# This one is to input message: 
def write():
    while True:
        messsage = "{}: {}".format(nickname, input(': '))
        client.send(messsage.encode('ascii'))


thread_1 = threading.Thread(target=write)
thread_1.start()

thread_2 = threading.Thread(target=receive)
thread_2.start()