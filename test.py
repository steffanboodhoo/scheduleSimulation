import numpy as np
import utils as utl
import initialization as ini
import event as ev
from random import randint, random
from pprint import pprint

def simulate():
	basic()
	# if(utl.runBasic)
	# 	for i in range(utl.basicSimulation):
	# 		basic()
	# if(utl.runFeedback)
	# 	for i in range(utl.feedbackSimulation):
	# 		feedback()

def basic():
	#initialization
	S = ini.init()
	mapp = {} 
	#loop to create an event and do feedback
	pprint(S)
	events = ev.generateEvents(S,mapp)
	pprint(S)


def feedback(userId, day, slot, events, mapping):
	#get all events that this user belongs to
	events = mapping[userId]


def fix_weights(event, S, newDay, newSlot):
	members = event['members']
	for m in members:
		#revert the weight in the person's schedule to what it was before this was assigned
		S[m] [ event['day'] ] [ event['slot'] ] = members[m]

		#save the old weight of the new day / slot of user so we can revert if needed
		event['members'][m] = S[m] [newDay] [newSlot]

		#set weight at new day / time of event
		S[m] [newDay] [newSlot] = newWeight


	event['day'] = newDay
	event['slot'] = newSlot
	return event


def handleEvent(S, events, e_id, mapp):
	[nDay,nSlot] = find_best_time(S,events[e_id])
	#if a different day and timeslot is chosen
	if day != events[e_id]['day'] or slot != events[e_id]['slot']:
		#revert the weights of the people in the event at e['day'] and e['slot'] then set the new e['day'] and e['slot'] and change the weights of the persons accordingly
		fix_weights(event[e_id], S, nDay, nSlot)
		
		#since the weights of weights of all the members are changed all the events that these members belong too must be re-evaluated as well
		for m_id in events[e_id]['members']:
			for e_id in mapp[m_id]:
				if not e_id in queue:
					queue.append(e_id)

# def feedback():
# 	#initialization
# 	S = init()
# 	S_p = equalize_schedules(3,np.copy(S))
# 	best = find_bestT(S_p)
# 	dBest = best[0]
# 	tBest = best[1]

# 	for i in range(utl.modifications):
# 		#random modifications and determining if we should consider changing our solution
# 		evaluate = timeSlotModification( dBest, tBest, S )
# 		if(evaluate):
# 			S_p = equalize_schedules(3,np.copy(S))
# 			best = find_bestT(S_p)
# 			dBest = best[0]
# 			tBest = best[1]	
# 		print S
# 		print best
	
# 	print '-------------------------------------------'

# #this randomly chooses both a schedule and a time-slot to modify 
# def timeSlotModification(dBest, tBest, S):
# 	#random schedule selection
# 	sMod = randint( 0, utl.s_count - 1 )
# 	dMod = randint( 0, utl.d_count - 1 )
# 	tMod = randint( 0, utl.t_count - 1 )
# 	oldVal = S[sMod][dMod][tMod]
# 	newVal = S[sMod][dMod][tMod] = random()*(utl.wMax - utl.wMin) + utl.wMin 
	 
	
# 	#if the timeslot being modified tMod is tBest, and there is an increase in the constraint violation [weight goes up]
# 	if dBest == dMod and (tBest == tMod) and ((newVal - oldVal) > 0):
# 		#we need to re-evaluate our solution as an increase in tMod=tBest, means tBest may no longer be optimal
# 		return True

# 	#if the timeslot being modified tMod is not tBest, and there is an decrease in the constraint violation [weight goes down]
# 	if not(dBest == dMod and tBest == tMod) and ((newVal - oldVal) < 0):
# 		#we need to re-evaluate as a decrease in any other value other than tBest means that this value tMod can replace tBest
# 		return True		

# 	#anything else 
# 	return False #no re-evaluation needed

if __name__ == '__main__':
	basic()

'''
	Some change in day, hour occurs,
	we need to then re-evaluate ALL possible scheduled Events
		Upon evaluation if an event changes, i.e. the day and hour changes, we need to treat that as as another change in day, hour
'''

'''
n - number of people in a group
g - number of groups
s - the number of people that intersects
total = (n*g)-(n*s)

create total schedules
S[total]

start a create g groups
G[g]

s_index = 0
group_count = 0
for i = 0 to n*g
	s_index += 1
	if( s_index % n == 0 )
		s_index -= k
		

'''