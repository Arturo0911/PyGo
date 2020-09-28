import socket
import json
import threading
import sys
import pickle

class Client():

    def __init__(self, host= "localhost", port= 5000):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        message = threading.Thread(target= self.msg_recv)
        message.daemon = True

        message.start()

        while True:

            msg = input("client: ")

            if msg != "exit":
                self.msg_send(msg)
            else:
                self.sock.close()
                sys.exit()

    def msg_recv(self):
        
        while True:

            try:
                data = self.sock.recv(1024)

                if data:
                    print("la data", data)
                    print(pickle.loads(data))

            except:

                pass


    def msg_send(self, msg):

        self.sock.send(pickle.dumps(msg))


cliente = Client()
        
