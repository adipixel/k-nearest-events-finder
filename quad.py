class Quad:

	def __init__(self, n, checked, topLeft, bottomRight):
		self.topLeft = topLeft
		self.bottomRight = bottomRight
		self.checked = checked
		self.quadFlag = [False, False, False, False]
		self.subQ = []
		self.n = n

	def setQuadFlag(num):
		self.quadFlag[num] = True