#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

def as_bin(n):
    s = bin(n)
    s = s[2:]
    s = '0' * 11 + s
    return s[-11:]

print(as_bin(123))