#!/usr/bin/env python
# coding=utf-8
import os


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(relpath, name)
            print(full_path)
            print(os.path.normpath(os.path.abspath(full_path)))



if __name__ == "__main__":
    findfile("code", "get_forward_name.py")
