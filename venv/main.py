import socket
import time
from threading import Thread
import sqlrequest


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
        name = conn.recv(1024).decode('utf-8')
        if sqlrequest.chek_User(name, 1):
            users.append((name,conn))
        else:
            try:
                conn.send("wrong user name or password".encode('utf-8'))
                conn.send()
                conn.close()
            except TypeError:
                continue
        print("Имя и IP юзера", conn, "\n", addr)
        print(users)
        t = Thread(target=message, args=(conn, addr, server))
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
                     user[1].send(a)
                 except BrokenPipeError:
                     #try:
                     sqlrequest.Disconection(user[0])
                     #except:
                     #    print("SQL error")
                     users.remove(user)
                     print(user, "\n\n REMOWED" )
                     print(len(users))


if __name__ == "__main__":
        server = sok_Strating(PORT, HOST)
        while True:
            connection(server)