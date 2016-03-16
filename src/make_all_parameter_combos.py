#!/usr/bin/python


param_open = '<parameters>\n'
param_close = '</parameters>\n'
rule = '  <rule>method:two,mu:<MU>,lambda:<LAMBDA></rule>\n'

dirichlets = [100, 1000, 1500, 2500, 500, 5000, 7500]

for i in range(0, 11):
	jm = i/10.0
	for mu in dirichlets:
		with open('two-stage_'+str(jm)+'_'+str(mu), 'w') as out:
			r = rule.replace('<MU>', str(mu)).replace('<LAMBDA>', str(jm))
			out.write(param_open)
			out.write(r)
			out.write(param_close)
	
