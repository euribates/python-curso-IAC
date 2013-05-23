#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return self.nombre
            
#
# 9.000 líneas de código después
#

def es_jubilable(empl):
    return empl.edad > 65

tyson = Empleado('Neil deGrasse Tyson', 54)
print tyson, es_jubilable(tyson) #--> False
