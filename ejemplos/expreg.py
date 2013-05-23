#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import re

Texto = '''INSTRUIDO por accidente de circulación ocurrido a las 09:43
entre la motocicleta HONDA 500, matrícula 0765-BBC  y la
motocicleta HARLEY-DAVIDSON , matrícula 9866-LPX, en el punto
kilométrico 3.5 de la carretera general del sur, término municipal de
Arona, Tenerife, y bla, bla, bla...'''

patron = re.compile('[H]?[0-9]{4}-?[BCDFGHJKLMNPRSTVWXYZ]{3}', re.IGNORECASE)
for matricula in patron.findall(Texto):
    print(matricula)