#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import math

def perimetro(r):
    """Devuelve el perímetro de una circunferencia de radio r.
    """
    return 2 * math.pi * r

radio = 6
print('El perímetro de una circunferencia de radio', radio, 'es:', perimetro(radio))
