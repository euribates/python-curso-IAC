#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

class A:
    def __len__(self):
        return 7 # por la cara

a = A()
print(len(a))