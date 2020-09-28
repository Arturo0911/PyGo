#!/usr/bin/python3

import socket
import os
import sys
import threading

class Server():
    

    def __init__(self, host= "localhost", port = 5000):
        
        # every client will be connected and pushed into the array.
        self.clients = []
        
        # Primero a que familia pertenece, después, que tipo de protocolo
        # Si es TCP entonces socket.SOCK_STREAM
        # Si es UDP entonces socket.SOCK_DGRAM
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # En el caso del servidor utilizamos el metodo bind
        self.sock.bind((str(host), int(port)))
        
        # maximum number of connections, in this case will be 10
        self.sock.listen(10)
        self.sock.setblocking(False)
        
        # We create the threads proccess, 2
        
        G_conn = threading.Thread(target = self.Get_connection)
        G_conn.daemon = True
        
        P_conn = threading.Thread(target = self.Proc_connection)
        P_conn.daemon = True

        
        # Initialize threads of connections
        G_conn.start()
        P_conn.start()

        while True:

            msg = input("Server: ")
            print(msg)
            #print(self.clients)
            if msg == "exit":

                self.sock.close()
                sys.exit()

            else:

                pass



    def message_(self, msg, client):

        for c in self.clients:

            try:
                
                if c != client:
                    c.send(msg)
            except:
                self.clients.remove(c)

        

    def Get_connection(self):

        print("[*] Connection was done successfully! ")

        while True:
            
            try:
                conn, addr = self.sock.accept()
                   
                conn.setblocking(False)
                #print(self.clients)
                self.clients.append(conn)

            except:

                pass



    def Proc_connection(self):

        print("[*] Connection in proccess.")
        
        while True:
            
            if len(self.clients) > 0 :
                #print(self.clients)
                for x in self.clients:

                    try:

                        data = x.recv(1024)

                        if data:

                            self.message_(data,x)
                    
                    except:
                        pass





#if __name__ == "__main__":

server = Server()


