#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

from decimal import Decimal
import itertools

ingresos = [
    Decimal('4090.20'),
    Decimal('1910.00'),
    Decimal('1945.45'),
    ]

pagos = [
    Decimal('1404.93'), Decimal('207.68'), Decimal('297.39'), Decimal('1816.42'),
    Decimal('153.56'), Decimal('1286.85'), Decimal('322.9'), Decimal('175.04'),
    Decimal('335.43'), Decimal('259.74'), Decimal('301.28'), Decimal('1384.43'),
    ]

for ingreso in ingresos:
    solucion = None
    for size in range(1, len(pagos)+1):
        # Probando combinaciones de size elementos
        for a_probar in itertools.combinations(pagos, size):
            if sum(a_probar) == ingreso:
                print('Encontrada una solución:')
                solucion = tuple(a_probar)
                print(*['{0:f}'.format(d) for d in solucion], sep=' + ', end=' = ')
                print(ingreso)
                break
    if solucion:
        for pago in solucion:
            pagos.remove(pago)

