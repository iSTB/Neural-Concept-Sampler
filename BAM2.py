class CL_BAM(object):
	def __init__(self):
		self.context = {}
		self.weights = []

	
	def add_item(self,(obj,features)):
		self.context[obj] = features		

	
	def make_weights(self):
		if self.context == {}:
			raise RuntimeError('The Context is yet to be defined')
		objects = self.context.keys()
		print objects
		self.n_objects = len(objects)
		self.n_features = len(self.context[objects[0]])
		q = max(self.n_objects, self.n_features) + 1	
	

		for obj in objects:
			ws =[1 if feature == 1 else -q for feature in self.context[obj]]
			self.weights.append(ws)

		print self.weights


	def feedforward(self,feature_pattern):

		obj_activitys = [0]*self.n_objects
		for row_n in range(len(self.weights)):
			activity = sum([weight*feature for weight,feature in zip(self.weights[row_n], feature_pattern)])
			obj_activitys[row_n] += activity

		print obj_activitys					
		objs_firing = [1 if activity > -0.5 else 0 for activity in obj_activitys]
		return objs_firing 

	def feedback(self,object_pattern):
		feature_activitys = [0] * self.n_features
		for i in range(len(object_pattern)):
			if object_pattern[i] == 1:
				for j in range(self.n_features):
					feature_activitys[j] += self.weights[i][j]
		
		print feature_activitys 
		features_firing = [1 if activity >-0.5 else 0 for activity in feature_activitys]
		return features_firing 
				

	def getConcept(self, input_pattern):

		if self.weights == {}:
			raise RuntimeError('Weight Matrix not created use makeWeight()')
		objects = self.feedforward(input_pattern) 	
		features = self.feedback(objects)
		return (objects,features)

o = CL_BAM()

o.add_item(['a',[0,0,0,1]])

o.make_weights()


print o.getConcept([0,0,0,1])

'''
os = o.feedforward([0,0,0,1])
print o.feedback(os)
'''


