# source: class book: Computer Networking by Kurose and Ross

from socket import *

server_name = "gaia.cs.umass.edu"
port_number = 80
# create client socket
# sock_stream indicates TCP socket rather than UDP
client_socket = socket(AF_INET, SOCK_STREAM)
# establish connection between server and client
client_socket.connect((server_name, port_number))
req_msg = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
# send message to server
client_socket.send(req_msg.encode())
# waits to receive bytes from server
# receives message
rec_msg = client_socket.recv(4026)
print(rec_msg.decode())
# close connection
client_socket.close()
