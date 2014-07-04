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



last_played = input_beat
for i in range(1000):
	
	bam.make_weights()
	concept_pattern =  bam.getConcept(input_beat)	


	toPlay = concept_pattern[1]

	dm.patterns = reader.decode(toPlay)


	print "size of context: " + str (len(concept_pattern[0]))
	
	print "concept:" + str(reader.decode(concept_pattern[2]))
	print "Playing:" + str(dm.patterns)
	dm.play(1)

	

	bam.add_item([c,toPlay])  
	c +=1

	
	#input_beat = toPlay#concept_pattern[2] 

	#input_beat =concept_pattern[2] 
	

