#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04: Ternary Expressions"""

DAY = raw_input('What day is it?').lower()
TIME = int(raw_input('What time is it? (e.g. 2300)'))
SNOOZE = 'Snooze'

SNOOZE if DAY == ('saturday', 'sunday') else TIME < 0600
print 'SNOOZE'