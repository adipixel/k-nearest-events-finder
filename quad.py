class Quad:
   def __init__(self, ne, se, sw, nw, hasChild, topLeft, bottomRight):
      self.ne = ne
      self.se = se
      self.nw = nw
      self.nw = nw
      self.hasChild = hasChild
      self.topLeft = topLeft
      self.bottomRight = bottomRight
   
   def getEvent(self):
      return self.event