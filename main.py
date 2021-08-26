import socket
from select import select
import asyncio
import time
from threading import Thread

PORT = 31182
HOST = 'localhost'
users =  []

def sok_Strating(port, host):
    # Создание Сокета Который будет принимать данные
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket is Created")

    if sock.bind((host, port)) != None:
        print("Poblem Whit Bind")

    if sock.listen(5) != None:
        print("Poblem whit Listening")
    return sock


def connection(server):
    while True:
        conn, addr = server.accept()
        print("Имя и IP юзера", conn, "\n", addr)
        t = Thread(target=message, args=(conn, addr))
        t.start()

def message(conn, adrr):
        while True:
            a = conn.recv(1024)
            if not a:
                break
            print(a.decode("utf-8"), " From User :  ")

if __name__ == "__main__":
        server = sok_Strating(PORT, HOST)
        while True:
            connection(server)
