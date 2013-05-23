#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

class A:
    _Tabla = {
        0: 'ninguno',  1: 'uno',     2: 'dos',
        3: 'tres',     4: 'cuatro',  5: 'cinco',
        6: 'umm... seis',
    }
    
    def __len__(self):
        return 7 # por la cara

    def __getitem__(self, index):
        if 0 <= index < 7:
            return self._Tabla[index]
        else:
            return 'Muchos'

    def __setitem__(self, index, value):
        pass

a = A()
print(a[3])
print(a[25])
a[4] = 'IV'
print(a[4])
