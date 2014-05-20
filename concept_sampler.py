import drumMachine
import BAM
import tabIO
import math
import random

def sigmoid(x,nu):
	
	return 1/(1+math.exp(-nu*x))	
	
reader = tabIO.tabIO()
beats  = reader.read('beats/beats.csv')

bam = BAM.CL_BAM()
dm = drumMachine.drumMachine()


org_beat = reader.encode({'hhc': '----------------', 'snare': '----------------', 'kick': '----------------'})
input_beat = org_beat[:] 


#Adding intitial Context
c = 0
for beat in beats: 
	pattern =reader.encode(beat) 
	bam.add_item([c,pattern])	
	c +=1

bam.make_weights()


noise = 0.015
p = 1.0/len(input_beat)
for i in range(1000):
	

	bam.make_weights()
	concept_pattern =  bam.getConcept(input_beat)	
	activitys = concept_pattern[2]
	#print concept_pattern
	print "Concept:" + str(reader.decode(concept_pattern[1]))    
	#print p 
	toPlay = []


	

	max_ = max(activitys)*1.0
	min_ = min(activitys)*1.0

	probs = []
	for act in activitys:
		if max_ - min_ == 0:
			prob = 1

		else:	
			prob = (act - min_)/(max_-min_) 
		'''
		if prob >= 90:
			prob -= abs(random.gauss(0,noise))*1.5	
		
		elif prob <= 0:
			prob += abs(random.gauss(0,noise))		

		else:
			prob += random.gauss(0,noise)		
		'''
		probs.append(prob)
		if prob >= random.uniform(0.0,1.0):
			toPlay.append(1)
		else: toPlay.append(0)



#	print "Probabilitys: " +str(probs)
	dm.patterns = reader.decode(toPlay)
	print "Playing:" + str(dm.patterns)
	dm.play(1)





		


	bam.add_item([c,toPlay])  
	c +=1



