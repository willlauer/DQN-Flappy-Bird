
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
		self.minPipeID = -1

		# Monitor all pipes and their coordinates
		# Map from pipe id to a tuple of
		# (topX, topLowestY, botX, botHighestY)
		self.pipeState = {}

		self.timeStep = 0
		self.hop = False

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
			self.display.rmovePipe(self.minPipeID)
			del self.pipeState[self.minPipeID]
			self.minPipeID += 1

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
		self.updateRHSPipes()

		self.updateDisplay()


		

	def runInitialTimeStep(self):
		'''
		Run a time-step with no pipes
		'''
		



	def run(self):
		
		for _ in range(config.initTimeSteps):
			self.runInitialTimeStep()	
	
		while not self.gameOver:
			self.runTimeStep()
