#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import hashlib

m = hashlib.md5()
m.update("Su teoría es descabellada".encode('utf-8'))
m.update(", pero no lo suficente".encode('utf-8'))
m.update(" para ser correcta.".encode('utf-8'))
print(m.hexdigest()) # 46c8a761de36c7306532ae6f1013164c
m = hashlib.md5()
m.update('Su teoría es descabellada, pero no lo suficente para ser correcta.'.encode('utf-8'))
print(m.hexdigest())  # 46c8a761de36c7306532ae6f1013164c