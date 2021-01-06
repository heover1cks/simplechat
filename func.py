import socket

def send(sock):
  quitFlag = False
  while not quitFlag:
    sendData = input('>>>')
    encoded = sendData.encode('utf-8')
    if encoded == "quit()": quitFlag = True
    sock.send(encoded)

def recv(sock):
  quitFlag = False
  while not quitFlag:
    recvData = sock.recv(1024)
    decoded = recvData.decode('utf-8')
    if decoded == "quit()": quitFlag = True
    print('remote: ',decoded)
