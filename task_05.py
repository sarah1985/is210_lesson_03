#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: Compound Examples"""

NAME = raw_input('What is your name?')
PRINCIPAL = int(raw_input('What is the amount of your principal (the amount being borrowed)?'))
TERM = int(raw_input('For how many years is this loan being borrowed?'))
PRE_QUAL = raw_input('Are you pre-qualified for this loan?')
INT = 0

if 0 <= PRINCIPAL <= 199999:
	if 1 <= TERM <= 15:
		if PRE_QUAL == 'Yes':
			INT = float(0.0363)
		else PRE_QUAL == 'No':
			INT = float(0.0465)
	elif 15 < TERM <= 20:
		if PRE_QUAL == 'Yes':
			INT = float(0.0404)
		else PRE_QUAL == 'No':
			INT = float(0.0498)
	elif 20 < TERM <= 30:
		if PRE_QUAL == 'Yes':
			INT = float(0.0577)
		else PRE_QUAL == 'No':
			INT = float(0.0639)
if 200000 <= PRINCIPAL <= 999999:
	if 1 <= TERM <= 15:
		if PRE_QUAL == 'Yes': 
			INT = float(0.0302)
		else PRE_QUAL == 'No':
			INT = float(0.0398)
	elif 15 < TERM <= 20:
		if PRE_QUAL == 'Yes':
			INT = float(0.0327)
		else PRE_QUAL == 'No':
			INT = float(0.0408)
	elif 20 < TERM <= 30:
		if PRE_QUAL == 'Yes':
			INT = float(0.0466)
		else PRE_QUAL == 'No':
			INT = NULL
			print 'None'
if PRINCIPAL > 1000000:
	if 1 <= TERM <= 15:
		if PRE_QUAL == 'Yes':
			INT = float(0.0205)
		else PRE_QUAL == 'No':
			INT = NULL
			print 'None'
	elif 15 < TERM <= 20:
		if PRE_QUAL == 'Yes':
			INT = float(0.0262)
		else PRE_QUAL == 'No':
			INT = NULL
			print 'None'

TOTAL = round(PRINCIPAL * [1 + (INT/12)]**(12 * TERM))

REPORT = '''
Loan Report for: {}
-------------------------------------------------------------
	Principal:			${}
	Duration:			{} yrs
	Pre-qualified?		{}
	
	Total:				${}'''.format(NAME, PRINCIPAL, DURATION, PRE_QUAL)

print REPORT