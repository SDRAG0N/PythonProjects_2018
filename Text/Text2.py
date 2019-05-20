import socket

def client():
    client1 = socket.socket()
    client1.connect(('127.0.0.1',12345))
    while True:
        data = input('请输入您要发送的数据')
        client1.send(data.encode())
        if data == 'close':
            client1.close()
            break
        result = client1.recv(1024)
        print('服务端返回的数据是：{}'.format(result))

if __name__ == "__main__":
    client()