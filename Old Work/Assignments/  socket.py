 from socket import *
from sys import *

#number of arguments 
if len(argv) != 4:
    print('Usage:', argv[0], '<serverName> <portNumber> <clientName>')
    exit()

    #server contact information and client name
    serverName = argv[1]
    serverPort = int(argv[2])
    clientName = argv[3]

    #create the client socket
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((serverName, serverPort))
    print(f'Connected to server at ({serverName}, {serverPort})')

    sockFile = sock.makefile('r+')

    try:
        while True:
            line = input(f'{clientName}: ')
            sockFile.write(line + '\n')
            sockFile.flush()
            #read and print the server's response
            response = sockFule.readline()
            if not response:
                print('Server closed the connection')
                break
            print(f'Server: {response.strip()}')

    finally:
        #cleanup
        sockFile.close()
        sock.close()
        