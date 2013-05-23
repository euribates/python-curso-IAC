#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import datetime
    
class Empleado:
    def __init__(self, nombre, f_nacimiento):
        self.nombre = nombre
        self.f_nacimiento = f_nacimiento
        
    def __str__(self):
        return self.nombre

    def set_edad(self, edad):
        raise ValueError('No se puede asignar la edad; modifique la fecha de nacimiento')
        
    def get_edad(self):
        delta = datetime.date.today() - self.f_nacimiento
        return int(delta.days // 365.25)

    edad = property(get_edad, set_edad)

tyson = Empleado('Neil deGrasse Tyson', datetime.date(1958, 10, 5))
            
#
# 9.000 líneas de código después
#

def es_jubilable(empl):
    return empl.edad > 65

print tyson, es_jubilable(tyson) # False
