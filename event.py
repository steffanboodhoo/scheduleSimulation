def addToEvents(Events, day, hour, weight, participants):
	if not(day in Events):
		Events[day]={}
	Events[day][hour] = {'weight':weight,'participants':participants}

def checkForMeeting(Events, day, hour):
	if day in Events and hour in Events[day]:
		return True
	return False

def selectParticipants(n,S):
	participants = []
	indicies = []
	for i in range(n):
		indicies.append( randint(0 , utl.s_count -1 ) ) 
		p = S[ indicies[i] ]
		participants.append( p )

	return [indicies, participants]