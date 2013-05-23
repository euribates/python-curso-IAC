#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

def as_bin(n, width=11):
    s = bin(n)
    s = s[2:]
    s = '0' * width + s
    return s[-width:]

def as_blocks(s):
    output = []
    for c in s:
        if c == '1':
            output.append(u'\u2588\u2588')
        elif c == '0':
            output.append('  ')
        else:
            raise ValueError('%s no es una cadena en binario, no esperaba %s' % (s, c))
    return ''.join(output)

def as_bin(n, width=11):
    s = bin(n)
    s = s[2:]
    s = '0' * width + s
    return s[-width:]

data = [260, 136, 508, 886, 2047, 1533, 1285, 216]
for i,d in enumerate(data):
    print(i, as_bin(d, width=11))


for i,d in enumerate(data):
    print(i, as_blocks(as_bin(d, width=11)))

print()

data = [240, 2046, 4095, 3687, 4095, 408, 876, 3075]
for i,d in enumerate(data):
    print(i, as_blocks(as_bin(d, width=12)))

print()

data = [24, 60, 126, 219, 255, 36, 90, 165]
for i,d in enumerate(data):
    print(i, as_blocks(as_bin(d, width=8)))

