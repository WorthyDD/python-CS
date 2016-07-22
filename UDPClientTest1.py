import socket
import threading


def recv_data(sock):
    print('recv data:')
    while True:
        data = sock.recv(1024)
        if(data and data.decode('utf-8')):
            print('server : %s' % data.decode('utf-8'))

def send_data(sock):
    print('send data:')
    while True:
        ans = raw_input()
        sock.sendto(ans, ('0.0.0.0', 9999))


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t1 = threading.Thread(target = recv_data, args = (s,))
t1.start()
t2 = threading.Thread(target = send_data, args = (s,))
t2.start()
