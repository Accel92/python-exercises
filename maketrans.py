from string import maketrans
# from string module imports translation function

table_of_cypher = "aeiou"
output_table = "4310u"

translation_table = maketrans(table_of_cypher, output_table)

sentence = "Hi there, welcome to college humor, It has a \
good bit and you can dance to it."

print sentence,\
"\n\nAnd translated one\n"
print sentence.translate(translation_table)
