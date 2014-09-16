#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04: Ternary Expressions"""

DAY = raw_input('What day is it?').lower()
TIME = raw_input('What time is it? (e.g. 2300)')
SNOOZE = 'True' if DAY == 'saturday' or DAY == 'sunday' or TIME < 0600 else 'False'
