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
		stops = [word for word in text.split() if word in stopwords]
		print('\t'.join([num, str(len(stops))]))
