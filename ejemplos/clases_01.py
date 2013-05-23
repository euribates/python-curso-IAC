#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

class Point:
    def __init__(self, lat, lng):
        self.latitud = lat
        self.longitud = lng

    def esta_en_hemisferio_sur(self):
        return self.latitud < 0 

x = Point(28.4779, -16.3118)
print(x, 'Está en el hemisferio sur', x.esta_en_hemisferio_sur())
print(x, 'Está en el hemisferio sur', Point.esta_en_hemisferio_sur(x))
