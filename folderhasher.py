#!/usr/bin/env python3

from hashlib import sha1
from os import listdir, path

from sys import argv


def hash_file(file_path):
    with open(file_path, 'rb') as file:
        contents = file.read()
        return sha1(contents).hexdigest()


def hash_folder(base_path, folder='', recursion=-1):
    if recursion >= 0:
        print(('  ' * recursion) + folder)
    files = listdir(base_path + folder)
    files.sort()
    for item in files:
        if path.isdir(base_path + folder + item):
            hash_folder(base_path, folder + item + '/', recursion=recursion + 1)
    for item in files:
        if path.isfile(base_path + folder + item):
            print('%s%s-%s' % (('  ' * (recursion + 1)), hash_file(base_path + folder + item), item))


base_path = argv[1]
if not base_path.endswith('/'):
    base_path += '/'
if not path.isdir(base_path):
    raise BaseException('Not a valid directory: %s' % base_path)
hash_folder(base_path)
