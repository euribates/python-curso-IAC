#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import random

n = random.randint(-10, 10)
print(n, 'es', end=' ')
if n == -10:
     print('el límite inferior')
elif -9 <= n < 0:
     print ('negativo')
elif n == 0:
     print('cero')
elif 0 < n <= 9:
     print ('positivo')
else:
    print('el límite superior')