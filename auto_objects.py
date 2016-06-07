class Plantation:
	
	def __init__(self, a, b):
		self.__plant_a = a
		self.__plant_b = b
	
	def grow(self):
		self.__plant_a += self.__plant_b
		self.__plant_b += self.__plant_a
	def show_plants(self):
		print("plant a:", self.__plant_a, "plant b:",self.__plant_b)
		
	
my_plants = KonopiaPlantation(2, 4)
my_plants.show_plants()
print("")
my_plants.konopia_grow()
my_plants.show_plants()
print("")
my_plants.konopia_grow()
my_plants.show_plants()
print("")

def create(object_type, element_a, element_b):
	creation = object_type(element_a, element_b)
	return creation
	
plantacja = create(Plantation, 2, 4)
plantacja.show_plants()
	
