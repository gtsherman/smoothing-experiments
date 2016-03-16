#!/usr/bin/python

import os, sys


results_dir = sys.argv[1]

results = {}
mus = {}
max_map = 0
for results_file in os.listdir(results_dir):
	with open(results_dir+'/'+results_file) as f:
		mean_ap = 0.0
		for line in f:
			m, query, ap = line.split()
			ap = float(ap)
			mean_ap += ap
			if query not in results or ap > results[query]:
				results[query] = ap
				mus[query] = results_file.replace('dirichlet_', '').replace('jm_', '')
		mean_ap /= len(results)
		if mean_ap > max_map:
			max_map = mean_ap

optimal_map = 0.0
for query in results:
	optimal_map += results[query]
	print('\t'.join([query, mus[query]]))
optimal_map /= len(results)

print('Max actual map: '+str(max_map))
print('Optimal map: '+str(optimal_map))
