#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

class CuentaAtras:
    def __init__(self, tope):
        self.tope = tope

    def __iter__(self):
        self.counter = self.tope
        return self

    def next(self): return self.__next__() # python 2.7

    def __next__(self):
        result = self.counter
        self.counter -= 1
        if result < 0:
            raise StopIteration
        return result



for i in CuentaAtras(12):
    print(i, end=', ')
print()

for i in CuentaAtras(3):
    print(i, end=', ')
print()

print(*CuentaAtras(7), sep=', ', end='\n')