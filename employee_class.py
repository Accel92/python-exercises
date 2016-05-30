class Employee:
	'''List of employees in company'''
	"Common base class for all employees"
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name: %s, Salary: %s" %(self.name, self.salary)
		
		
employee1 = Employee("JohnyMacaroni", "5600")
employee2 = Employee("BigLeap", "3800")

employee1.displayEmployee()
employee2.displayEmployee()

employee1.age = 24
employee2.age = 23

print "Employee 1 age: %s" %(employee1.age)

del employee2.age
print "Employee count is:",Employee.empCount

if hasattr(employee1, "name"):
	print employee1.name
	
setattr(employee2, "age", 23)
for i in range(0,1):
	try:
		print "age of Johny/notJohny: ",getattr(employee2, "age")
	except: #AttributeError, argument:
		print "Error: something went wrong"#"AttributeError: %s"% argument
		break

print Employee.__dict__
print Employee.__doc__
