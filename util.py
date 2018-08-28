def stretch_pipe(l, up_or_down):
	'''
	Given a length and something to specify whether up or down, choose a 
	pipe sprite and stretch it to be equal to length l
	'''
	
	if up_or_down == 'up':
		sprite = Config. 




'''
List all of our constants used in the game here
'''
screenWidth = None
screenHeight = None

pipeWidth = None 

avatarWidth = None
avatarHeight = None

screenStep = None # How many pixels to shift the screen by each time

initBirdY = None # The starting position for our bird

hopVelocity = None # The initial velocity applied when the bird hops


# Treat each pixel as being one meter, to simplify physics

timeStep = None # How much time passes with each step of our display



'''
Equations for our game physics calculations
'''
def p2(p1, v, a, t):
	'''
	r = r0 + vt - 1/2 at^2
	'''
	return p1 + (v * t) - (a * (t ** 2)) / 2

def v2(v, a, t):
	'''
	v = v0 + at
	'''
	return v + (a * t)
