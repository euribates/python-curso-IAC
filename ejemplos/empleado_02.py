#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import datetime
    
class Empleado:
    def __init__(self, nombre, f_nacimiento):
        self.nombre = nombre
        self.f_nacimiento = f_nacimiento
    
    def get_edad(self):
        delta = datetime.date.today() - self.f_nacimiento
        return int(data.days // 365.25)
            
#
# 9.000 líneas de código después
#

def es_jubilable(empl):
    return empl.edad > 65

tyson = Empleado('Neil deGrasse Tyson', 54)
print tyson, es_jubilable(tyson) #--> AttributeError: Empleado instance has no attribute 'edad'
