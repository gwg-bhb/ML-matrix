#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-07-30 10:43
#@Author: daemon
#@File  : 2-1.py.py

print("hello world")

#import

import time
print(time.localtime())

import time as t
print(t.localtime())
print(t.asctime())

from time import localtime,time
print(localtime())
print(time())

try:
    file = open('aaa', 'r+')
except Exception as e:
    print("no this file")

string=' test '
number=1

print(string.title())
print(string.upper())
print(string.lower())
print("\n")

print(string.rstrip())
print(string.lstrip())
print(string.strip())

listT1=['a', 'b', 'c', 'd']
print(listT1[-1])

listT1=['a', 'b', 'c', 'd', 'g']
listT1.append('f')
print(listT1)

listT1=['a', 'b', 'c', 'd']
listT1.insert(0, '0')
print(listT1)

listT1=['a', 'b', 'c', 'd']
del listT1[0]
print(listT1)

listT1=['a', 'b', 'c', 'd']
print("5th")
tp1=listT1.pop()
print(tp1)
print(listT1)
tp1=listT1.pop(0)
print(tp1)
print(listT1)
