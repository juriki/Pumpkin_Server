import socket
import asyncio
import time
from threading import Thread

PORT = 31181
HOST = 'localhost'
users =  []


def sok_Strating(port, host):
    # Создание Сокета Который будет принимать данные
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.bind((host, port)) != None:
        print("Poblem Whit Bind")
    if sock.listen(5) != None:
        print("Poblem whit Listening")
    sock.setblocking(False)
    return sock


async def connection(server):
    loop = asyncio.get_event_loop()
    while True:
        conn, addr = await loop.sock_accept(server)
        print("Имя и IP юзера", conn, "\n", addr)
        await message(conn)
        return conn


async def message(conn):
    loop = asyncio.get_event_loop()
    while True:
        message = await loop.sock_recv(conn, 1024)
        print(message, " From User :  ")


async def main(srver):
    while True:
        task = asyncio.create_task(connection(server))
        await task
        await message(task)

if __name__ == "__main__":
    server = sok_Strating(PORT, HOST)
    print("Socket is Created")
    asyncio.run(main(server))