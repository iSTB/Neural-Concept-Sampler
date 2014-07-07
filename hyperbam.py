import numpy
from BAM import CL_BAM




class HyperBam(object):

	def __init__(self, n):
		self.n_layers = n
		self.layers = []
		for layer in self.n_layers:	
			l = CL_BAM()
			self.layers.append(l)


	def __str__(self):
		

	def add_item(self,obj,features,layer):
		if layer < 0 or layer >= self.n_layers:
			raise RuntimeError('Layer does not exist, only %d layers in hyperbam' % self.n_layers)
		self.layers[layer].add_item((obj,features))

	def lineUP(self):
		pass	
	def make_weights(self):
		#Check if layers line up

	
