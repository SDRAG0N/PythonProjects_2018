import  multiprocessing
import socket

class ServerProcess(object):
    def __init__(self, ip, port):
        self.server = socket.socket()
        self.server.bind((ip, port))
        self.server.listen()

    def run(self):
        while True:
            client = self.server.accept()
            pro = multiprocessing.Process(target=self.resp, args=(client,))
            pro.start()

    def resp(self, cli):
        while True:
            result = cli[0].recv(1024)
            if result == b'close':
                cli[0].close()
                break
            print('接收到来自于{}的信息：{}'.format(cli[1], result))

if __name__ == '__main__':
    s = ServerProcess('0.0.0.0', 12345)
    s.run()