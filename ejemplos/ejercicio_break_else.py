#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

# Queremos saber el mayor factorial menor que 1.000.000

acc = num = 1
while acc * (num+1) < 1000000:
    num = num + 1
    acc = num * acc

print('El mayor factorial menor que 1E6 es: ', num, '! = ', acc, sep='')

# Usando la cláusula else, o la clausula break, modificar el programa
# para que muestre el menor factorial mayor que 1.000.000
