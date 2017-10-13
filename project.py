from seeddata import generateNumberOfEvents, genRandXY, generateTickets
from quad import Quad

import random
import json

# storage for randomly generated json data
w, h = 20, 20
area = [[0 for x in range(w)] for y in range(h)]

# data structure for a quad
quad = Quad(None, None, None, None, False, None)



def generateCoordinates():
	#co-ordinates range from -10 to +10
	position = genRandXY()
	if area[position[0]][position[1]] != 0 :
		position = generateCoordinates()
	else:
		return position
	return position

# generation of input data
def generateSeedData(numberOfEvents):
	data = []
	eventNumber = 0;
	position = []
	for x in xrange(0,numberOfEvents):
		position = generateCoordinates()
		numberOfTickets = random.randint(0,10)
		tickets = generateTickets(numberOfTickets)
		event = {'num': eventNumber, 'position': position, 'tickets': tickets}
		eventNumber = eventNumber + 1
		area[position[0]][position[1]] = event
		#insertIntoQuad(event, position)
	return area


#def getNearestEvents(user, num):

#def insertIntoQuad(event, position):
	




def main():
	numberOfEvents = generateNumberOfEvents()
	inputData = generateSeedData(numberOfEvents)
	with open('data.json', 'w') as outfile:
		json.dump(inputData, outfile)
	print "Random input created!"
	userNumber = input('Enter User Location (Format: x,y): ')
	# Make sure the input is an integer number
	x = int(userNumber[0])
	y = int(userNumber[1])
	user = [x,y]
	print user

	#nearest 5 events
	num = 5;

#	getNearestEvents(user, num)


main()