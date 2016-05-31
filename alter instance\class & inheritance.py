class SimpleCounter(object):
   
	#def __init__(self):
	#	self.__secretCount = 0
  
	__secretCount = 0
   
	def count_instance(self):
		self.__secretCount += 1
		
	def count_class(self):
		JustCounter.__secretCount +=1

	def get_secret_instance_counter(self):
		return self.__secretCount
		
	def get_secret_class_counter(self):
		return JustCounter.__secretCount

counter = JustCounter()
counter.count_instance()
counter.count_instance()
counter.count_instance()
counter.count_instance()
counter.count_instance()

'''print counter.__secretCount'''    # will not work on __ atributes
print "Instance has counted up to:", counter.get_secret_instance_counter()

counter.count_class()
'''print JustCounter.__secretCount'''	# will not work as well
print "Class has counted up to:", counter.get_secret_class_counter()

class InheritedCounter(SimpleCounter):
	
	pass

next_counter = InheritedCounter()
next_counter.count_instance()
next_counter.count_instance()

next_counter.count_class()

print "Instance has counted from inherited (class) value up to:",next_counter.get_secret_instance_counter()
print "Class has counted from inherited (class) value up to:", next_counter.get_secret_class_counter()
