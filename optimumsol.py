import utils as utl
from pprint import pprint
import copy
event_perms = []
combs = []
data = [0] * utl.Event_num

def globalOptimum(S, events):
	event_ids = events.keys()
	# pprint(event_ids)
	slots = range(0,utl.d_count*utl.t_count)
	# pprint(slots)
	comb(slots, 0, 0)
	permutations(0,event_ids)
	optimal = findOptimal(event_perms, combs, S, events)
	print 'optimal solution'
	pprint(optimal)
	# pprint(event_perms)
	# pprint(combs)

def permutations(i,event_ids):
	if(i == utl.Event_num-1):
		event_perms.append(event_ids[:])

	for j in range(i, utl.Event_num):
		swap(event_ids, i, j)
		permutations(i+1, event_ids)
		swap(event_ids, i, j)

def swap(event_ids, i, j):
	temp = event_ids[i]
	event_ids[i] = event_ids[j]
	event_ids[j] = temp

def comb(slots, start, index):
	if(index == utl.Event_num):
		combs.append(data[:])
		return

	for i in range(start,len(slots)):
		data[index] = slots[i]
		comb(slots, i+1, index+1)
''' USING MULTIPLE DAYS
def findOptimal(event_perms, time_combs, S, events):
	for slot_combination in time_combs:	#each slot combination 
		
		for event_permutation in event_perms:#try ALL event permutations in current slot combination

			S_copy = copy.deepcopy(S) #create a copy for this particular combination of time slots and this permutation of events
			
			for i in range(utl.Event_num):#for each event
				
				time = slot_combination[i] # get the day/slot for the ith event for this particular combination
				day =  time / utl.t_count
				slot = time % utl.t_count
				
				event_id = event_permutation[i]#get the ith event for this particular permutation
				event = events[event_id]
				
				for user_id in event['invited']:#for each user invited to the current event 
					if(S_copy[user_id][day][slot] < event['weight']):
						S_copy[user_id][day][slot] = event['weight']

			getStatistics(S_copy)
		#End Of Permutations
	#End Of Combinations
'''

#USING ONE DAY
def findOptimal(event_perms, time_combs, S, events):
	optimal = None
	for slot_combination in time_combs:	#each slot combination 
		
		for event_permutation in event_perms:#try ALL event permutations in current slot combination

			S_copy = copy.deepcopy(S) #create a copy for this particular combination of time slots and this permutation of events
			
			for i in range(utl.Event_num):#for each event
				
				time = slot_combination[i] # get the day/slot for the ith event for this particular combination
				day =  0 #time / utl.t_count
				slot = time #time % utl.t_count
				
				event_id = event_permutation[i]#get the ith event for this particular permutation
				event = events[event_id]
				
				for user_id in event['invited']:#for each user invited to the current event 
					if(S_copy[user_id][day][slot] < event['weight']):
						S_copy[user_id][day][slot] = event['weight']

			instance = getStatistics(S_copy)
			if(optimal is None):
				optimal = instance
			elif instance[0]>optimal[0]:
				optimal = instance

		#End Of Permutations
	#End Of Combinations
	return optimal


def getStatistics(S):
	average_schedule_sum = 0
	timeslot_avg = 0

	for user_id in S: #for each user
		temp_sum = sum(sum(S[user_id]))
		average_schedule_sum = temp_sum
		timeslot_avg += temp_sum/(utl.d_count * utl.s_count)


	average_schedule_sum = average_schedule_sum / len(S)
	timeslot_avg = timeslot_avg / len(S)
	return_obj = [average_schedule_sum, timeslot_avg]

	return return_obj

if __name__ == '__main__':
	globalOptimum()