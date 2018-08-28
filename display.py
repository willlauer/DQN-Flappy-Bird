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
		self.pipeIDs = [] # eh? could help 
		self.blits = {} 


	def removePipe(self, pipeCounter):
		'''
		Remove the two pipe segments that correspond to pipeCounter
		This mutates the dictionary, so be careful with other references
		'''
		del self.tempBlits['TopPipe' + str(pipeCounter)]
		del self.tempBlits['BotPipe' + str(pipeCounter)]

	def slideScreen(self):
		'''
		Analagous to the slideScreen method in game.py. Update the x 
		coordinates of each of our pipes
		'''
		for pipeID in self.pipeIDs:
			
			# So we can update our blits
			topID = 'TopPipe' + str(pipeID)
			botID = 'BotPipe' + str(pipeID)
			
			# orig top img, coords
			# orig bot img, coords
			otImg, otCoords = self.blits[topID][0], self.blits[topID][1]
			obImg, obcoords = self.blits[botID][0], self.blits[botID][1]

			# update the column coordinate of the pipes corresponding to ID
			self.blits[topID] = (otImg, (otCoords[0], otCoords[1] - util.screenStep))
			self.blits[botID] = (obImg, (obCoords[0], obCoords[1] - util.screenStep))

			


		


	def addNewPipe(self, pipeID, coords):
		'''
		pipeID = int
		coords = topCoords, botCoords
		topCoords = x1, y1, x2, y2
		botCoords = x3, y3, x4, y4
		'''
		topCoords, botCoords = coords
		topPipeLength = topCoords[2] - topCoords[0]
		botPipeLength = botCoords[2] - botCoords[0]

		# Create new copies of our pipe surfaces and scale them to have the 
		# desired lengths, with constant width
		newTopPipe = self.topPipe.copy()
		newTopPipe = pygame.transform.scale(newTopPipe, (config.pipeWidth, topPipeLength))
		newBotPipe = self.botPipe.copy()
		newBotPipe = pygame.transform.scale(newBotPipe, (config.pipeWidth, botPipeLength))

		blitTopCoords = topCoords[0], topCoords[1]
		blitBotCoords = botCoords[0], botCoords[1]

		# Initialize the tuple of img, coords that we'll use to blit this to the screen
		# Add them to the dict of things to blit to the screen
		self.tempBlits['TopPipe' + str(pipeID)] = (newTopPipe, blitTopCoords)
		self.tempBlits['BotPipe' + str(pipeID)] = (newBotPipe, blitBotCoords)
	


	def moveBird(self, y):
		'''
		Move the bird to the new y coordinate
		Does not update the display
		'''
		oldBird = self.blits['Bird']
		newBird = (oldBird[0], (oldBird[1][0], y))
		self.blits['Bird'] = newBird


	def update(self):
		'''
		After the game has called methods in this class to make changes to the 
		display, blit all of them to the screen and flip to make them visible
		'''
		for blit in list(self.blits.values()):
			self.screen.blit(blit[0], blit[1])
		pygame.display.flip()

			














