#communication process
#perform socket programming for getting the command via the sockets
#working on the same wifi network

import socket

host=socket.gethostname()
port=9000
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('',port))
server_socket.listen(2)
conn,address=server_socket.accept()
print("Connection from:"+ str(address))

while True:
    data=conn.recv(1024).decode()
    if not data:
        continue
    data=data.lower()
    print("From connected user:"+str(data))

conn.close()

#this process is simple socket programming
