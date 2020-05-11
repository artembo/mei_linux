import socket
import multiprocessing
from time import sleep


def server_process():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('127.0.0.1', 5050))
        client_list = []  # Массив для хранения адреса клиентов
        print('Сервер запущен')
        while True:
            data, address = sock.recvfrom(1024)
            print(address[0], address[1])
            if address not in client_list:
                client_list.append(address)  # Если такого клиента нету, то добавить
            for client in client_list:
                if client == address:
                    continue  # Не отправлять данные клиенту, который их прислал
                sock.sendto(data, client)
    except OSError:
        pass


def read_sok():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind(('', 0))  # Задаем сокет как клиент
    conn.sendto((alias + ' подключился').encode('utf-8'), server_address)
    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))


if __name__ == "__main__":
    alias = input("Ваше имя: ")  # Вводим наш псевдоним
    server_address = '127.0.0.1', 5050  # Данные сервера

    server = multiprocessing.Process(target=server_process, daemon=True)
    server.start()

    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.bind(('', 0))  # Задаем сокет как клиент
    connection.sendto((alias + ' Connect to server').encode('utf-8'), server_address)  # Уведомляем сервер о подключении
    job = multiprocessing.Process(target=read_sok, daemon=True)
    job.start()

    while True:
        # задержка приглашения ввода
        sleep(0.1)
        msg = input("> ")
        connection.sendto(('[' + alias + '] ' + msg).encode('utf-8'), server_address)
