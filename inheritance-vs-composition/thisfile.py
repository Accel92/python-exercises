import other_mod

class Child(object):
	
	spec = "Knight"
	
	def __init__(self):
		self.mod1 = other_mod
		
	def override(self):
		self.mod1.override(self)
		
	def implicit(self):
		self.mod1.implicit(self)
	
	def altered(self):
		self.mod1.altered(self)
		
dziecior = Child()
dziecior.override()


class VeryBadChild(Child):
	pass
	
	
rudy_dziecior = VeryBadChild()
print rudy_dziecior.spec 
