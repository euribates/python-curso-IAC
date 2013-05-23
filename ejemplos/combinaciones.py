#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import itertools

s = set('ABCD')
print('Combinaciones de ABCD Tomados de uno en uno')
for t in itertools.combinations(s, 1):
    print('{}'.format(*t))
print('Combinaciones de ABCD Tomados de dos en dos')
for t in itertools.combinations(s, 2):
    print('{}{}'.format(*t))
print('Combinaciones de ABCD Tomados de tres en tres')
for t in itertools.combinations(s, 3):
    print('{}{}{}'.format(*t))
print('Combinaciones de ABCD Tomados de cuatro en cuatro')
for t in itertools.combinations(s, 4):
    print('{}{}{}{}'.format(*t))
