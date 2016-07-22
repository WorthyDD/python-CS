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
        sock.send(ans)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.30.29', 9999))

# print(s.recv(1024).decode('utf-8'))

# while True:
    # print(s.recv(1024).decode('utf-8'))
    # ans = raw_input()
    # s.send(ans)

t1 = threading.Thread(target = recv_data, args = (s,))
t1.start()
t2 = threading.Thread(target = send_data, args = (s,))
t2.start()

# s.close()


# for data in [b'Micheal', b'Tracy', b'Sarah']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
#
# s.send(b'exit')
# s.close()