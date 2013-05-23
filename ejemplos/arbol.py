#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

for i in range(16):
    print(' ' * (16-i), '*' * (1+2*i), ' ' * (16-i))
else:
    for i in range(5):
        print(' ' * 15, '***')