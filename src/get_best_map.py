#!/usr/bin/python

import fileinput


max_map = 0.0
for line in fileinput.input():
	if len(line.split()) <= 1:
		continue
	m, q, ap = line.split()
	if float(ap) > max_map:
		max_map = float(ap)
		print(line)
