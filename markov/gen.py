'''
METHOD 1
Generate within a range for each state
i.e. state 0 has a particular range e.g. 0 - 2, state 1 : 3 - 7, state 2: 8 - 10

METHOD 2
Assign larger ranges so specific numbers per range
e.g. state 0, 1 : .2, 2 : .2, 
'''
from random import randint, random
import utils as utl 
import numpy as np

def gen(S, method, s_count, d_count, t_count):
	for s in range(s_count):
		for d in range(d_count):
			for t in range(t_count):
				state = S[s][d][t]
				if method == utl.gen_method_1:
					S[s][d][t] = method_1(state)
				# else:
				# 	S[s][d][t] = method2(S[s][d][t]) 
				# print S[s][d][t]
	return S

#0-2,3-7,8-10
def method_1(state):
	l_0 = 0
	h_0 = 2
	l_1 = 3
	h_1 = 7
	l_2 = 8
	h_2 = 10
	if state == 0 :
		return random()*( h_0 - l_0 ) + l_0
	if state == 1 :
		return random()*( h_1 - l_1 ) + l_1
	if state == 2 :
		return random()*( h_2 - l_2 ) + l_2
	print 'nothing worked'

def method2(state):
	s_0 = [0.233, 0.233, 0.233, 0.05, 0.05, 0.04, 0.04, 0.031, 0.03, 0.03, 0.03]
	s_1 = [0.025, 0.025, 0.05, 0.16, 0.16, 0.16, 0.16, 0.16, 0.05, 0.025, 0.025]
	s_2	= [0.03, 0.03, 0.03, 0.031, 0.04, 0.04, 0.05, 0.05, 0.233, 0.233, 0.233]
	
	if state == 0 :
		state_dist = s_0
	elif state == 1 :
		state_dist = s_1
	elif state == 2 :
		state_dist = s_2

	
	partition = state_dist[0]
	i = 1
	k = random()
	while k <= partition:
		partition += partition[i]
		i += 1

	return i


