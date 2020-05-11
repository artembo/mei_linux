#!/usr/bin/env python3

"""
Написать программу вывода списка имен всех файлов из
указанного каталога и всех вложенных в алфавитном порядке
с указанием размера файла. Формат вызова программы: filelist <путь>.
Программа должна выводить список файлов в два столбца: имя файла, размер файла.
"""

import os
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('path', type=str,
                    help='path where to find the files')


def find_in_path(path):
    if os.path.exists(path):
        # итерация по каталогу
        for file_name in os.listdir(path):
            # получаем путь к файлу
            _path = os.path.join(path, file_name)
            # проверка существования файла
            if os.path.exists(_path):
                # определяем размер файла
                size = os.stat(_path).st_size
                print(f"{file_name:20} {size:10}")


if __name__ == "__main__":
    args = parser.parse_args()

    find_in_path(args.path)
