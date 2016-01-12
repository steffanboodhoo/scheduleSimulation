from markov import markov as mkv
import numpy as np
import utils as utl

def init():
	return init_mkv()

#initialize arrays to random values indicate the weighted constraints of each hour
def init_mkv(): 
	S = mkv.init(utl.s_count, utl.d_count, utl.t_count)
	return S