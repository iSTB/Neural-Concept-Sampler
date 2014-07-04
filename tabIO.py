


class tabIO(object):
	#For reading/writing and  encoding/decoding drum beats
	
	def __init__(self):
		pass

	def read(self,path_to_file):
		#takes drum beats and returns [{}]
		
		self.beats = []

		with open(path_to_file) as f:
			self.content = f.readlines()
			self.instruments = self.content[0][:-1].split(',')
			self.patterns = [pattern[:-1].split(',') for pattern in self.content[1:] if pattern != '']
	     				
		
		for pattern in self.patterns:
			data = {}
			for (line,inst) in zip(pattern,self.instruments):
				data[inst] = line

			self.beats.append(data)


		return self.beats

	def encode(self,beat):
		pattern = [item for sublist in beat.values() for item in sublist]
		return [0 if x == '-' else 1 for x in pattern]
		
	
	def toDrumTab(self,pattern):
		return ['x' if p == 1  else '-' for p in pattern]
		
	def decode(self,pattern,bar_length = 16):
		split = [''.join(self.toDrumTab(pattern[i:i+bar_length])) for i in range(0,len(pattern),bar_length )]
		musak = {}

		c = 0
		for inst in self.instruments:
			musak[inst] = split[c]
			c +=1

		return musak 	
	
		
'''
reader = tabIO()

beats = reader.read('beats/beats.csv')
pattern = reader.encode(beats[0])
print reader.decode(pattern)
'''
