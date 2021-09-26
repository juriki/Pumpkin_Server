import socket
import time
from threading import Thread
import sqlrequest

users_toadd = []
users_online = []
users_offline = []
PORT = 31182
HOST = 'localhost'


class Socket_start:
    def __init__(self, PORT, HOST):
        self.port = PORT
        self.host = HOST


    def socket_Strat(self):
        # Создание Сокета Который будет принимать данные
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Socket is Created")

        if sock.bind((self.host, self.port)) != None:
            print("Poblem Whit Bind")

        if sock.listen(0) != None:
            print("Poblem whit Listening")
        return sock


class datbase_request:
    def __init__(self, users_toadd = []):
        self.users_toadd = users_toadd
        print(len(self.users_toadd), "user len")
    def online_status(self,user_name, num):
        if sqlrequest.chek_User(user_name, num):
            print("sql working")
            return True
        else:
            return False


def connection(server):
    while True:
        conn, addr = server.accept()
        name = conn.recv(1024).decode('utf-8')
        users_toadd.append((name, conn))
        sqlrequest.chek_User(name)
        t = Thread(target=user_start, args=(conn, addr, server))
        t.start()


class user_start:
    def __init__(self, conn, adrr, server):
        while True:
                send_to = conn.recv(512)
                a = conn.recv(2048)
                if not a:
                    break
                else:
                    print(a, "\tmessage to :\t" , send_to.decode("utf-8"))
                for name in users_toadd:
                    if send_to.decode("utf-8") == name[0]:
                        name[1].send(a)
                    else:
                        continue

if __name__ == "__main__":
        server = Socket_start(PORT, HOST)
        run = server.socket_Strat()
        while True:
            connection(run)