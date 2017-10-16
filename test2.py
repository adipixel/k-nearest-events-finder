from operator import itemgetter
from sets import Set
import random
import json

class Node:
	def __init__(self, location, left_child, right_child, level, distance, otherBranch):
		self.location = location
		self.left_child = left_child
		self.right_child = right_child
		self.level = level
		self.distance = distance
		self.otherBranch = otherBranch

def kdTree(listOfEvents, level):
	try:
		k = len(listOfEvents[0]) # assumes all points have the same dimension
	except IndexError as e: # if not point_list:
		return None

	xy = level % k
	listOfEvents.sort(key = itemgetter(xy))
	median = len(listOfEvents) // 2
	treeNode = Node(listOfEvents[median], kdTree(listOfEvents[:median], level+1), 
		kdTree(listOfEvents[median+1:], level+1), level, -1, False)
	return treeNode


def getManhattanDistance(node, userLocation):
	manDist = abs(node.location[0] - userLocation[0]) + abs(node.location[1] - userLocation[1])
	node.distance =manDist
	return node


def neighborSearch(userLocation, tree):
	if tree.left_child==None and tree.right_child == None:
		node = getManhattanDistance(tree, userLocation)
		#print node.location
		return [node]
		
	else:
		curBestList1 = [] 
		curBestList2 = []
		# AABB check
		axis = 0
		if tree.level%2 == 0:
			axis = 0
		else:
			axis = 1

		if userLocation[axis] <= tree.location[axis]:
			subNode = tree.left_child 
		else:
			subNode = tree.right_child
		
		# for boundary condition
		if subNode == None:
			return [getManhattanDistance(tree, userLocation)]

		# getting the current best list
		curBestList1 = neighborSearch(userLocation, subNode)

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
				#return [getManhattanDistance(tree, userLocation)]
				curBestList2 = neighborSearch(userLocation, subNode)

		curBestList = curBestList1 + curBestList2
		curBestList.sort(key=lambda item: item.distance)

		curBestList = curBestList[:3]

		if len(curBestList) >= 3:
			if curBestList[-1].distance > treeDist.distance:
				curBestList.append(treeDist)
		else:
			curBestList.append(treeDist)

		
		curBestList.sort(key=lambda item: item.distance)

		return curBestList

def getRandomLocation(tupRange):
	return (random.randint(tupRange[0],tupRange[1]), random.randint(tupRange[0],tupRange[1]))

def generateTickets(numberOfTickets):
	tickets = []
	if(numberOfTickets == 0):
		return None
	for x in xrange(0, numberOfTickets):
		tickets.append(round(random.uniform(1.00,500.00),2))
	tickets.sort()
	return tickets

def main():
	global distance
	distance = -1
	getNumOfEvents = 3
	data=[[None for x in range(-10, 10)] for y in range(-10,10)]
	

	setOfEvents = Set()

	for x in xrange(random.randint(0,10)):
		loc = getRandomLocation([-10,11])
		# assuming max of 10 tickets available at each event
		numberOfTickets = random.randint(0,10)
		tickets = generateTickets(numberOfTickets)
		event = {'num': x, 'position': loc, 'tickets': tickets}
		data[loc[0]][loc[1]] = event
		setOfEvents.add(loc)
	
	listOfEvents = list(setOfEvents)

	for x in xrange(-10,11):	
		for y in xrange(-10,11):
			if x==0 and y == 0:
				print "+",
			else:
				if data[x][y] != None:
					print "@",
				else:
					print "-",
		print ""


	tree = kdTree(listOfEvents, 0)
	userNumber = input('Enter User Location (Format: x,y): ')
	# Make sure the input is an integer number
	x = int(userNumber[0])
	y = int(userNumber[1])
	userLocation = (x,y)
	print "User Location: ",userLocation

	resNodeList = neighborSearch(userLocation, tree)
	resNodeList.sort(key=lambda item: item.distance)
	for x in xrange(0,getNumOfEvents):
		print resNodeList[x].location,
		print ":",
		print resNodeList[x].distance
		print data[resNodeList[x].location[0]][resNodeList[x].location[1]]



main()
