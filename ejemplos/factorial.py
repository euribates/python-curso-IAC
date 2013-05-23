#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

def fact(x):
    acc = 1
    while x > 1:
        acc = acc * x
        x = x - 1
    return acc

def show(x):
    v = fact(x)
    print('El factorial de {} vale {} y es de tipo {}'.format(x, v, type(v)))

show(5)
show(16)
show(50)

