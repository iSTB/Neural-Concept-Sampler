__author__ = "Jack Fletcher"
__copyright__ = "Copyright 2014, Plymouth University "
__credits__ = ["Thomas Wennekers",  "Radim Belohlavek"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jack Fletcher"
__email__ = "jack.mckayfletcher@plymouth.ac.uk"
__status__ = "Production"

import random
import pylab

class CL_BAM(object):
	def __init__(self):
		self.context = {}
		self.weights = []

	
	def add_item(self,(obj,features)):
		if features not in self.context.values():
			self.context[obj] = features

		else: print "Already in conxtext"		
	
	def make_weights(self):
		self.weights = []
		if self.context == {}:
			raise RuntimeError('The Context is yet to be defined')
		objects = self.context.keys()
		#print objects
		self.n_objects = len(objects)
		self.n_features = len(self.context[objects[0]])
 
		self.q = max(self.n_objects, self.n_features)*1.0 +1 	

		for obj in objects:
			ws =[1 if feature == 1 else -self.q for feature in self.context[obj]]
			self.weights.append(ws)

		#print self.weights

	def feedforward(self,feature_pattern):

		obj_activitys = [0]*self.n_objects
		for row_n in range(len(self.weights)):
			activity = sum([weight*feature for weight,feature in zip(self.weights[row_n], feature_pattern)])
			obj_activitys[row_n] += activity

		max_ = max(obj_activitys)*1.0 #+self.n_objects +1
		min_ = min(obj_activitys)*1.0 



		if max_ == min_:
			objs_firing = [1 if x >= -0.5 else 0 for x in obj_activitys]
			print "here!"



		else:

			obj_probs = [(act-min_)/(max_-min_) for act in obj_activitys]

			objs_firing = [1 if random.uniform(0,1) <= prob else 0 for prob in obj_probs]
			print "objects probs:" + str(obj_probs) 

			
		objs_firing = [1 if x >= -0.5 else 0 for x in obj_activitys]



		return objs_firing


	def feedback(self,object_pattern):
		feature_activitys = [0] * self.n_features
		for i in range(len(object_pattern)):
			if object_pattern[i] == 1:
				for j in range(self.n_features):
					feature_activitys[j] += self.weights[i][j]
		
		max_ = max(feature_activitys)*1.0
		min_ = min(feature_activitys)*1.0 


		
		concept = [1 if x >= -0.5 else 0 for x in feature_activitys]

		if max_ == min_:
			features_firing = concept
		
		else:
			feature_probs = [(act-min_)/(max_ - min_) for act in feature_activitys]
			features_firing = [1 if random.uniform(0,1) <= prob else 0 for prob in feature_probs]


		return (features_firing, concept)
				

	def getConcept(self, input_pattern):

		if self.weights == {}:
			raise RuntimeError('Weight Matrix not created use makeWeight()')
		objects = self.feedforward(input_pattern) 	
		features = self.feedback(objects)
		return (objects,features[0],features[1])





o = CL_BAM()
o.add_item(['a',[0,0,0,1]])
o.add_item(['b',[1,0,1,1]])

o.make_weights()

print o.getConcept([0,0,0,1])


