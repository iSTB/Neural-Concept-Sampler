import pygame
import pyglet
from random import randint, uniform
import tabIO

class drumMachine(object):


	def __init__(self,bpm = 120, bar_length = 16):
	
		self.clock = pygame.time.Clock()
		pygame.init()
		self.set_bpm(bpm)


		self.bar_length = bar_length

		self.patterns = {}
		self.sounds = {}



		self.set_snare_sound()
		self.set_hhc_sound()
		self.set_kick_sound()


	def set_snare_sound(self,path_to_snare_sound='snare.wav',volume = 1):
		
		sound  = pyglet.resource.media(path_to_snare_sound, streaming=False).play()
		sound.volume = volume 
		self.sounds['snare'] = [sound,volume]


	def set_snare_pattern(self, pattern= "x-x-x-x-x-x-x-x-" ):
		self.snare_pattern = pattern
		self.patterns['snare'] = pattern
			
	def set_hhc_sound(self, path_to_hhc_sound='hhc.wav',volume = 1):
		sound = pyglet.resource.media(path_to_hhc_sound, streaming=False).play()

		sound.volume = volume
		self.sounds['hhc'] = [sound,volume]

	def set_hhc_pattern(self,pattern="x-x-x-x-x-x-x-x-"):
		self.hhc_pattern = pattern
		self.patterns['hhc'] = pattern

	def set_kick_pattern(self,pattern="x-x-x-x-x-x-x-x-"):
		self.kick_pattern = pattern
		self.patterns['kick'] = pattern
	
	def set_kick_sound(self, path_to_kick_sound= 'kick.wav',volume = 1):
		sound = pyglet.resource.media(path_to_kick_sound, streaming=False).play()
		sound.volume = volume
		self.sounds['kick'] = [sound,volume]
	

	def set_bpm(self,bpm):
		self.bpm = bpm
		self.fps = float(bpm*3.5)/60		


	def play(self,loops=-1):
		c = 0
		while (c < loops or loops == -1):
		
			for beat in range(self.bar_length):					
				for instrument in self.sounds.keys():
					if self.patterns[instrument][beat] =='x':
						
						inst = self.sounds[instrument]
						
						inst[0].volume = inst[1] * uniform(0.6,1)
						inst[0].seek(0.0)
						inst[0].play()
					
										
									

				pygame.time.wait(randint(0,30))
				self.clock.tick(self.fps)
			c +=1

	def playBeatsInFile(self,path_to_file,index_of_beat):
		reader = tabIO.tabIO()
		beats = reader.read(path_to_file)
		
		self.patterns = beats[index_of_beat]


		self.play()
		


			



'''drum_machine = drumMachine()
drum_machine.set_snare_sound(volume = 0.9)
drum_machine.set_hhc_sound(volume = 0.6)
drum_machine.set_kick_sound(volume = 0.6)

#drum_machine.playBeatsInFile('beats/beats.csv',5)


drum_machine.set_snare_pattern("x----x----------")
drum_machine.set_kick_pattern("x-xx-x-x-x-x-x-x")
drum_machine.set_hhc_pattern("x---------------")
print drum_machine.patterns
drum_machine.play()'''


