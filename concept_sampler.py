import drumMachine
import BAM
import tabIO

reader = tabIO.tabIO()
beats  = reader.read('beats/beats.csv')

bam = BAM.CL_BAM()
dm = drumMachine.drumMachine()

print beats
c = 0
for beat in beats: 
	pattern =reader.encode(beat) 
	bam.add_item([c,pattern])	
	c +=1

bam.make_weights()

input_beat = {'hhc': '----------------', 'snare': '----------------', 'kick': 'x-x-------------'}

concept_pattern =  bam.getConcept(reader.encode(input_beat))

dm.patterns = reader.decode(concept_pattern[1])
print dm.patterns
dm.play(2)


  




