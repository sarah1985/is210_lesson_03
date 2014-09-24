#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04: Ternary Expressions"""

DAY = raw_input('What day is it?')[:3].lower()
TIME = int(raw_input('What time is it? (e.g. 2300)'))

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if SNOOZE == True:
    print 'Snooze'
else:
    print 'Wake up!'