import socket
import threading, time

def recv_data(sock):
    print('recv data:')
    while True:
        data, addr = sock.recvfrom(1024)
        if(data and data.decode('utf-8')):
            print('client : %s' % data.decode('utf-8'))

def send_data(sock, addr):
    print('send data:')
    while True:
        ans = raw_input()
        sock.sendto(ans,addr)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 9999))
data, addr = s.recvfrom(1024)
t1 = threading.Thread(target = recv_data, args = (s,))
t1.start()
t2 = threading.Thread(target = send_data, args = (s,addr))
t2.start()

# s.close()

