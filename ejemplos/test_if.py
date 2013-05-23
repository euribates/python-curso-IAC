#!/usr/bin/env python

from __future__ import print_function

def test_if(predicado, comentario):
    if predicado:
        print(comentario, 'es equivalente a True')
    else:
        print(comentario, 'es equivalente a False')


test_if(None, 'None')
test_if('', 'Una cadena vacia')
test_if(0, 'Cero (entero)')
test_if(0.0, 'Cero (flotante)')
test_if([], 'Una lista vacia')
test_if((), 'Una tupla vacia')
test_if({}, 'Un diccionario vacio')

test_if('Hola, mundo', 'Una cadena no vacia')
test_if(1, 'Uno (entero)')
test_if(7, 'Siete (entero)')
test_if(1.0, 'Uno (flotante)')
test_if(7.0, 'Siete (flotante)')
test_if([1, 'a'], 'Una lista no vacia')
test_if((1, 'a'), 'Una tupla no vacia')
test_if({'uno':1,'dos':2}, 'Un diccionario no vacio')
