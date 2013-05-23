#!/usr/bin/env python

from __future__ import print_function
from decimal import Decimal

def divide_por_dos(x):
    if x*100 % 2 == 0:
        return (x/2, x/2)
    else:
        return ((x-Decimal('0.01'))/2, ((x-Decimal('0.01'))/2)+Decimal('0.01'))

cantidad = Decimal('74.35')
pago_1, pago_2 = divide_por_dos(cantidad)
print ('Primer pago:', pago_1, '+ segundo pago:', pago_2 , '=', cantidad)

cantidad = Decimal('843.72')
pago_1, pago_2 = divide_por_dos(cantidad)
print ('Primer pago:', pago_1, '+ segundo pago:', pago_2 , '=', cantidad)

def divide_por_tres(x):
    pass
