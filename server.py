#!/usr/bin/python3

import socket
import os
import sys
import threading
import codecs

"""
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
        #self.sock.setblocking(False)
        
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
            #print(msg)
            #print(self.clients)


            while True:

                try:

                except Exception as e:
                    print("Error in constructor function by: ", e)
                    break

            if msg == "exit":

                self.sock.close()
                sys.exit()

            else:
                #self.message_()
                pass



    def message_(self, msg, client):

        for c in self.clients:

            print("C: ",c)
            connect, addr = c
            
            #print("data received {}", c.recv(1024))
            try:
                
                if c != client:
                    
                    print("Message from client: ", connect.recv(1024).encode('ascii'))

                    c.sendall(msg)
            except:
                self.clients.remove(c)

        

    def Get_connection(self):

        print("[*] Connection was done successfully! ")

        while True:
            
            try:
                conn, addr = self.sock.accept()
                   
                #conn.setblocking(False)
                #print(self.clients)
                self.clients.append(conn)

            except Exception as e:

                print("Error in Get_connection by: ", e)
                break



    def Proc_connection(self):

        print("[*] Connection in proccess.")
        
        while True:
            
            if len(self.clients) > 0 :
                #print(self.clients)
                for c in self.clients:

                    try:

                        data = c.recv(1024)

                        if data:

                            self.message_(data,c)
                    
                    except Exception as e:
                        print("Error in Proc_connection, by: ", e)
                        break
                break

"""
#########


#if __name__ == "__main__":

#server = Server()



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((str('localhost'), int(5000)))


server.listen(2)


while True:

    print("[*] Waiting for any connection.")

    conn, address = server.accept()
        
    try:
        
        print("address: ",address)
        print("connection: ",conn)
        
        message = conn.recv(1024).decode('ascii')
        #message_values = message.decode('utf-8').strip()
        
        #if message != b'exit':
        print("client say: ", message)
        
        #else:
        #print("message: ", codecs.encode(message,'hex_codec'))
        #print(type(message))
        #message = conn.recv(1024)
        #print("{}".format(message).decode())
        #print(len(message))
        #print("message: ",message_values )
        break
    except Exception as e:
        print("se cayó por esto: ", e)
        break
    


"""
class Server:

    def __init__(self):
        
        self.clients = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind((str('localhost'), int(5000)))
        
        M_client = threading.Thread(target= self.client_message)
        C_client = threading.Thread(target = self.client_connection)

        M_client.start()
        C_client.start()

        while True:

            server_message = input()

            if (server_message == "exit"):

                self.socket.close()
                sys.exit()
            else:
                pass

    
    
    def client_message(self):
        
        while True:
            if len(self.clients) > 0:
                
                print(self.clients)
                message = self.clients[0].recv(1024).encode('ascii')
                print("Client says: ", message)
                break
            else:
                pass
                
                
    def client_connection(self):
        
        while True:
            try:
                conn, addr = self.socket.accept()

                #if (conn):
                print("[*] Connection was done successfully.")
                self.clients.append(conn)

                #else:
                    #pass

            except Exception as e:
                #pass
                print("Error in client connection by: ", e)
                break




if __name__ == "__main__":

    server = Server()
"""








