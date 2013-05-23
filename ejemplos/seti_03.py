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
    output = ''
    for c in s:
        if c == '1':
            output += u'\u2588\u2588'
        elif c == '0':
            output += '  '
        else:
            raise ValueError('No es 1/0')
    return output

print('Señal 1')
data = [260, 136, 508, 886, 2047, 1533, 1285, 216]
for d in data:
    print(as_blocks(as_bin(d, width=11)))

print('Señal 2')
data = [240, 2046, 4095, 3687, 4095, 408, 876, 3075]
for d in data:
    print(as_blocks(as_bin(d, width=12)))

print('Señal 3')
data = [24, 60, 126, 219, 255, 36, 90, 165]
for d in data:
    print(as_blocks(as_bin(d, width=8)))
