#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Simple Branching"""

BP_STATUS = int(raw_input('What is your systolic blood pressure?'))
print 'Hello, your blood pressure status is {}.'.format('low' if BP_STATUS <= 90 elif 'ideal' if BP_STATUS >90 and >=119 elif 'warning' if BP_STATUS >119 and <= 139 elif 'high' if BP_STATUS >139 and <= 160 elif 'emergency' if BP_STATUS >160)

    
