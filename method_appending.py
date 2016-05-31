class Passenger:
	def firstmethod(self):
		print "first method"
		
guy = Passenger()
guy.firstmethod()

def secondmethod(self):
	print "second method"
	raw_input("what is your name, nigga?\n>")
	
Passenger.secondmethod = secondmethod
	
guy.secondmethod()
