import numpy as np
from pprint import pprint
from munkres import Munkres, print_matrix
import sys
from pprint import pprint
import utils as utl
# def testMatrix():
# 	rows = np.random.randint(1,5)
# 	columns = np.random.randint(1,5)
# 	#creating matrix
# 	A =  np.random.randint(10,size=(rows,columns))
# 	pprint(A)

# def main():
# 	balanceMatrix()

# def balanceMatrix():
# 	print "balanceMatrix"
def assignment(S,events):
	A = create_profit(S,events)
	pprint(A)
	assign(A)
'''	matrix = [[ 4, 8, 7, 9, 5],
			[ 33, 5, 8, 14, 9],
			[ 6, 6, 3, 5, 7],
			[ 9, 3, 12, 4, 5]]
	matrix = [[1, 0, 0, 4, 5, 1, 0, 5, 8, 6, 7, 8],
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			 [8, 12, 9, 1, 6, 7, 1, 0, 4, 2, 10, 6],
			 [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0]]'''


	
	

def create_profit(S,events):
	A = []
	for e_id in range(utl.Event_num):
		print e_id
		#create a row of timeslots for this event
		times =  utl.d_count*utl.t_count
		A.append( [0]*times )
		for i in range(times):
			profit = getProfit(events[str(e_id)], i, S)
			A[e_id][i] = int(profit)+1

	return A


def getProfit(event, time, S):
	increase = 0
	day = time / utl.t_count  # get day
	slot = time % utl.t_count # get slot

	for user_id in event['invited']:
		user_weight = S[user_id][day][slot]
		increase += 0 if user_weight > event['weight'] else event['weight'] - user_weight # add 0 if user_weight > event_weight otherwise, add event_weight - user_weight

	return increase


def test():
	matrix = [[5, 9, 1],
	          [10, 3, 2],
	          [8, 7, 4],
	          [5, 6, 3],
	          [5, 6, 7]]


	assign(matrix)

def assign( matrix ):

	cost_matrix = []
	for row in matrix:
	    cost_row = []
	    for col in row:
	        cost_row += [sys.maxint - col]
	    cost_matrix += [cost_row]

	m = Munkres()
	indexes = m.compute(cost_matrix)
	print_matrix(matrix, msg='Lowest cost through this matrix:')
	total = 0
	for row, column in indexes:
	    value = matrix[row][column]
	    total += value
	    print '(%d, %d) -> %d' % (row, column, value)

	print 'total profit=%d' % total


if __name__ == '__main__':
	test()