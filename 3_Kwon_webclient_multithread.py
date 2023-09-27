from socket import * 
import time
import sys # In order to terminate the program

clientSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#HOST = str(input("Input the Server Hostname/IP"))  #The server hostname/IP
#PORT = int(input("Input the Port Number"))   #The Port used by the Server
#FILENAME = str(input("Input the Filename"))
HOST = "127.0.0.1"
PORT = 6789
FILENAME = "HelloWorld.html"
clientSocket.connect((HOST, PORT))

while True:
    #Establish the connection
    print('The Client is ready to Send')

    try:
        HTTP_REQUEST = "GET /"+FILENAME+" HTTP/1.1\r\nHost: "+HOST + ":"+str(PORT)+"\r\n\r\n"
        print(HTTP_REQUEST)
        clientSocket.sendall(HTTP_REQUEST.encode('utf-8')) 

        response = clientSocket.recv(1024)
        response = response.decode('utf-8')
        print(response[6:])
        print(response[:5])

        PORT = response[:5]
        #print("Port is : ",PORT)

        clientSocket.close()

        #Note that your code must first close the current socket connection, and then establish a new TCP connection to the same server but on the new port number.

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((HOST, int(PORT)))

        HTML_RESPONSE = clientSocket.recv(1024)
        print(HTML_RESPONSE.decode('utf-8'))

        clientSocket.close()
        sys.exit()#Terminate the program after sending the corresponding data

    except IOError:
            print("ERROR")

            # Close the client connection socket  
            clientSocket.close()  
            sys.exit()#Terminate the program after sending the corresponding data   
    except KeyboardInterrupt:
        print("Stopped Client by Ctrl+C")
        if clientSocket:
              clientSocket.close()
        sys.exit()#Terminate the program after sending the corresponding data   
