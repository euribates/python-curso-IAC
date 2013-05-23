#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import datetime
    
class Empleado:
    def __init__(self, nombre, edad):
        self.set_nombre(nombre)
        self.set_edad(edad)
        
    def __str__(self):
        return self.get_nombre()

    def set_edad(self, edad):
        self._edad = edad
        
    def get_edad(self):
        return self._edad

    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre
            
#
# 9.000 líneas de código después
#

def es_jubilable(empl):
    return empl.get_edad() > 65

tyson = Empleado('Neil deGrasse Tyson', 54)
print tyson, es_jubilable(tyson) # False
