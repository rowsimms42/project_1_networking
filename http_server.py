# source: class book: Computer Networking by Kurose and Ross

from socket import *

server_port = 4242
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((gethostname(), server_port))
data = "HTTP/1.1 200 OK\r\n" \
       "Content-Type: text/html; charset=UTF-8\r\n\r\n" \
       "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
# server waits
server_socket.listen(1)
print("The server on port %d is listening." % server_port)
while True:
    connection_socket, address = server_socket.accept()
    rec_msg = connection_socket.recv(1024).decode()
    print(rec_msg)
    send_msg = data
    connection_socket.send(send_msg.encode())
    print(data)
    connection_socket.close()
