#!/usr/bin/env python3

"""
Написать программу поиска файла по имени в указанном каталоге и во всех вложенных.
Формат вызова программы: filesearch <путь> <имя файла>.
Программа должна вывести путь к искомому файлу.
"""

import os
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('path', type=str,
                    help='path where to find the files')
parser.add_argument('word', type=str,
                    help='word which must contain the file name')


def find_in_path(path, word):
    # проверка существования пути
    if os.path.exists(path):
        # итерация по дереву каталогов
        for _path, _dirs, _files in os.walk(path):
            for file_name in _files:
                # проверка вхождения слова в название файла
                if word in file_name:
                    print(os.path.join(_path, file_name))


if __name__ == "__main__":
    args = parser.parse_args()
    find_in_path(args.path, args.word)
