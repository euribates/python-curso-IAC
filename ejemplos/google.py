#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import urllib2
import re

patTitle = re.compile('<title>([^<]+)</title>', re.IGNORECASE)
url = 'http://www.python.org/'
f = urllib2.urlopen(url)
with open('python.html', 'w') as salida:
    for linea in f.readlines():
        salida.write(linea)
        match = patTitle.search(linea)
        if match:
            print('Titulo:', match.group(1))
f.close()

