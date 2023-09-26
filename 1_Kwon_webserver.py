# Import socket module
from socket import * 
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
HOST = "127.0.0.1"
PORT = 6789
#The .bind() method is used to associate the socket with a specific network interface and port number
serverSocket.bind((HOST, PORT))
#.listen() enables a server to accept connections
serverSocket.listen()
#Fill in end

while True:
    #Establish the connection
    print('The server is ready to receive')

    # Set up a new connection from the client - The .accept() method blocks execution and waits for 
    # an incoming connection. When a client connects, it returns a new socket object representing 
    # the connection and a tuple holding the address of the client
    connectionSocket, addr = serverSocket.accept()


    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send the HTTP response header line to the connection socket
        #Fill in start    
        Header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(Header.encode('utf-8'))      
        
        #Fill in end
 
        # Send the content of the requested file to the client
        #Fill in start
        connectionSocket.sendall(outputdata.encode('utf-8'))          

        #Fill in end
        
        # Close the connection socket with this particular client
        connectionSocket.close()

    except IOError:
            # Send response message for file not found
			# Fill in start   
            ErrorMessage = "HTTP/1.1 404 Not found\r\n\r\n"   
            connectionSocket.send(ErrorMessage.encode('utf-8'))   
            #ErrorHTML = "<html><head></head><body><h1>File Not Found</h1></body></html>\r\n"
            #connectionSocket.send("<html><head></head><body><h1>File Not Found</h1></body></html>\r\n")
			# Fill in end

            # Close the client connection socket
            #Fill in start   
            connectionSocket.close()      
            #Fill in end

    serverSocket.close()  
    sys.exit()#Terminate the program after sending the corresponding data



    # http://127.0.0.1:6789/HelloWorld.html