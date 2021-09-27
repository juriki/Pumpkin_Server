import socket
import time
from threading import Thread
connection = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 31182))
login = "juriki".encode("utf-8")
connection = True
s.send(login)
send_to_user = "juriki".encode("utf-8")

def thread(s):
        t = Thread(target=mes, args=(s, 2))
        t2 = Thread(target=sending, args=(s, 2))
        if connection == True:
            t.start()
            t2.start()
        else:
            return


def mes(s, num=0):
    global connection
    while True:
        data = s.recv(1024)
        if data == False:
            s.close()
            connection = False
            return False
        elif not data:
            print("server donwn")
            connection = False
            return False
        else:
            print("\nNew message ",data.decode("utf-8"),"\nSano Jotian : ", end=" ")
            time.sleep(1)

def sending(s, num=0):
    global send_to_user
    while True:
        text = input("Sano Jotian : ").encode("utf-8")
        if text == "1".encode("utf-8"):
            send_to_user_va = send_to_user
            send_to_user = input("Input user Name Then press enter : ").encode("utf-8")
            if send_to_user == None:
                send_to_user = send_to_user_va
                print("Next Message to : ", send_to_user.decode("utf-8"))
                continue
            else:
                print("Next Message to : ", send_to_user.decode("utf-8"))
                continue



if __name__ == '__main__':
        thread(s)


