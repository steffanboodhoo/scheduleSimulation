import utils as utl
from random import randint, random
from pprint import pprint
import numpy as np

def selectParticipants(n,S):
	participants = []
	user_ids = []
	i = 0 
	while i<n:
		u_id = str(randint(0 , utl.s_count -1 ))
		if not (u_id in user_ids):
			user_ids.append(u_id)
			p = S[ u_id ]
			participants.append( p )
			i+=1

	return [user_ids, participants]

#scale weights according to their average constraint weight so it becomes abstract_mu
def equalize_schedules(abstract_mu, S):
	#s is an index representing a schedule in S
	for s in range(len(S)):
		#find the average constraint weight
		mu_s = np.sum(S[s]) / (utl.t_count * utl.d_count)

		#create value to scale each weight 
		scale = abstract_mu / mu_s

		#scale weight
		S[s] = S[s] * scale
	#return the equalized schedules
	return S


def createEvent(S,mapp,e_id):
	event = {'members':[]}

	#randomly select participants from S
	[user_ids, participants] = selectParticipants(2,S)
	
	#equalize schedules
	S_p = equalize_schedules(3,np.copy(participants))
	
	#find the best day, timeslot
	[day, slot] = find_bestT(S_p)
	
	#make the event official
	event['day'] = day
	event['slot'] = slot
	# event['weight'] = random()*(utl.wMax - utl.wMin) + utl.wMin
	event['weight'] = randint(0, utl.wMax)
	event['invited'] = user_ids

	return event


def generateEvents(S,mapp):
	Events = {}

	for i in range(utl.Event_num):#number of events being created
		Events[str(i)] = createEvent(S,mapp,str(i))
	
	return Events

def placeEvents(S,events,mapp):
	for e_id in events:
		event = events[e_id]
		user_ids = event['invited']
		for user_id in user_ids:
			if( event['weight'] > S[user_id][day][slot] ):
			 	event['members'].append({ user_id : S[user_id][day][slot] })
				#PREVIOUSLY:generate a weight between the user's current weight and the maximum weight for the carded event # S[user_id][day][slot] = random()*( utl.wMax - S[user_id][day][slot] ) + S[user_id][day][slot]
		 		#NOW use 1 weight for all users
		 		S[user_id][day][slot] = event['weight']
		 		mapp[user_id].append(e_id)
		 	else:
		 		print "did not take it"


#find the Tbest given the equalized schedules
def find_bestT(S):	
	dBest = 0
	tBest = 0
	tVal = utl.wMax * utl.t_count

	#for every day d in the schedule
	for d in range(utl.d_count):
		#for every time slot, t, in a day
		for t in range(utl.t_count):
			constraint_t = 0
			#for every schedule s
			for s in range( len(S) ):
				#sum all the constraints at time t
				constraint_t += S[s][d][t] 

			#if the sum of constraints violated is less than the currrent smallest
			if( constraint_t < tVal ):
				tVal = constraint_t #make current best
				tBest = t           #save the best timeslot index
				dBest = d

	return [dBest, tBest]
	