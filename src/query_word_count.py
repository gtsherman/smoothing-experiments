#!/usr/bin/python

from sys import argv


with open(argv[1]) as f:
	for line in f:
		query, text = line.split('\t')
		count = len(text.split())
		print('\t'.join([query, str(count)]))	
