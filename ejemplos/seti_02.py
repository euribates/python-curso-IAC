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

data = [260, 136, 508, 886, 2047, 1533, 1285, 216]
for d in data:
    print(as_bin(d, width=11))
