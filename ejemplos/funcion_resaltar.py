#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

def resaltar(texto, mark_char='-'):
    size = len(texto)
    print(mark_char * size)
    print(texto)
    print(mark_char * size)

resaltar('Informe sobre probabilidad A')
resaltar('Informe sobre probabilidad A', '=')
