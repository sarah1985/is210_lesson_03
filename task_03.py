#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Nested Statements"""

BASE = raw_input('Do you prefer Seattle Gray or Manatee?').lower()
ACCENT = 0
HIGHLIGHT = 0

if BASE == 'seattle gray':
    ACCENT = raw_input('Do you prefer Ceramic Glaze or Cumulus Nimbus?').lower()
    if ACCENT == 'ceramic glaze':
        HIGHLIGHT = raw_input('Do you prefer Basically White or White?').lower()
        if HIGHLIGHT == 'basically white':
            print BASE
            print ACCENT
            print HIGHLIGHT
        elif HIGHLIGHT == 'white':
            print BASE
            print ACCENT
            print HIGHLIGHT
    elif ACCENT == 'cumulus nimbus':
        HIGHLIGHT = raw_input('Do you prefer Basically White or
        White?').lower()
        if HIGHLIGHT == 'basically white':
            print BASE
            print ACCENT
            print HIGHLIGHT
        elif HIGHLIGHT == 'white':
            print BASE
            print ACCENT
            print HIGHLIGHT
elif BASE == 'Manatee':
    ACCENT = raw_input('Do you prefer Platinum Mist or Spartan Sage?').lower()
    if ACCENT == 'platinum mist':
        HIGHLIGHT = raw_input('Do you prefer Bone White or Just White?').lower()
        if HIGHLIGHT == 'bone white':
            print BASE
            print ACCENT
            print HIGHLIGHT
        elif HIGHLIGHT == 'just white':
            print BASE
            print ACCENT
            print HIGHLIGHT
    elif ACCENT == 'spartan sage':
        HIGHLIGHT = raw_input('Do you prefer Fractal White or Not White?').lower()
        if HIGHLIGHT == 'fractal white':
            print BASE
            print ACCENT
            print HIGHLIGHT
        elif HIGHLIGHT == 'not white':
            print BASE
            print ACCENT
            print HIGHLIGHT