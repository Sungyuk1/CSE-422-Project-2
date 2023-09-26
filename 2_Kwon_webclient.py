#You can assume that the HTTP request sent is a GET method. The
#client should take command line arguments specifying the server IP address or host name, the port
#at which the server is listening, and the path at which the requested object is stored at the server.

# Import socket module
from socket import * 
import sys # In order to terminate the program

clientSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
HOST = str(input("Input the Server Hostname/IP"))  #The server hostname/IP
PORT = int(input("Input the Port Number"))   #The Port used by the Server
FILENAME = str(input("Input the Filename"))

while True:
    #Establish the connection
    print('The Client is ready to Send')

    try:
        '''message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()'''

        clientSocket.connect((HOST, PORT))
        HTTP_REQUEST = "GET /"+FILENAME+" HTTP/1.1\r\nHost: "+HOST + ":"+str(PORT)+"\r\n\r\n"
        print(HTTP_REQUEST)
        clientSocket.sendall(HTTP_REQUEST.encode('utf-8')) 

        response = clientSocket.recv(1024)
        print(response.decode('utf-8'))
        HTML_RESPONSE = clientSocket.recv(1024)
        print(HTML_RESPONSE.decode('utf-8'))
        
        
        # Close the connection socket with this particular server
        clientSocket.close()

    except IOError:
            print("ERROR")

            # Close the client connection socket  
            clientSocket.close()      

    clientSocket.close()  
    sys.exit()#Terminate the program after sending the corresponding data
