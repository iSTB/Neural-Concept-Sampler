import tabIO
import drumMachine


reader = tabIO.tabIO()
data = reader.read('beats/beats.csv')
print data
def encodeBeat(beat):
	print beat
	pattern = [item for sublist in beat.values() for item in sublist]
	return [0 if x == '-' else 1 for x in pattern]

def toDT(xs):
	return ['x' if x == 1 else '-' for x in xs]

def decode(pattern):
	n = 16
	split = [''.join(toDT(pattern[i:i+n])) for i in range(0,len(pattern),n)]
	
	return {'hhc':split[0], 'snare':split[1], 'kick':split[2]}


		



#############Making wegiht Matrix######################
barlength =  len(data[0][data[0].keys()[0]])
n_output_nodes = len(data)
n_input_nodes = barlength*len(data[0])
 

q = max(n_output_nodes,n_input_nodes) + 1

weight_matrix = [[0]*n_input_nodes for _ in range(n_output_nodes)]



########Making Context#################################
context = []
c = 0
for beat in data:
	context.append((c, encodeBeat(beat)))
	c +=1
#####Training weight Matrix##############
for (groove,beats) in context:
	for i in range(len(beats)):
		if beats[i] == 1:
			weight_matrix[groove][i] = 1

		else:
			weight_matrix[groove][i] = -q



def getConcept(pattern):
	patternE = encodeBeat(pattern)
	forward = []
	raw_f = []

	back = [0]*n_input_nodes	
	for groove in weight_matrix:
		activity = sum([g*p for g,p in zip(groove,patternE)])				
		
		raw_f.append(activity)


		if activity > -0.5:
			forward.append(1)

		else:
			forward.append(0)	


	print forward

	for i in range(len(forward)):
		if forward[i] == 1:
			for j in range(len(back)):
				back[j] += weight_matrix[i][j]
	#print raw_f
	print back

	for i in range(len(back)):
		if back[i] > -0.5:
			back[i] = 1
		else: back[i] = 0




	return back


toPlay = getConcept({'hhc':"xxxxxxxxxxxxxxxx",'snare':"xxxxxxxxxxxxxxxx",'kick':"xxxxxxxxxxxxxxxx"})
dm = drumMachine.drumMachine()
dm.patterns = decode(toPlay)

print dm.patterns

dm.play()
