#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Nested Statements"""

BASE = raw_input('Do you prefer Seattle Gray or Manatee?').lower()
ACCENT = 0
HIGHLIGHT = 0 

if BASE == 'Seattle Gray':
	ACCENT = raw_input('Do you prefer Ceramic Glaze or Cumulus Nimbus?').lower()
	if ACCENT == 'Ceramic Glaze':
		HIGHLIGHT = raw_input('Do you prefer Basically White or White?').lower()
		if HIGHLIGHT == 'Basically White':
			print BASE
			print ACCENT
			print HIGHLIGHT
		elif HIGHLIGHT == 'White':
			print BASE
			print ACCENT
			print HIGHLIGHT
	elif ACCENT == 'Cumulus Nimbus':
		HIGHLIGHT = raw_input('Do you prefer Basically White or White?').lower()
		if HIGHLIGHT == 'Basically White':
			print BASE
			print ACCENT
			print HIGHLIGHT
		elif HIGHLIGHT == 'White':
			print BASE
			print ACCENT
			print HIGHLIGHT
elif BASE == 'Manatee':
	ACCENT = raw_input('Do you prefer Platinum Mist or Spartan Sage?').lower()
	if ACCENT == 'Platinum Mist':
		HIGHLIGHT = raw_input('Do you prefer Bone White or Just White?').lower()
		if HIGHLIGHT == 'Bone White':
			print BASE
			print ACCENT
			print HIGHLIGHT
		elif HIGHLIGHT == 'Just White':
			print BASE
			print ACCENT
			print HIGHLIGHT
	elif ACCENT == 'Spartan Sage':
		HIGHLIGHT = raw_input('Do you prefer Fractal White or Not White?').lower()
		if HIGHLIGHT == 'Fractal White':
			print BASE
			print ACCENT
			print HIGHLIGHT
		elif HIGHLIGHT == 'Not White':
			print BASE
			print ACCENT
			print HIGHLIGHT