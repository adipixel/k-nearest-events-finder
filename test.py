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


print getQuadNum(4, [0,0], [3,3], [0,2]) # 1
print getQuadNum(4, [0,0], [3,3], [2,1]) # 3
print getQuadNum(4, [0,0], [3,3], [1,0]) # 0
print getQuadNum(4, [0,0], [3,3], [3,3]) # 2