import socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1' ,53210))
client_sock.sendall(b'Hello, world')
data=client_sock.recv(1024)
client_sock.close()
print ('Received', repr(data))

import socket
serv_sock=socket.socket (socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('',53210))
serv_sock.listen(10)
while True:
    client_sock, client_addr=serv_sock.accept ()
    print (' Connected by', client_addr) 
    while True:
        data=client_sock.recv(1024)
        if not data: 
            break
        client_sock.sendall(data)
    client_sock.close()
