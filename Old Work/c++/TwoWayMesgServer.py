from socket import *
from sys import *

#correct number of arguments
if len(argv) != 3:
    print('Usage:', argv[0], '<portNumber> <serverName>')
    exit()

serverPort = int(argv[1])
serverName = argv[2]

#socket
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', serverPort))
serverSock.listen()

#wait for a client connection
print('Waiting for a client ...')
clientSock, clientAddr = serverSock.accept()
print(f'Connected to a client at {clientAddr}')

#file streams
clientSockFile = clientSock.makefile('r')
serverSockFile = clientSock.makefile('w')

try:
    while True:
        #read a message from the client
        message = clientSockFile.readline()

        if not message:
            print('Client closed connection')
            break

        print(f'{argv[2]}: {message.strip()}')

        #user response
        response = input('Server: ')
        serverSockFile.write(response + '\n')
        serverSockFile.flush()

finally:
    #clean up
    clientSockFile.close()
    serverSockFile.close()
    clientSock.close()
    serverSock.close()
