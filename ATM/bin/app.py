#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/2/9
import sys,os

def env_path():
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(path)
env_path()
if __name__ == '__main__':
    print('song')