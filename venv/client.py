import socket
import time

from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 31182))
login = "jura".encode('utf-8')
password = "odin"
send_to_user = "juriki".encode("utf-8")

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
        if not data:
            print("Server Down")
            return
        print("\nNew message ",data.decode("utf-8"),"\nSano Jotian : ")

def sending(s, num=0):
    global send_to_user
    while True:
        text = input("Sano Jotian : ").encode("utf-8")
        if text == "1".encode("utf-8"):
            send_to_user_va =send_to_user
            send_to_user = input("Input user Name Then press enter : ").encode("utf-8")
            if send_to_user == None:
                send_to_user =send_to_user_va
                print("Next Message to : ", send_to_user.decode("utf-8"))
                continue
            else:
                print("Next Message to : ", send_to_user.decode("utf-8"))
                continue

        s.send(send_to_user)
        time.sleep(0.01)
        s.send(text)



if __name__ == '__main__':
        thread(s)


