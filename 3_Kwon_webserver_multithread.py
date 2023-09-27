import socket
import sys # In order to terminate the program
import threading
from threading import Thread

# Multithreaded Python server : TCP Server Socket Thread Pool
def HandleClientThread(conn, addr): 
    try:
            print("Starting a thread")

            message = conn.recv(1024)
            filename = message.split()[1]
            print("File : ", filename)
            f = open(filename[1:])
            outputdata = f.read()

            print("Message Recieved")

            HOST = "127.0.0.1"
            #The .bind() method is used to associate the socket with a specific network interface and port number
            print(addr[1])

            print("Sending Header")

            # Send the HTTP response header line to the connection socket  
            Header = 'HTTP/1.1 200 OK\r\n\r\n'
            #send new Port Address
            address = str(addr[1]+1)
            print(address)
            Header = address + ":"+Header
            conn.send(Header.encode('utf-8')) 

            conn.close()

            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.bind((HOST, addr[1]+1))
            conn.listen()
            conn2, addr2 = conn.accept()  

            try:
                print('The server is ready to receive on new port')

                # Send the content of the requested file to the client
                conn2.sendall(outputdata.encode('utf-8'))    

                # Close the connection socket with this particular client
                conn2.close()
            except IOError:
                ErrorMessage = "HTTP/1.1 404 Not found\r\n\r\n"   
                conn2.send(ErrorMessage.encode('utf-8'))   
                conn2.close()      
                        
    except IOError:
                # Send response message for file not found  
                ErrorMessage = "HTTP/1.1 404 Not found\r\n\r\n"   
                conn.send(ErrorMessage.encode('utf-8'))   

                # Close the client connection socket
                conn.close()  

'''main thread in which your modified server listens for clients at a fixed port. When it receives
a TCP connection request from a client, it will set up the TCP connection through another port
3 and services the client request in a separate thread.'''
#serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#SO_REUSEADDR socket option allows for the reuse of local addresses and ports
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
threads = [] 

#Prepare a sever socket
HOST = "127.0.0.1"
PORT = 6789
#Increment this variable for each thread
Current_PORT = 6789

#The .bind() method is used to associate the socket with a specific network interface and port number
serverSocket.bind((HOST, PORT))
#.listen() enables a server to accept connections
serverSocket.listen()

while True:
    try:
        print('The server is ready to receive')

        # Set up a new connection from the client - The .accept() method blocks execution and waits for 
        # an incoming connection. When a client connects, it returns a new socket object representing 
        # the connection and a tuple holding the address of the client
        conn, addr = serverSocket.accept()
        Current_PORT += 1
        print("Client : ", Current_PORT)
        new_thread = threading.Thread(target=HandleClientThread, args=(conn, addr))
        new_thread.start() 
        threads.append(new_thread)
    except KeyboardInterrupt:
        print("Stopped by Ctrl+C")
        if serverSocket:
              serverSocket.close()
        for thread in threads:
            thread.join()
        sys.exit()#Terminate the program after sending the corresponding data
