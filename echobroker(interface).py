import socketserver
import socket
import threading
import json
import os
class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        message = self.rfile.readline().strip()
        message = message.decode("utf-8")
        print("msg:"+message)
        message = json.loads(message)
        data = {}
        data['contents'] = message
        answer = ""
        if len(data['contents'])>0: 
                          ClientMultiSocket = socket.socket()
                host = ' '
                port = []
                port = random.choice(port)
                try:
                    ClientMultiSocket.connect((host,port))
                    host, port = ClientMultiSocket.getpeername()
                    print('Connected-->',port)
                    check_isfile = os.path.isfile('registered_port.json')
                    if check_isfile:
                        with open('registered_port.json','r') as readfile:
                            registered_port_ = json.load(readfile)
                        with open('registered_port.json','w') as outfile:
                            if port not in registered_port_.values():
                                if len(registered_port_) == 0:
                                    registered_port_[1] = port
                                    json.dump(registered_port_,outfile)
                                else:
                                    registered_port_[len(registered_port_)+1] = port
                                    json.dump(registered_port_,outfile)
                            else:
                                json.dump(registered_port_,outfile)
                    else:
                        with open('registered_port.json','w') as create_file:
                            json.dump({},create_file)
                        with open('registered_port.json','r') as readfile:
                            registered_port_ = json.load(readfile)
                        with open('registered_port.json','w') as outfile:
                            if port not in registered_port_.values():
                                if len(registered_port_) == 0:
                                    registered_port_[1] = port
                                    json.dump(registered_port_,outfile)
                                else:
                                    registered_port_[len(registered_port_)+1] = port
                                    json.dump(registered_port_,outfile)
                            else:
                                json.dump(registered_port_,outfile)                        
                except socket.error as e:
                    print(str(e))
                res = ClientMultiSocket.recv(1024)
                if True:
                    Input = data["contents"]
                    print('Input---->',Input)
                    ClientMultiSocket.send(str.encode(Input))
                    res = ClientMultiSocket.recv(1024)
                    print('irsen message----->',res)
                    response = res.decode('utf-8')
                    print('message: ', response)
                answer = response
            ClientMultiSocket.close()
        # creating response message...
        self.wfile.write(answer.encode("utf-8"))
