import socket
import threading, time

def tcplink(sock, addr):
    print('Accept new connect from (%s, %s)' % (sock, addr))
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        ans = raw_input()
        # print(ans)
        # bytes(ans, encoding = 'utf-8')
        sock.send(ans)
        # sock.send(('Hello, %s' % data.decode('utf-8').encode('utf-8')))
    sock.close()
    print('Connection from (%s, %s) is closed' % (sock,addr))


def recv_data(sock, addr):
    print('recv data:')
    while True:
        data = sock.recv(1024)
        if(data and data.decode('utf-8')):
            print('client : %s' % data.decode('utf-8'))

def send_data(sock, addr):
    print('send data:')
    while True:
        ans = raw_input()
        sock.send(ans)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))
s.listen(5)
print('waiting connection......')

while True:
    sock, addr = s.accept()

    # t = threading.Thread(target=tcplink, args=(sock, addr))
    # t.start()

    print('Accept new connect from (%s, %s)' % (sock, addr))
    t1 = threading.Thread(target = recv_data, args=(sock, addr))
    t1.start()
    t2 = threading.Thread(target = send_data, args = (sock, addr))
    t2.start()

s.close()

