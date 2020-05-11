#!/usr/bin/env python3

"""
Написать программу поиска всех файлов в указанном каталоге,
содержащих заданное число. Формат вызова программы:
numbersearch <путь> <искомое число>.
Программа должна выводить имена всех файлов в один столбец.
"""

import os
import argparse


parser = argparse.ArgumentParser(description='Find files with number.')
parser.add_argument('path', type=str,
                    help='path where to find the files')
parser.add_argument('number', type=int,
                    help='word which must contain the file name')


_text_characters = (
        b''.join(bytes((i,)) for i in range(32, 127)) +
        b'\n\r\t\f\b')


def istextfile(fileobj, blocksize=512):
    """ Использует эвристику для определения типа файлов, текстовый или
        бинарный читая 512-байтный блок байтов из файла.
        Если более 30% символов в блоке не текстовые или есть NULL ('\x00')
        байты в блоке, считаем файл бинарным.
    """
    block = fileobj.read(blocksize)
    if b'\x00' in block:
        # Файлы с NULL байтами бинарные
        return False
    elif not block:
        # Пустой файл считаем текстовым
        return True

    # Удаляем печатные символы
    nontext = block.translate(None, _text_characters)
    # Возвращаем результат
    return float(len(nontext)) / len(block) <= 0.30


def find_in_path(path, number):
    # проверка существования пути
    if os.path.exists(path):
        # итерация по списку файлов в каталоге
        for file_name in os.listdir(path):
            # получаем относительный путь
            file = os.path.join(path, file_name)
            # проверяем является ли объект файлом
            if os.path.isfile(file):
                # открываем файл
                with open(file, 'rb') as fileobj:
                    # проверка содержимого файла
                    if istextfile(fileobj):
                        # перемещение курсора в начало
                        fileobj.seek(0)
                        # читаем содержимое файла
                        text = fileobj.read()
                        # проверяем вхождения числа в содержимое файла
                        if str(number) in text.decode('utf8'):
                            print(file_name)


if __name__ == "__main__":
    args = parser.parse_args()
    find_in_path(args.path, args.number)
