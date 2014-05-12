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


org_beat = reader.encode({'hhc': '----------------', 'snare': '---x------------', 'kick': '----------------'})
input_beat = org_beat 



#Adding intitial Context
c = 0
for beat in beats: 
	pattern =reader.encode(beat) 
	bam.add_item([c,pattern])	
	c +=1

bam.make_weights()
for i in range(100):
	

	bam.make_weights()
	concept_pattern =  bam.getConcept(input_beat)	
	activitys = concept_pattern[2]

	print "Concept:" + str(reader.decode(concept_pattern[1]))    

	nu = bam.n_objects+1

	p = 0.2 
	#print p 
	toPlay = []


	

	max_ = max(activitys)*1.0
	min_ = min(activitys)*1.0

	for act in activitys:
		
		prob = (act - min_)/(max_-min_) 
		

		if prob >= random.uniform(0.0,1.0):
			toPlay.append(1)
		else: toPlay.append(0)

	dm.patterns = reader.decode(toPlay)
	print "ing example of concept" + str(i)
	print "playing beat: " + str(dm.patterns)
	dm.play(1)
	#input_beat = toPlay

	bam.add_item([c,toPlay])  
	c +=1



