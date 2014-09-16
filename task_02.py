#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Simple Branching"""

BP_STATUS = int(raw_input('What is your systolic blood pressure?'))

if BP_STATUS <= 90: 
    print 'Hello, your blood pressure status is low.'
elif BP_STATUS > 90 and BP_STATUS >= 119: 
    print 'Hello, your blood pressure status is ideal.'
elif BP_STATUS > 119 and BP_STATUS <= 139: 
    print 'Hello, your blood pressure status is warning.'
elif BP_STATUS > 139 and BP_STATUS <= 160: 
    print 'Hello, your blood pressure status is high.'
elif BP_STATUS > 160: 
    print 'Hello, your blood pressure status is emergency.'
