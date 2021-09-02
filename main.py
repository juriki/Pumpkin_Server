import socket
import time
from threading import Thread

PORT = 31182
HOST = 'localhost'
users =  []

def sok_Strating(port, host):
    # Создание Сокета Который будет принимать данные
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket is Created")

    if sock.bind((host, port)) != None:
        print("Poblem Whit Bind")

    if sock.listen(0) != None:
        print("Poblem whit Listening")
    return sock


def connection(server):
    while True:
        conn, addr = server.accept()
        print("Имя и IP юзера", conn, "\n", addr)
        t = Thread(target=message, args=(conn, addr, server))
        users.append(conn)
        t.start()

def message(conn, adrr, server):
    print(len(users))
    while True:
            a = conn.recv(2048)
            if not a:
                break
            else:
                print(a, " From User :  ")
            for user in users:
                 try:
                     user.send(a)
                 except BrokenPipeError:
                     users.remove(user)
                     print(user, "\n\n REMOWED" )
                     print(len(users))


if __name__ == "__main__":
        server = sok_Strating(PORT, HOST)
        while True:
            connection(server)