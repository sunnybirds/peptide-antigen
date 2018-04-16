# import numpy as np
aai = {}
aas = "ACDEFGHIKLMNPQRSTVWY"
aa2ary = {}
values = [5.5,5.4,5.3,5.2,5.1,5.0,4.9,4.8,4.7,4.6,4.5,4.4,4.3,4.2,4.1,4.0,3.9,3.8,3.7,3.6,3.5,3.4,3.3,3.2,3.1,3.0,2.9,2.8,2.7,2.6,2.5,2.4,2.3,2.2,2.1,2.0,1.9,1.8,1.7,1.6,1.5,1.4,1.3,1.2,1.1,1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0,-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,-1.2,-1.3]


i = 0
for aa in list(aas):
	aai[aa] = i
	i = i+1
ori = ['0'] * 20
val = ['0'] * len(values)
aa2ary[" "] = ori
for aa in list(aas):
	tmp = ori[:]
	tmp[aai[aa]] = '1'
	# print(tmp)
	aa2ary[aa] = tmp

def retI(v):
	for i in range(len(values)):
		if float(v) == values[i]:
			t = val[:]
			t[i] = '1'
			return t

fh = open("peptides.txt")
fo = open("antigen-score.txt", "w")
for ln in fh.readlines():
	ln = ln.strip()
	data = ln.split("\t")
	tmp = []
	seq = list(data[0])
	if len(seq)<30:
		seq = seq + [" "] * (30-len(seq))
	for aa in seq:
		tmp = tmp + aa2ary[aa]
	# print(retI(data[1]))
	tmp += retI(data[1])
	fo.write(",".join(tmp) + "\n");
fo.close()


