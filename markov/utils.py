
wMax = 10
wMin = 0

basicSimulation = 10
modifications = 10
feedbackSimulation = 10
runBasic = False
runFeedBack = True


initial_distro = [0.4,0.2,0.4]

#0 free
#1 scheduled but able to preempt
#2 definitely busy
trans_mat =[
	 [0.69,0.27,0.04],
	 [0.27,0.52,0.21],
	 [0.15,0.18,0.67]]

gen_method_1 = 1
gen_method_2 = 2