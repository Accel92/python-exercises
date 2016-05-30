foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bar = [i*i for i in range(10,101)]

print foo, "\n"
print bar

#---------------------------------------------------------------
i = 25

while i <=10:
	print i
	i+=1
else:
	print "while loop exhausted"
	
#---------------------------------------------------------------

names = ["Damian", "Bartosz", "Darek", "Catharine"]

for i in range(len(names)):
	print names[i],\
	", Next name is:\n"

#---------------------------------------------------------------

import shaz_module
print dir(shaz_module)

for num in range(3345, 3500):
	for i in range(2,num):
		if num%i == 0:
			break
	else:
		print num, "is prime"
