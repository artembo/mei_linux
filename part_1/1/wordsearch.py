#!/usr/bin/env python3

"""
Написать программу поиска всех файлов в указанном каталоге,
содержащих заданное слово. Формат вызова программы:
wordsearch <путь> <искомое слово>.
Программа должна выводить имена всех файлов в один столбец.
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
        # итерация по файлам в каталоге
        for file_name in os.listdir(path):
            # проверка вхождения слова в имя файла
            if word in file_name:
                print(file_name)


if __name__ == "__main__":
    args = parser.parse_args()

    find_in_path(args.path, args.word)
