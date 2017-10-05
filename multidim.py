import numpy as np
import matplotlib.pylab as plt
from random import randint
import copy

rules = [i for i in range(0,256)]
rule_matrix = list()
for rule in rules:
	#temp = []
	r = bin(rule)[2:]
	if len(r)<8:
		r = '0'*(8-len(r)) + r
	
	rvec = list(r)
	rvec = rvec[::-1]
	rule_matrix.append(rvec)

#print(rule_matrix)

def op(left,mid,right,rule):
	chosen_str = left + mid + right
	#print(chosen_str)
	chosen_val = int(chosen_str,2)
	val = rule_matrix[rule][chosen_val]
	return val


entrant_col = list()
mat = list()
entrant1 = list()
# entrants = [0,0,0,0,0,0,0,0,0,0]
# for i in range(9):
# 	mat.append(entrants)
for i in range(999):
	entrant_col.append(randint(0,1))
for i in range(1000):
	entrant1.append(randint(0,1))
mat.append(entrant1)
for i in range(999):
	temp = []
	temp.append(entrant_col[i])
	for j in range(999):
		temp.append(0)
	mat.append(temp)
tv= copy.deepcopy(mat)
mat_rev = copy.deepcopy(mat)


#print(len(mat))
for rls in range(31,256):
	mat = copy.deepcopy(tv)
	mat_rev = copy.deepcopy(tv)
	for i in range (1,1000):
		for j in range (1,1000):
			mat[i][j] = op(str(mat[i][j-1]),str(mat[i-1][j-1]),str(mat[i-1][j]),rls)
			mat_rev[i][j] = op(str(mat[i-1][j]),str(mat[i-1][j-1]),str(mat[i][j-1]),rls)
	mat2 = []
	for row in mat:
		k = []
		for i in row:
			k.append(float(i))
		mat2.append(k)

	mat3 = []
	for row in mat_rev:
		k = []
		for i in row:
			k.append(float(i))
		mat3.append(k)

	npmatrix1 = np.matrix(mat2)

	npmatrix2 = np.matrix(mat3)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.set_aspect('equal')
	plt.imshow(npmatrix1, interpolation='nearest', cmap=plt.cm.binary, aspect = 'auto')
	plt.colorbar()
	#plt.show()
	plt.savefig('./newtest5/test'+str(rls)+'.png')
	plt.imshow(npmatrix2, interpolation='nearest', cmap=plt.cm.binary, aspect = 'auto')
	plt.close()
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.set_aspect('equal')
	plt.imshow(npmatrix2, interpolation='nearest', cmap=plt.cm.binary, aspect = 'auto')
	plt.colorbar()
	plt.savefig('./newtest5/test'+str(rls)+'-rev.png')
	plt.close()