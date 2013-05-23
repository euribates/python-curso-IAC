#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import math

def area_triangulo(base=0, altura=0, a=0, b=0, c=0):
        if base and altura:
            return (base * altura) / 2.0
        elif a and b and c:
            s = (a + b + c) / 2
            return math.sqrt(s*(s-a)*(s-b)*(s-c))
        else:
            raise ValueError('Hay que especificar base y altura, o los lados a,b,c')

print(area_triangulo(base=3, altura=4))
print(area_triangulo(a=3, b=4, c=5))
print(area_triangulo())