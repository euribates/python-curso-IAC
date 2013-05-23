#!/usr/bin/env python

from __future__ import print_function
from decimal import Decimal

print(.1+.1+.1+.1+.1+.1+.1+.1+.1+.1 == 1.0)
print(.1+.1+.1+.1+.1+.1+.1+.1+.1+.1 - 1.0)

a = Decimal('0.1')
print (a+a+a+a+a+a+a+a+a+a == Decimal('1.0'))