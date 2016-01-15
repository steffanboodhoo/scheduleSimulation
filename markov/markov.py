'''
A schedule s has d days which has T timeslots, all s timeslots are contained in S
This is represented by a 2d numpy Array dim_0 = s, dim_1 = d, dim_2 = t

Process:
Generating states for each timeslot
define an initial probility state vector [x1, x2, x3]
define 
States are generated using markov.py, 
then the 
'''

import utils as utl 
from pprint import pprint
import numpy as np
from random import randint, random
import gen as g

def init(s_count, d_count, t_count):
	S = {}
	for i in range(s_count):
		S[str(i)] = np.zeros( (d_count,t_count) ) 
	
	S = generateStates( S, s_count, d_count, t_count)
	S = generateWeights(S, s_count, d_count, t_count)
	return S

def generateStates( S, s_count, d_count, t_count):
	count = 0
	for s in S:
		for d in range(d_count): # a new day
			t = 0
			S[s][d][t] = getInitialState()	
			t += 1
			while t < t_count:
				S[s][d][t] = nextState(S[s][d][t-1])
				t+=1
	return S

def generateWeights(S, s_count, d_count, t_count):
	return g.gen(S, utl.gen_method_1, s_count, d_count, t_count)

def getInitialState():
	t_0 = random()
	if t_0 <= utl.initial_distro[0]:
		return 0
	if t_0 <= ( utl.initial_distro[0] + utl.initial_distro[1] ):
		return 1
	else:
		return 2

def nextState(c_state):
	c_state = int(c_state)
	trans = utl.trans_mat[c_state]
	t = random()
	if t <= trans[0]:
		return 0
	if t <= ( trans[0] + trans[1] ):
		return 1
	else:
		return 2


if __name__ == '__main__':
	S = init( 3, 3, 3)
	print S