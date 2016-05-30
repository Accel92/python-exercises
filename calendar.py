from sys import argv
import calendar

scripts_name, year_provided, month_provided = argv
year_provided = int(year_provided)
month_provided = int(month_provided)

current_calendar = calendar.month(year_provided, month_provided)

list_of_months = {
1:"January",2:"February",3:"March",4:"April",5:"May",\
6:"June",7:"July",8:"August",9:"September",10:"October",\
11:"November",12:"December"}

for i in range(1,13):
	if month_provided == i:
		month_name = list_of_months[i]
	else:
		i+=1
		
print "Your calendar for %s:" % month_name,"\n"
print current_calendar
