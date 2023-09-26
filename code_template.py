# Import socket module
from socket import * 
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
#Fill in end

while True:
    #Establish the connection
    print('The server is ready to receive')

    # Set up a new connection from the client
    connectionSocket, addr = #Fill in start          #Fill in end


    try:
        message = #Fill in start          #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start          #Fill in end

        # Send the HTTP response header line to the connection socket
        #Fill in start          
        
        #Fill in end
 
        # Send the content of the requested file to the client
        #Fill in start          

        #Fill in end
        
        # Close the connection socket with this particular client
        connectionSocket.close()

    except IOError:
            # Send response message for file not found
			# Fill in start          

			# Fill in end

            # Close the client connection socket
            #Fill in start          

            #Fill in end

    serverSocket.close()  
    sys.exit()#Terminate the program after sending the corresponding data
