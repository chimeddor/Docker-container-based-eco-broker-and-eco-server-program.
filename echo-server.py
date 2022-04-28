import socket
import os
import json
from _thread import *

ServerSideSocket = socket.socket()
host = 'IP'
port = <Port_Number>
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening.. {}'.format(ServerSideSocket.getsockname()))
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        with open('registered_port.json','r') as infile:
            df = json.load(infile)
            for key, value in df.items():
                if port == int(value):
                    my_name_ = key
        data = connection.recv(2048)
        response = my_name_ + '번 에커 서버: '+data.decode('utf-8')
        # return response
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()
    return response

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
