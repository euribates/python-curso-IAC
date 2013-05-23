#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

def logged(f):
    def result_function(*args, **kwargs):
        print('saludo starts')
        f(*args, **kwargs)
        print('saludo ends')
    result_function.__name__ = f.__name__
    result_function.__doc__ = f.__doc__
    return result_function

@logged
def saludo(s):
    """Imprime una cadena de texto anteponiendo hola.
    """
    print("Hola", s)

print(saludo)
saludo('Jack')
help(saludo)