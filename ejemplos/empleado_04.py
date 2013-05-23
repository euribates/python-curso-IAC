#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import datetime
    
class Empleado:
    def __init__(self, nombre, f_nacimiento):
        self.set_nombre(nombre)
        self.set_f_nacimiento(f_nacimiento)
        
    def __str__(self):
        return self.get_nombre()

    def set_edad(self, edad):
        raise ValueError('No se puede asignar la edad; modifique la fecha de nacimiento')
        
    def get_edad(self):
        delta = datetime.date.today() - self.f_nacimiento
        return int(delta.days // 365.25)

    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre

    def set_f_nacimiento(self, f_nacimiento):
        self.f_nacimiento = f_nacimiento
        
    def get_f_nacimiento(self):
        return self.f_nacimiento

tyson = Empleado('Neil deGrasse Tyson', datetime.date(1958, 10, 5))
            
#
# 9.000 líneas de código después
#

def es_jubilable(empl):
    return empl.get_edad() > 65


print tyson, es_jubilable(tyson) # False
