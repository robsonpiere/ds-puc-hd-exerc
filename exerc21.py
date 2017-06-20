'''
Aluno: Robson Henrique Piere
robsonpiere@outlook.com
'''

import mincemeat
import glob
import csv

text_files = glob.glob('textos\\*')
def file_contents(file_name):
	f = open(file_name)
	try:
		return f.read()
	finally:
		f.close()

def mapfn(k,v):
	print 'map ' + k
	from stopwords import allStopWords
	for line in v.splitlines():
		for word in line.split():
			if (word not in allStopWords):
				yield word,1

def reducefn(k,v):
	print 'reduce ' + k
	return sum(v)

source = dict((file_name,file_contents(file_name)) for file_name in text_files)

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("RESULT.CSV","w"))
for k, v in results.items():
	w.writerow([k,v])