from socket import *
import func
import threading

port = 28080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)

print('%d port listening......'%port)


connectionSock, addr = serverSock.accept()

print('connected from: ',str(addr))

sender = threading.Thread(target=func.send, args=(connectionSock,))
receiver = threading.Thread(target=func.recv, args=(connectionSock,))

sender.start()
receiver.start()