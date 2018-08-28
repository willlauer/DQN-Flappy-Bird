import config
import util


class Display:
	
	'''
	Contains all of the objects in our display, and a wrapper to access the pixels stored therein
	'''

	def __init__(self):
		
		self.colors = {'green': (16, 124, 16), 'blue': (0, 0, 231), 'orange': (243, 87, 40), 'red': (241, 0, 0)}

		
		self.bird = pygame.image.load(config.BIRD)
		self.upPipe = pygame.image.load(config.UPPIPE)
		self.downPipe = pygame.image.load(config.DOWNPIPE)
		self.background = pygame.image.load(config.BACKGROUND)

		
		# Store the bird and the background
		# Stored as tuples of (obj, (coords))
		self.permanentBlits = []
		
		# Store in order of appearance
		# 'name' : (img, (blitAtX, blitAtY))
		self.tempBlits = {} 


	def blitAll(self, di):
		
		for key in di:
				

	def displayNewPipe(self, y1, y2):
		'''	
		Add two new pipe segments, with the downpipe reaching down to y1,
		and the uppipe reaching up to y2. This will have been created previously in
		the game class where we need to store all of the objects
		'''
