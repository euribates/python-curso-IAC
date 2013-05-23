#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

def cuenta_ocurrencias(txt, *args):
    result = 0
    for palabra in args:
        result += txt.count(palabra)
    return result

texto = """Muchos años después, frente al pelotón de fusilamiento,
el coronel Aureliano Buendía había de recordar aquella tarde remota
en que su padre le llevó a conocer el hielo."""

print(cuenta_ocurrencias(texto, 'coronel', 'el', 'tarde', 'fusilamiento'))
print(cuenta_ocurrencias(texto, 'remota', 'hielo'))
print(cuenta_ocurrencias(texto))
