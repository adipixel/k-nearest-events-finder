import random
def generateNumberOfEvents():
    #return sum(random.randint(1, 6) for _ in range(numrolls))
    # for -10 to +10 area, 400 events can be generated at most
    return random.randint(0, 399)

def genRandXY():
	randomX = random.randint(0, 19)
	randomY = random.randint(0, 19)
	return [randomX,randomY]


def generateTickets(numberOfTickets):
	tickets = []
	if(numberOfTickets == 0):
		return None
	for x in xrange(0, numberOfTickets):
		tickets.append(round(random.uniform(1.00,500.00),2))
	tickets.sort()
	return tickets

