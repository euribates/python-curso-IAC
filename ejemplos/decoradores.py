#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

def logged(func):
    def inner(* args, **kwargs):
        print('Empieza la función {}'. format(func.__name__))
        func(*args, **kwargs)
        print('Termina la función {}'. format(func.__name__))

    return inner

def a(): print('Soy a()')

def b(): print('Soy b()')
b = logged(b)

@logged
def c(): print('Soy c()')

@logged
def d(msg): print('Soy d y digo: {}'.format(msg))

a()
b()
c()
d('Hola, mundo')
