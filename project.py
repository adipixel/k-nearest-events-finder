from seeddata import generateNumberOfEvents, genRandXY, generateTickets
from quad import Quad

import random
import json

# storage for randomly generated json data
global size
size = 32
area = [[None for x in range(size)] for y in range(size)]
neighbors = []

# data structure for a quad

def getQuadNum(n, topLeft, bottomRight, position):
	if topLeft[0] <= position[0] and bottomRight[0]-(n/2) >= position[0]:
		if topLeft[1] <= position[1] and bottomRight[1]-(n/2) >= position[1]:
			return 0
		else:
			return 1
	else:
		if topLeft[1] <= position[1] and bottomRight[1]-(n/2) >= position[1]:
			return 3
		else:
			return 2


# inserting events to data structure using quad tree
def insertEvent(event, n, quad):
	if (n==1):
		# insert event
		area[event['position'][0]][event['position'][1]] = event
	else:
		quadNum = getQuadNum(n, quad.topLeft, quad.bottomRight, event['position'])
		print quadNum
		quad.subQ.append(Quad(n/2, False, [quad.topLeft[0],quad.topLeft[1]], [quad.bottomRight[0]-(n/2), quad.bottomRight[1]-(n/2)]))
		quad.subQ.append(Quad(n/2, False, [quad.topLeft[0],quad.topLeft[1]+(n/2)], [quad.bottomRight[0]-(n/2), quad.bottomRight[1]]))
		quad.subQ.append(Quad(n/2, False, [quad.topLeft[0]+(n/2),quad.topLeft[1]+(n/2)], [quad.bottomRight[0], quad.bottomRight[1]]))
		quad.subQ.append(Quad(n/2, False, [quad.topLeft[0]+(n/2),quad.topLeft[1]], [quad.bottomRight[0], quad.bottomRight[1]-(n/2)]))

		quad.quadFlag[quadNum] = True
		subQuad = quad.subQ[quadNum]
		insertEvent(event, n/2, subQuad)


def searchEvent(user, quad):
	userQuad = getQuadNum(quad.n, quad.topLeft, quad.bottomRight, user)
	#print userQuad
	if quad.n == 1:
		cell = [quad.topLeft[0], quad.topLeft[1]]
		if area[cell[0]][cell[1]] != None: # Verification check but can be removed.
			neighbors.append(cell)
			return 0
		return 0
		
	if(quad.quadFlag[userQuad] == True and quad.checked == False):
		userSubQuad = quad.subQ[userQuad]
		searchEvent(user, userSubQuad)
		userSubQuad.checked = True

	# move to next
	for x in xrange(0,4):
		if (quad.subQ[x].checked == False and quad.quadFlag[x] == True):
			searchEvent(user, quad.subQ[x])
			quad.subQ[x].checked = True

	# special case: check for one step boxes

	# 1. get quadrant num of user
	# 2. check whether it has a valid child (true quadFlag)
		# 2.1. if yes, goto 1 with selected sub quad
			# 2.1.2. if leaf node with data, retrive data
	# 4. if no, check the next quad
















def generateCoordinates():
	#co-ordinates range from -10 to +10
	position = genRandXY()
	if area[position[0]][position[1]] != None:
		position = generateCoordinates()
	else:
		return position
	return position


def getMatCoordinates(x,y):
	# for -10 to +10 co-ordinates, n=11
	n = 10
	col = n + x
	row = n - y
	mat = [row, col]
	return mat


# generation of input data
def generateSeedData(numberOfEvents, n, quad):
	data = []
	eventNumber = 0;
	position = []
	for x in xrange(0,numberOfEvents):
		position = generateCoordinates()
		matPos = getMatCoordinates(position[0], position[1])
		numberOfTickets = random.randint(0,10)
		tickets = generateTickets(numberOfTickets)
		event = {'num': eventNumber, 'position': matPos, 'coPos': position, 'tickets': tickets}
		eventNumber = eventNumber + 1
		insertEvent(event, n, quad)
	return area

def main():
	n=32
	quad = Quad(n, False, [0,0], [n-1,n-1])
	size = n
	numberOfEvents = generateNumberOfEvents()
	inputData = generateSeedData(numberOfEvents, n, quad)
	with open('data.json', 'w') as outfile:
		json.dump(inputData, outfile)
	print "Random input created!"

	for x in xrange(0,n):
		for y in xrange(0,n):
			if(x%4 == 0 and y%4 == 0):
				if area[x][y] == None:
					print "+",
				else:
					print "*",
			else:
				if area[x][y] == None:
					print "-",
				else:
					print "@",
			
		print ""



	userNumber = input('Enter User Location (Format: x,y): ')
	# Make sure the input is an integer number
	x = int(userNumber[0])
	y = int(userNumber[1])
	inputPos = [x,y]
	print inputPos
	user = getMatCoordinates(x,y)
	print user

	#nearest 5 events
	

	
main()