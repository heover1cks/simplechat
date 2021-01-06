from socket import *
import func
import threading

port = 28080

clientSock = socket(AF_INET,SOCK_STREAM)
clientSock.connect(('localhost',28080))

print('connected')

sender = threading.Thread(target=func.send, args=(clientSock,))
receiver = threading.Thread(target=func.recv, args=(clientSock,))

sender.start()
receiver.start()