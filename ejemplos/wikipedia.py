#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import urllib2

url = 'http://es.wikipedia.org/wiki/Especial:Aleatoria'
headers = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-agent': 'urllib2 (Python 2.7)',
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#    'Accept-Encoding': 'none',
#    'Accept-Language': 'es-ES,en;q=0.8',
#    'Connection': 'keep-alive',
    }
req = urllib2.Request(url, headers=headers)
f = urllib2.urlopen(req)
filename = f.geturl().rsplit('/', 1)[1] + '.html'
print('Salvando', filename, end='')
with open(filename, 'w') as salida:
    salida.write(f.read())
f.close()
print('[OK]')