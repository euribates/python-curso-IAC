#!/usr/bin/env python

import timeit

def f1():
    result = 'a'
    for i in range(100):
        result += 'a'
    return result

def f2():
    result = ['a']
    for i in range(100):
        result.append('a')
    return ''.join(result)

print('Version sumando strings:', timeit.timeit(f1))
print('Version con listas y join:', timeit.timeit(f2))

