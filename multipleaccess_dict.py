family_status = {'Darek':'Dad','Catharine':'Mom',
'Damian':'First son', 'Bartosz': 'Second son'}
# status from name

# first simple way to make a dictionary where one string is an access key,
# and the second is an accessable value
# as if the key to vault and valueable thing inside a vault


age = dict()
# age from status
age['First son'] = 24
age['Second son'] = 14
age['Dad'] = 45
age['Mom'] = 45
# second way to make a dictionary, you make an empty one
# and then add pairs of key (in parenthesis) and value (after equation)

days_lived = {24:24*365, 14:14*365, 45:45*365}
# days lived from age

print "Damian is a %s in his family" % family_status['Damian']
print "Bartosz is a %s in his family", % family_status['Bartosz']
print "Also Bartosz is" % age[family_status['Bartosz']]
print "He has lived for %s days" % days_lived[age['Drugi Syn']]

print "Days lived by 45 years old man", days_lived[45]
print "Days lived by my dad", days_lived[age['Tata']]
print "Days lived by Darek, who is my dad", days_lived[age[family_status['Darek']]]

inv_age = {v: k for k, v in age.items()}	#invert dictionary

print inv_age[45]

print "\n", age.values()
