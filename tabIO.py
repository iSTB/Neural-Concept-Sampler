class tabIO(object):

	def __init__(self):
		pass

	def read(self,path_to_file):
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

	def encodeBeat(self,beat):
		pattern = [item for sublsit in beat.values() for item in sublist]
		return [0 if x == '-' else 1 for x in pattern]
		
	
	def toDrumTab(self,pattern):
		return ['x' if p == 1 else '-' for p in pattern]
		
	def decode(pattern,bar_length = 16):
		split = [''.join(toDT(pattern[i:i+bar_length])) for i in range(0,len(pattern),n)]
		musak = {}

		c = 0
		for inst in self.instruments:
			beat[inst] = split[c]
			c +=1

		return musak 	
	
		
#reader = tabIO()

#reader.read('beats/beats.csv')

#reader.read()

