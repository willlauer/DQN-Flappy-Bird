import numpy as np

class Game:
	
	'''
	This class holds the game state
	'''
	
	def __init__(self):
	
		self.display = Display()
	
		# Store all information relevant to the bird, like
		# position and velocity
		self.birdState = 
			{
				'y': config.initBirdY,
				'v': 0
			}
		
		# Track the id of the oldest pipe still displayed
		# 1-indexed just cause
		# This is updated when a pipe is deleted
		self.minPipeID = 1 

		# Track the id to use when we add a new pipe
		# This is updated when a pipe is created
		self.curPipeID = 1

		# Monitor all pipes and their coordinates
		# Map from pipe id to a tuple of
		# topPipeCoords, botPipeCoords
		# ((x1, y1, x2, y2), (x3, y3, x4, y4))
		self.pipeState = {}
		
		# Track how many time steps have passed
		self.time = 0 
		self.hop = False

		# We can have a top pipe no longer than this  
		self.maxPipeLength = int((util.screenHeight - util.pipeSeparation) * 0.8)
		# and no shorter than this
		self.minPipeLength = int((util.screenHeight - util.pipeSeparation) * 0.2)


	def updateBirdLoc(self):
		'''
	 	Given bird state, computes the new bird location and velocity	
		Make changes to bird state.
		'''
		y, v = self.birdState['y'], self.birdState['v']	
		newLoc = util.p2(y, v, config.gravity, config.timeStep)
		newVel = util.v2(v, config.gravity, config.timeStep)

		self.birdState['y'] = newLoc
		self.birdState['v'] = newVel

	def birdHop(self):
		'''
		If we got user input indicating we should perform a hop,
		reset the bird's velocity
		'''
		self.birdState['v'] = util.hopVelocity 

	def gameOver(self):
		'''
		Check for collisions with between the bird, the pipes, and the 
		ground
		'''
		pass

	def finish(self):
		'''	
		Run the game-over stuff and reset for another run
		'''
		pass

	def updateLHSPipes(self):
		'''
		Check whether the leftmost pipe, once slid, will be off the
		left hand side of the screen. If so, remove it from the pipe data
		and issue a message to the display to remove this pipe
		'''
		minPipeXCoord = self.pipeState[self.minPipeID][0]

		if minPipeXCoord - util.screenStep < 0:
			self.display.removePipe(self.minPipeID)
			del self.pipeState[self.minPipeID]
			self.minPipeID += 1

	def slideScreen(self):
		'''
		Update the x coordinates of all the pipes. Only the pipe x coordinates
		change currently. Send a message to the display to do the same
		'''
		for pipeID in self.pipeState:
			self.pipeState[pipeID][1] -= util.screenStep
			self.pipeState[pipeID][3] -= util.screenStep

		self.display.slideScreen()

	def createNewPipe(self):
		'''
		Returns a tuple corresponding to the coordinates for a new pipe
		added to the right hand side of the screen
		'''
		topLen = np.random.randint(self.minPipeLength, self.maxPipeLength)
		botLen = util.screenHeight - topLen - util.pipeSeparation

		# Therefore the top pipe extend from rows 0 to topLen, and the 
		# bottom pipe will extend from util.screenHeight - botLen to the bottom
		# Store top left, bottom right coordinates for each image
		topCoords = (0, util.screenWidth - util.pipeWidth, topLen, util.screenWidth)
		botCoords = (util.screenHeight - botLen, util.screenWidth - util.pipeWidth,
					 util.screenHeight, util.screenWidth)

		return (topCoords, botCoords)

		

	
	def updateRHSPipes(self):
		'''
		Every once in a while, we add a new pipe to the right hand side
		This gets called only when we actually want to add a new pipe
		'''
		newCoords = self.createNewPipe()
		self.pipeState[self.curPipeID] = newCoords
		self.display.addNewPipe(self.curPipeID, newCoords)
		self.curPipeID += 1


	def runTimeStep(self):
		'''
		Run a primary time-step. Each time step should consist of the
		following basic steps:
			1. Update the bird's y-coordinate
			2. Check for game-over conditions
			3. Check for pipes that will be removed on the left-hand side
				of the screen and remove them if any
			4. Slide everything to the left except for the bird
			5. Check if we should initialize a new pipe on the right-hand
				side of the screen and add it if yes
		'''
		if self.doHop: 
			self.birdHop()
		
		self.updateBirdLoc()
	
		if self.gameOver():	
			self.finish()

		self.updateLHSPipes()

		self.slideScreen()

		if self.time % util.pipeInterval == 0:
			self.updateRHSPipes()

		self.display.update() # Update the visible display
		self.time += 1 

		

	def runInitialTimeStep(self):
		'''
		Run a time-step with no pipes
		'''
		



	def run(self):
		
		for _ in range(config.initTimeSteps):
			self.runInitialTimeStep()	
	
		while not self.gameOver:
			self.runTimeStep()
