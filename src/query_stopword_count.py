#!/usr/bin/python

from sys import argv


query_file = argv[1]
stoplist_file = argv[2]

stopwords = set()
with open(stoplist_file) as f:
	for line in f:
		stopwords.add(line.strip())

with open(query_file) as f:
	for line in f:
		num, text = line.split('\t')
		words = text.split()
		stops = 0
		for word in words:
			stops += 1 if word in stopwords else 0
		print('\t'.join([num, str(stops)]))
