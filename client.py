import socket
import time

from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 31182))
login = "jura".encode('utf-8')
password = "odin"

list= (login)

s.send(list)

def thread(s):
    t = Thread(target=mes, args=(s, 2))
    t2 = Thread(target=sending, args=(s, 2))
    t.start()
    t2.start()


def mes(s, num=0):
    while True:
        data = s.recv(1024)
        print("\nNew message ",data.decode("utf-8"),"\nSano Jotian : ")
        time.sleep(1)

def sending(s, num=0):
    while True:
        text = input("Sano Jotian : ").encode("utf-8")
        s.sendall(text)



if __name__ == '__main__':
        thread(s)

