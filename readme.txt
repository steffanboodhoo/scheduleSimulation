Dependencies:
python - 2.7+
numpy - Installation Instructions http://www.numpy.org/

How to run:
python test.py

BASIC

Description:
The basic usage really occurs in three parts
1) Initialization of the schedules
2) Equalization of the schedules
3) Finding the best timeslot
all contained in basic()

Initialization of the schedules

init()
This function creates a two dimensional array S with dimension 1 (rows) being the schedule and
dimension 2 (columns) being the timeslots. Each timeslot is filled with a random float between 0 and 1, then these values 
are converted to match the range of the maximum and minimum weight range, wMax and wMin.


Equalization of the schedules

equalize_schedules(abstract_mu, S)
This function accepts the raw schedules, and an abstract mu. The function goes through all the schedules and finds the 
average constraint weight, it then uses the abstract mu and the average constraint weight to create a variable to scale 
all the weights of the current schedule.


Finding the best timeslot

find_bestT(S)
This function accepts the equalized or scaled schedules, it then goes through each time slot and 
sums the weights for all the scheules of the current timeslot. Each sum is compared and the smallest is recorded as well
as the timeslot(column index) which gave this result.

FEEDBACK

Description:
Starts off with basic but then modifies a randomly chosen timeslot and schedule. The modification is also random and follows the initialization method.
The algorithm then determines if the solution needs to be re-evaluated or not. If it does, then the solution is re-evaluated using the basic method.

CHANGING THE SIMULATION

Any changes to the simulation such as number of timeslots, number of schedules, number of times you would like a part of the simulation to run,
all these variables are contained within utils.py

tCount 			-			Number of timeslots in a schedule 
sCount 			-			Number of schedules in simulation
wMax 			-			Maximum Weight Constraint
wMin 			-			Minimum Weight Constraint

basicSimulation 		-	Number of times you want to run the basic simulation
feedbackSimulation		- 	Number of times you want to run the feedback simulation
modifications = 10		-	Number of times you want to modify the schedules in ONE feedback simulation
