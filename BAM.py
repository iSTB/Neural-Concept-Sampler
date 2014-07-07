__author__ = "Jack Fletcher"
__copyright__ = "Copyright 2014, Plymouth University "
__credits__ = ["Thomas Wenneker",  "Radim Belohlavek"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jack Fletcher"
__email__ = "jack.mckayfletcher@plymouth.ac.uk"
__status__ = "Production"

class CL_BAM(object):
	def __init__(self):
		self.context = {}
		self.weights = []
	
	def __str__(self):
		return "BAM implmenting the formal concept %s" % self.context

	def add_item(self,(obj,features)):
		if features not in self.context.values():
			self.context[obj] = features
		else: print "%s, %s is already in conxtext and was not added" % (obj,features)
	def make_weights(self):
		self.weights = []
		if self.context == {}:
			raise RuntimeError('The Context is yet to be defined')
		objects = self.context.keys()
		self.n_objects = len(objects)
		self.n_features = len(self.context[objects[0]])
 
		q = max(self.n_objects, self.n_features) + 1	
	

		for obj in objects:
			ws =[1 if feature == 1 else -q for feature in self.context[obj]]
			self.weights.append(ws)

	def feedforward(self,feature_pattern):

		obj_activitys = [0]*self.n_objects
		for row_n in range(len(self.weights)):
			activity = sum([weight*feature for weight,feature in zip(self.weights[row_n], feature_pattern)])
			obj_activitys[row_n] += activity

		objs_firing = [1 if activity > -0.5 else 0 for activity in obj_activitys]
		return objs_firing 

	def feedback(self,object_pattern):
		feature_activitys = [0] * self.n_features
		for i in range(len(object_pattern)):
			if object_pattern[i] == 1:
				for j in range(self.n_features):
					feature_activitys[j] += self.weights[i][j]
		
		#print feature_activitys 
		features_firing = [1 if activity >-0.5 else 0 for activity in feature_activitys]
		return (features_firing, feature_activitys) 
				

	def getConcept(self, input_pattern):

		if self.weights == {}:
			raise RuntimeError('Weight Matrix not created use makeWeight()')
		objects = self.feedforward(input_pattern) 	
		features = self.feedback(objects)
		return (objects,features[0],features[1])




'''
o = CL_BAM()

o.add_item(['a',[0,0,0,1]])

o.make_weights()


print o.getConcept([0,0,0,1])


os = o.feedforward([0,0,0,1])
print o.feedback(os)
'''


