from BAM import CL_BAM




class HyperBam(object):

	def __init__(self, n):
		self.n_layers = n
		self.layers = []
		for layer in range(self.n_layers):	
			l = CL_BAM()
			self.layers.append(l)


		

	def add_item(self,obj,features,layer):
		if layer < 0 or layer >= self.n_layers:
			raise RuntimeError('Layer does not exist, only %d layers in hyperbam' % self.n_layers)
		self.layers[layer].add_item((obj,features))

	def lineUp(self):
		notInLine = None
		for i,cur in enumerate(layers):
			prev = layers[i-1]
			len_top = len(prev.context.keys())
			len_bot = len(cur.context.values[0])
			if len_top != len_bot:
				notInLine = (i-1,i)
				break
		return b

	def make_weights(self):
		#Check if layers line up
		notInLine = self.lineUp()
		if layers != None:
			raise RuntimeError('Layers %d and %d do not Line up' % notInLine[0], notInLine[1])



h = HyperBam(2)
h.add_item('a',[0,0,0],0)
h.add_item('t',[1,2,3],1)
h.add_item('j',[1,2,4],1)
