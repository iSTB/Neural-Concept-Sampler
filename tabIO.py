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


		

		
#reader = tabIO()

#reader.read('beats/beats.csv')

#reader.read()

