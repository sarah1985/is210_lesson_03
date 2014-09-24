#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: Compound Examples"""

from decimal import Decimal
import locale
locale.setlocale(locale.LC_ALL, '')
NAME = raw_input('What is your name?')
PRINCIPAL = int(raw_input('What is the amount of your principal?'))
TERM = int(raw_input('For how many years is this loan being borrowed?'))
PRE_QUAL = raw_input('Are you pre-qualified for this loan?')
PREQUAL_BOOL = True if PRE_QUAL[:1].lower() == 'y' else False
RATE = 0

if PRINCIPAL < 0:
    RATE = None
if 0 <= PRINCIPAL < 200000:
    if 1 <= TERM <= 15:
        if PREQUAL_BOOL:
            RATE = Decimal('0.0363')
        else:
            RATE = Decimal('0.0465')
    elif 15 < TERM <= 20:
        if PREQUAL_BOOL:
            RATE = Decimal('0.0404')
        else:
            RATE = Decimal('0.0498')
    elif 20 < TERM <= 30:
        if PREQUAL_BOOL:
            RATE = Decimal('0.0577')
        else:
            RATE = Decimal('0.0639')
if 200000 <= PRINCIPAL < 1000000:
    if 1 <= TERM <= 15:
        if PREQUAL_BOOL:
            RATE = Decimal('0.0302')
        else:
            RATE = Decimal('0.0398')
    elif 15 < TERM <= 20:
        if PREQUAL_BOOL:
            RATE = Decimal('0.0327')
        else:
            RATE = Decimal('0.0408')
    elif 20 < TERM <= 30:
        if PREQUAL_BOOL:
            RATE = Decimal('0.0466')
        else:
            RATE = None
if PRINCIPAL >= 1000000:
    if 1 <= TERM <= 15:
        if PREQUAL_BOOL:
            RATE = Decimal('0.0205')
        else:
            RATE = None
    elif 15 < TERM <= 20:
        if PREQUAL_BOOL:
            RATE = Decimal('0.0262')
        else:
            RATE = None

if RATE is None:
    TOTAL = 0
else:
    TOTAL = PRINCIPAL * (1 + (RATE/12))**(12 * TERM)
    TOTAL = int(round(TOTAL))

REPORT = '''
Loan Report for: {0}
-------------------------------------------------------------
    Principal:       {1:>15}
    Duration:        {2:>15}
    Pre-qualified?   {3:>15}

    Total:           {4:>15}'''.format(
    NAME,
    locale.currency(PRINCIPAL, grouping=True),
    str(TERM) + 'yrs',
    PRE_QUAL,
    locale.currency(TOTAL, grouping=True)
)

print REPORT