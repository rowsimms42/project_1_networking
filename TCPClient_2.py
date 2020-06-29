# source: class book: Computer Networking by Kurose and Ross
# source: https://pythonprogramming.net/sockets-tutorial-python-3/

from socket import *

server_name = "gaia.cs.umass.edu"
port_number = 80
# create client socket
# sock_stream indicates TCP socket rather than UDP
client_socket = socket(AF_INET, SOCK_STREAM)
# establish connection between server and client
client_socket.connect((server_name, port_number))
complete_rec_msg = ''
req_msg = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
# send message to server
client_socket.send(req_msg.encode())
# waits to receive bytes from server
# receives message
while True:
    rec_msg = client_socket.recv(8)

    if len(rec_msg) <= 0:
        break
    complete_rec_msg += rec_msg.decode("utf-8")
print(complete_rec_msg)

# close connection
client_socket.close()
