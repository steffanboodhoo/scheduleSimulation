import numpy as np
import utils as utl
from random import randint, random
from markov import markov as mkv

def simulate():
	feedback()
	# basic()
	# if(utl.runBasic)
	# 	for i in range(utl.basicSimulation):
	# 		basic()
	# if(utl.runFeedback)
	# 	for i in range(utl.feedbackSimulation):
	# 		feedback()


def basic():
	#initialization
	S = init()
	print S #uncomment to view initial schedules
	best = find_bestT(S)
	print 'Normal best day and time :',best
	#changing the weights of the schedules to give equal influence
	S_p = equalize_schedules(3,np.copy(S))
	print S_p #uncomment to view equalized schedules
	best = find_bestT(S_p)
	print 'Equalized best day and time :',best
	print '-------------------------------------------'
	

#initialize arrays to random values indicate the weighted constraints of each hour
def init(): 
	S = mkv.init(utl.s_count, utl.d_count, utl.t_count)
	return S

#scale weights according to their average constraint weight so it becomes abstract_mu
def equalize_schedules(abstract_mu, S):
	#s is an index representing a schedule in S
	for s in range(utl.s_count):
		#find the average constraint weight
		mu_s = np.sum(S[s]) / (utl.t_count * utl.d_count)

		#create value to scale each weight 
		scale = abstract_mu / mu_s

		#scale weight
		S[s] = S[s] * scale
	#return the equalized schedules
	return S

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
			for s in range(utl.s_count):
				#sum all the constraints at time t
				constraint_t += S[s][d][t] 

			#if the sum of constraints violated is less than the currrent smallest
			if( constraint_t < tVal ):
				tVal = constraint_t #make current best
				tBest = t           #save the best timeslot index
				dBest = d

	return [dBest, tBest]

# def actualCost(t, S):
# 	cost = 0
# 	for s in range(s_count):
# 		cost += S[s][t]
# 	return cost
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

'''this uses the equalized arrays and does not bother to display mu's or matricies of the original 
as this is to purely observe the FEEDBACK functionality''' 
def feedback():
	#initialization
	S = init()
	S_p = equalize_schedules(3,np.copy(S))
	best = find_bestT(S_p)
	dBest = best[0]
	tBest = best[1]

	for i in range(utl.modifications):
		#random modifications and determining if we should consider changing our solution
		evaluate = timeSlotModification( dBest, tBest, S )
		if(evaluate):
			S_p = equalize_schedules(3,np.copy(S))
			best = find_bestT(S_p)
	
		print S
		print tBest
	
	print '-------------------------------------------'
	print tBest

#this randomly chooses both a schedule and a time-slot to modify 
def timeSlotModification(dBest, tBest, S):
	#random schedule selection
	sMod = randint( 0, utl.s_count - 1 )
	dMod = randint( 0, utl.d_count - 1 )
	tMod = randint( 0, utl.t_count - 1 )
	oldVal = S[sMod][dMod][tMod]
	newVal = S[sMod][dMod][tMod] = random()*(utl.wMax - utl.wMin) + utl.wMin 
	 
	
	#if the timeslot being modified tMod is tBest, and there is an increase in the constraint violation [weight goes up]
	if dBest == dMod and (tBest == tMod) and ((newVal - oldVal) > 0):
		#we need to re-evaluate our solution as an increase in tMod=tBest, means tBest may no longer be optimal
		return True

	#if the timeslot being modified tMod is not tBest, and there is an decrease in the constraint violation [weight goes down]
	if not(dBest == dMod and tBest == tMod) and ((newVal - oldVal) < 0):
		#we need to re-evaluate as a decrease in any other value other than tBest means that this value tMod can replace tBest
		return True		

	#anything else 
	return False #no re-evaluation needed

if __name__ == '__main__':
	simulate()