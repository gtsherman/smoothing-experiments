#!/usr/bin/python

from bs4 import BeautifulSoup
from sys import argv


with open(argv[1]) as f:
	xml = BeautifulSoup(f)
	for query in xml.find_all('query'):
		num = query.find('number').get_text().strip()
		text = query.find('text').get_text().strip()
		print('\t'.join([num, text]))
