import numpy as numpy
from random import randint

rlist = []
for rule in range(0,256):
	l = bin(rule)[2:]
	dif = 8 - len(l)
	pad = '0'*dif
	l = pad + l
	l = l[::-1] #reverse
	rlist.append(l)

#print(rlist[119])
input_stream = '1011101000000100101111101001111100011101'
input_stream = '010010000110001110000110110111100101100111'
input_stream = '1011101000000100101111101001111100011101'
input_stream = '10111010000001001011111010011111000111010111111110010101011101000101100111110111'
#input_stream = '0101000001101000011011110110111001100101'
ln = len(input_stream)
input_list = list(input_stream)
# for i in range(0, ln, 8):
# 	print(input_list[i:i+8])
input_list = [int(i) for i in input_list]
output_list = input_list[:]

key = '1011000000111010'
keygen = list(key)
keygen = [int(i) for i in keygen]

mat = []
mat.append(keygen)

tiv = []
tiv = keygen


for it in range(0,len(input_list)):
	dummy = []
	for col in range(0, len(keygen)):
		if(col == 0):
			lel = tiv[-1]
			mel = tiv[0]
			rel = tiv[1]
		elif(col == len(keygen)-1):
			lel = tiv[-2]
			mel = tiv[-1]
			rel = tiv [0]
		else:
			lel = tiv[col-1]
			mel = tiv[col]
			rel = tiv[col+1]
		state = str(lel) + str(mel) + str(rel)
		state_no = int(state,2)
		state_val = rlist[30][state_no]
		dummy.append(int(state_val))
	tiv = dummy[:]
	mat.append(dummy)
key1 = []
for i in range(len(output_list)):
	key1.append(mat[i][0])
	output_list[i] = input_list[i] ^ mat[i][0]

# print(mat)
# print(input_list)
# print(key1)
# print(output_list)


text = []
for i in range(0, ln, 8):
	block = output_list[i:i+8]
	block_str = ''.join([str(p) for p in block])
	block_no = int(block_str, 2)
	c = str(chr(block_no))
	text.append(c)
t = ''.join(text)
print(t)


