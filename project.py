# Author: Aditya Mhamunkar
# This is an application which accepts a user location as a pair of co-
# ordinates, and returns a list of the five closest events, along with 
# the cheapest ticket price for each event.

from operator import itemgetter
from sets import Set
import random
import json

# this is a class for each node of the tree
class Node:
	# this the constructor of Node class
	# arguments - location, Node object of left child, Node object of right child,
	# 	tree depth level, and distance from user location 
	def __init__(self, location, left_child, right_child, level, distance):
		self.location = location
		self.left_child = left_child
		self.right_child = right_child
		self.level = level
		self.distance = distance

# this method constructs the k dimentional tree 
# arguments - list of event locations, depth of tree level
# returns - Node object
def kdTree(listOfEvents, level):
	try:
		kd = len(listOfEvents[0])
	except IndexError as e:
		return None
	# generating the axis for branch direction selection
	xy = level % kd
	listOfEvents.sort(key = itemgetter(xy))
	median = len(listOfEvents) // 2
	# creating a Node object with a left child and right child
	treeNode = Node(listOfEvents[median], kdTree(listOfEvents[:median], level+1), 
		kdTree(listOfEvents[median+1:], level+1), level, -1)
	return treeNode

# this method adds the Manhattan distance between two locations
# 	to the given node object
# arguments - user location, the event location
# returns - node object
def getManhattanDistance(node, userLocation):
	manDist = abs(node.location[0] - userLocation[0]) + abs(node.location[1] - userLocation[1])
	node.distance =manDist
	return node

# this method search for the nearest locations to the given 
# 	user location
# arguments - user location, tree and number of nearest events
# returns - a list of current best nearby events
def neighborSearch(userLocation, tree, numOfNearestEvents):
	if tree.left_child==None and tree.right_child == None:
		node = getManhattanDistance(tree, userLocation)
		#print node.location
		return [node]
		
	else:
		curBestList1 = [] 
		curBestList2 = []
		# Axis Aligned Boundary Box check
		axis = 0
		if tree.level%2 == 0:
			axis = 0
		else:
			axis = 1

		# selecting the tree branch direction (left or right)
		if userLocation[axis] <= tree.location[axis]:
			subNode = tree.left_child 
		else:
			subNode = tree.right_child
		
		# for boundary condition
		if subNode == None:
			return [getManhattanDistance(tree, userLocation)]

		# getting the current best list
		curBestList1 = neighborSearch(userLocation, subNode, numOfNearestEvents)

		# getting distance from search node to current node
		treeDist = getManhattanDistance(tree, userLocation)


		#checking for other branch if necessary
		if userLocation[axis]-treeDist.location[axis] <= curBestList1[-1].distance:
			if userLocation[axis] <= tree.location[axis]:
				subNode = tree.right_child 
			else:
				subNode = tree.left_child
			
			# for boundary condition
			if subNode != None:
				curBestList2 = neighborSearch(userLocation, subNode, numOfNearestEvents)

		# combining the two lists
		curBestList = curBestList1 + curBestList2
		curBestList.sort(key=lambda item: item.distance)

		# triming the list for required number of events
		curBestList = curBestList[:numOfNearestEvents]


		if len(curBestList) >= numOfNearestEvents:
			if curBestList[-1].distance > treeDist.distance:
				curBestList.append(treeDist)
		else:
			curBestList.append(treeDist)

		
		curBestList.sort(key=lambda item: item.distance)

		return curBestList

# arguments - a range of numbers
# return - a tuple of randomly generated co-ordinates in the given range
def getRandomLocation(tupRange):
	return (random.randint(tupRange[0],tupRange[1]), random.randint(tupRange[0],tupRange[1]))

# this program assumes that at each event there can be
# 0 to 10 tickets available
# this method generates the tickets for each event
# arguments-  number of tickets to be generated
# returns - list of randomly generated tickets
def generateTickets(numberOfTickets):
	tickets = []
	if(numberOfTickets == 0):
		return None
	for x in xrange(0, numberOfTickets):
		tickets.append(round(random.uniform(1.00,500.00),2))
	tickets.sort()
	return tickets

# this is the Driver function of the program
def main():
	global listOfEvents
	global distance
	distance = -1
	getNumOfEvents = 5

	# storage for event objects at appropriate location
	data=[[None for x in range(-10, 11)] for y in range(-10,11)]
	# set of unique tuples of locations
	setOfEvents = Set()

	# Generating random events
	for x in xrange(random.randint(0,399)):
		loc = getRandomLocation([-10,10])
		# assuming max of 10 tickets available at each event
		numberOfTickets = random.randint(0,10)
		tickets = generateTickets(numberOfTickets)
		event = {'num': x, 'position': loc, 'tickets': tickets}
		data[loc[0]][loc[1]] = event
		setOfEvents.add(loc)
	
	# list of event locations
	listOfEvents = list(setOfEvents)
	# storing event data in the form of json
	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

	# printing event location list
	print "List of event locations:"
	for x in xrange(0,len(listOfEvents)):
		print list(listOfEvents[x]), 
		print ",",

	print "\nRandom input created!\n\n"

	# if number of events present are zero, informing the user	
	if len(listOfEvents)==0:
		print "Opps! Currently are no events around you."
		return None

	# calling kdtree() for tree contruction
	# arguments - list of event locations, depth of tree level
	# returns - tree
	tree = kdTree(listOfEvents, 0)

	# accepting user location
	userNumber = input('Enter User Location (Format: x,y): ')
	# Make sure the input is an integer number
	x = int(userNumber[0])
	y = int(userNumber[1])
	userLocation = (x,y)

	# checking boundary conditions for user input
	if x>10 or x<-10 or x>10 or x<-10:
		print "User location out of range!"
		return None
	print "Events closest to",userLocation

	# calling the search method
	resNodeList = neighborSearch(userLocation, tree, getNumOfEvents)
	#sorting the list of nearest events according to the distances
	resNodeList.sort(key=lambda item: item.distance)
	
	# printing the results (event number, cheapest ticket price, distance)
	
	# if returned list of nearby events is less than expected number
	if len(resNodeList)<getNumOfEvents:
		for x in xrange(0,len(resNodeList)):
			dataNode = data[resNodeList[x].location[0]][resNodeList[x].location[1]]
			print "Event:",str(dataNode["num"]).zfill(3),
			print "-",
			if dataNode["tickets"] != None:
				print "$", dataNode['tickets'][0],",",
			else:
				print "No tickets available",
			print "Distance",resNodeList[x].distance 
 
	else:
		for x in xrange(0,getNumOfEvents):
			dataNode = data[resNodeList[x].location[0]][resNodeList[x].location[1]]
			print "Event:",str(dataNode["num"]).zfill(3),
			print "-",
			if dataNode["tickets"] != None:
				print "$", dataNode['tickets'][0],",",
			else:
				print "No tickets available",
			print "Distance",resNodeList[x].distance 

# calling the driver function
main()
