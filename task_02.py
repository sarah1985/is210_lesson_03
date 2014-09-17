#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Simple Branching"""

BP_INPUT = int(raw_input('What is your systolic blood pressure?'))
print BP_INPUT
BP_STATUS = int()

if BP_INPUT <= 90:
    BP_STATUS = 'low'
elif BP_INPUT > 90 and BP_INPUT <= 119:
    BP_STATUS = 'ideal'
elif BP_INPUT > 119 and BP_INPUT <= 139:
    BP_STATUS = 'warning'
elif BP_INPUT > 139 and BP_INPUT <= 160:
    BP_STATUS = 'high'
elif BP_INPUT > 160:
    BP_STATUS = 'emergency'

print'Hello, your blood pressure status is {}.'.format(BP_STATUS)
