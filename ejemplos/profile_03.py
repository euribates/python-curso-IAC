#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import cProfile as profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq

# Create 5 set of stats
filenames = []
for i in range(5):
    filename = ’profile_stats_%d.stats’ % i
    profile.run(’print %d, fib_seq(20)’ % i, filename)

# Read all 5 stats files into a single object
stats = pstats.Stats(’profile_stats_0.stats’)
for i in range(1, 5):
    stats.add(’profile_stats_%d.stats’ % i)

# Clean up filenames for the report
stats.strip_dirs()

# Sort the statistics by the cumulative time spent in the function
stats.sort_stats(’cumulative’)
stats.print_stats()