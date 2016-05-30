family_status = {'Dariusz':'Father','Katarzyna':'Mother',
'Damian':'First son', 'Bartosz': 'Second son'}
# status from name

# first simple way to make a dictionary where one string is an access key,
# and the second is an accessable value
# as if the key to vault and valueable thing inside a vault


age = dict()
# age from status
age['Pierwszy Syn'] = 24
age['Drugi Syn'] = 14
age['Tata'] = 45
age['Mama'] = 45
# second way to make a dictionary, you make an empty one
# and then add pairs of key (in parenthesis) and value (after equation)

days_lived = {24:24*365, 14:14*365, 45:45*365}
# days lived from age

print "Damian w swojej rodzinie jest:", family_status['Damian']
print "Bartosz w swojej rodzinie jest:", family_status['Bartosz']
print "Poza tym Bartosz ma %d lat" % age[family_status['Bartosz']]
print "Tyle lat to %d dni" % days_lived[age['Drugi Syn']]

print "Ilosc dni zycia 45-cio latka:", days_lived[45]
print "ilosc dni zycia taty", days_lived[age['Tata']]
print "ilosc dni zycia Darka, mojego taty", days_lived[age[family_status['Dariusz']]]

inv_age = {v: k for k, v in age.items()}	#invert dictionary

print inv_age[45]

print "\n", age.values()
