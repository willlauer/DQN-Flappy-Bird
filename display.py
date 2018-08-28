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

		
		# Appearance shouldn't really matter, but if it does we can add an
		# something to define order, like a counter
		# 'name' : (img, (blitAtX, blitAtY))
		self.blits = {} 


	def blitAll(self):
		'''
		Blit everything in (self.permanentBlits)U(self.tempBlits)
		'''
		for blit in list(self.blits.values())
			self.screen.blit(blit[0], blit[1])


	def removePipe(self, pipeCounter):
		'''
		Remove the two pipe segments that correspond to pipeCounter
		This mutates the dictionary, so be careful with other references
		'''
		del self.tempBlits['TopPipe' + str(pipeCounter)]
		del self.tempBlits['BotPipe' + str(pipeCounter)]



	def addNewPipe(self, y1, y2, pipeCounter):
		'''
		y1: the bottom coordinate of the top pipe piece
		y2: the top coordinate of the bottom pipe piece
		pipeCounter: which pipe number this is
		'''
		topPipeLength = y1
		botPipeLength = config.screenHeight - y2

		newTopPipe = self.topPipe.copy()
		newTopPipe = pygame.transform.scale(newTopPipe, (config.pipeWidth, topPipeLength))

		newBotPipe = self.botPipe.copy()
		newBotPipe = pygame.transform.scale(newBotPipe, (config.pipeWidth, botPipeLength))

		# At the moment, we're just going to make new elements pop up towards the edge
		# of the screen. To make it look nicer, we should have a buffer zone where we
		# initially init blit this stuff, then slowly slide it onto the screen
		colCoord = config.screenWidth - pipeWidth

		topCoords = (0, colCoord)
		botCoords = (config.screenHeight - botPipeLength, colCoord)

		# Initialize the tuple of img, coords that we'll use to blit this to the screen
		self.tempBlits['TopPipe' + str(pipeCounter)] = (newTopPipe, topCoords)
		self.tempBlits['BotPipe' + str(pipeCounter)] = (newBotPipe, botCoords)
	


	def moveBird(self, y):
		'''
		Move the bird to the new y coordinate
		Does not update the display
		'''
		oldBird = self.blits['Bird']
		newBird = (oldBird[0], (oldBird[1][0], y))
		self.blits['Bird'] = newBird

















