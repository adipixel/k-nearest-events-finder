from operator import itemgetter
from sets import Set
import random
import json

class Node:
	def __init__(self, location, left_child, right_child, level, distance):
		self.location = location
		self.left_child = left_child
		self.right_child = right_child
		self.level = level
		self.distance = distance

def kdTree(listOfEvents, level):
	try:
		kd = len(listOfEvents[0])
	except IndexError as e:
		return None

	xy = level % kd
	listOfEvents.sort(key = itemgetter(xy))
	median = len(listOfEvents) // 2
	treeNode = Node(listOfEvents[median], kdTree(listOfEvents[:median], level+1), 
		kdTree(listOfEvents[median+1:], level+1), level, -1)
	return treeNode


def getManhattanDistance(node, userLocation):
	manDist = abs(node.location[0] - userLocation[0]) + abs(node.location[1] - userLocation[1])
	node.distance =manDist
	return node


def neighborSearch(userLocation, tree, numOfNearestEvents):
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
				#return [getManhattanDistance(tree, userLocation)]
				curBestList2 = neighborSearch(userLocation, subNode, numOfNearestEvents)

		curBestList = curBestList1 + curBestList2
		curBestList.sort(key=lambda item: item.distance)

		curBestList = curBestList[:numOfNearestEvents]

		if len(curBestList) >= numOfNearestEvents:
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
	getNumOfEvents = 5

	data=[[None for x in range(-10, 11)] for y in range(-10,11)]
	setOfEvents = Set()

	# Generating random events
	for x in xrange(random.randint(0,399)):
		loc = getRandomLocation([-10,11])
		# assuming max of 10 tickets available at each event
		numberOfTickets = random.randint(0,10)
		tickets = generateTickets(numberOfTickets)
		event = {'num': x, 'position': loc, 'tickets': tickets}
		data[loc[0]][loc[1]] = event
		setOfEvents.add(loc)
	
	listOfEvents = list(setOfEvents)

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)
	print "Random input created!"

	
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

	if len(listOfEvents)==0:
		print "Opps! Currently are no events around you."
		return None

	tree = kdTree(listOfEvents, 0)
	userNumber = input('Enter User Location (Format: x,y): ')
	# Make sure the input is an integer number
	x = int(userNumber[0])
	y = int(userNumber[1])
	userLocation = (x,y)
	print "Events closest to",userLocation

	resNodeList = neighborSearch(userLocation, tree, getNumOfEvents)
	resNodeList.sort(key=lambda item: item.distance)
	
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


main()
