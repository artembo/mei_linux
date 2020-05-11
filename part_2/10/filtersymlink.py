#!/usr/bin/env python3

"""
Написать программу автоматического создания символических ссылок
на все файлы из указанного каталога, содержащие в названии заданную
строку. Все ссылки должны быть сохранены в одном каталоге.
Формат вызова программы: filtersymlink <каталог с файлами> <строка> <каталог со ссылками>
"""

import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('source_path', type=str,
                    help='source path with files')
parser.add_argument('string', type=str,
                    help='string contain')
parser.add_argument('dest_path', type=str,
                    help='destination path to create symlinks')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def find_in_path(source, string, dest):
    # Делаем абсолютные пути
    if not source.startswith('/'):
        source = os.path.join(BASE_DIR, source)
    if not dest.startswith('/'):
        dest = os.path.join(BASE_DIR, dest)
    # Создание каталога назначения, если он не существует
    Path(dest).mkdir(parents=True, exist_ok=True)
    # Проверка каталога источника
    if os.path.exists(source):
        # Итерация по списку файлов в каталоге источника
        for file_name in os.listdir(source):
            if string in file_name:
                source_path = os.path.join(source, file_name)
                # Пропускаем итерацию, если это каталог
                if os.path.isdir(source_path):
                    break
                # Получение пути назначения
                dest_path = os.path.join(dest, file_name)
                if os.path.exists(source_path):
                    # Создание символической ссылки
                    os.symlink(source_path, dest_path)


if __name__ == "__main__":
    args = parser.parse_args()
    find_in_path(args.source_path, args.string, args.dest_path)
