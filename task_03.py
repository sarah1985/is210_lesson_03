#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Nested Statements"""

BASE = raw_input('Do you prefer Seattle Gray or Manatee?').lower()

if BASE == 'seattle gray':
    ACCENT = raw_input(
    'Do you prefer Ceramic Glaze or Cumulus Nimbus?'
).lower()
    if ACCENT == 'ceramic glaze':
        HIGHLIGHT = raw_input(
        'Do you prefer Basically White or White?'
).lower()
        if HIGHLIGHT == 'basically white':
            print BASE.title()
            print ACCENT.title()
            print HIGHLIGHT.title()
        elif HIGHLIGHT == 'white':
            print BASE.title()
            print ACCENT.title()
            print HIGHLIGHT.title()
    elif ACCENT == 'cumulus nimbus':
        HIGHLIGHT = raw_input(
        'Do you prefer Basically White or White?'
).lower()
        if HIGHLIGHT == 'basically white':
            print BASE.title()
            print ACCENT.title()
            print HIGHLIGHT.title()
        elif HIGHLIGHT == 'white':
            print BASE.title()
            print ACCENT.title()
            print HIGHLIGHT.title()
elif BASE == 'manatee':
    ACCENT = raw_input(
    'Do you prefer Platinum Mist or Spartan Sage?'
).lower()
    if ACCENT == 'platinum mist':
        HIGHLIGHT = raw_input(
        'Do you prefer Bone White or Just White?'
).lower()
        if HIGHLIGHT == 'bone white':
            print BASE.title()
            print ACCENT.title()
            print HIGHLIGHT.title()
        elif HIGHLIGHT == 'just white':
            print BASE.title()
            print ACCENT.title()
            print HIGHLIGHT.title()
    elif ACCENT == 'spartan sage':
        HIGHLIGHT = raw_input(
        'Do you prefer Fractal White or Not White?'
).lower()
        if HIGHLIGHT == 'fractal white':
            print BASE.title()
            print ACCENT.title()
            print HIGHLIGHT.title()
        elif HIGHLIGHT == 'not white':
            print BASE.title()
            print ACCENT.title()
            print HIGHLIGHT.title()