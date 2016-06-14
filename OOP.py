from random import randint

class PlayerTemplate:
	
	def __init__(self, level):
		self._level = level
		self._hp = 100 + 50 *(self._level - 1)
		self._mana = self._hp
	
	def get_hp(self):
		return self._hp

class Enemy(object):
	
	fight_plot = "I am no plot"
	first_hit_chance_ratio = randint(0,100)
	
	def __init__(self, level, special_status = ""):
		self._level = level
		self._special = special_status
		self._name = "{} (lvl. {}){}".format(self.__class__.__name__, self._level, self._special)
		self._player_template = PlayerTemplate(self._level)
		
		self._hp = self._player_template.get_hp()*0.7
		self._mana = self._hp
		self._exp_reward = 0
		self._skills = {
		"1. First: " : self._hp // 6,
		"2. Second: " : self._hp // 4,
		"3. Nuke: " : self._hp * 2000	# serious need for change when inherited
		}	

	def attack(self):
		'''fighting AI for all opponents, change it if you need to'''
		list_of_values = [value for (key, value) in self._skills.items()]
		list_of_values.sort()
		return list_of_values[-1]
	
	def get_hp(self):
		return self._hp
	
	def get_name(self):
		return self._name
	
	def get_exp_reward(self):
		return self._exp_reward	
		
	def get_special(self):
		return self._special
		

class Warrior(Enemy):
	
	fight_plot = "Enemy Warrior appears in front of you.\nYou need to fight!"
	first_hit_chance_ratio = 30
	
	def __init__(self, level, special_status = ""):
		super(Warrior, self).__init__(level, special_status)
		self._exp_reward = 100 + 50* self._level
		#del player_template
		if self._level < 3:
			self._skills = {
			"1. Charge: " : self._hp // 4,
			}	
		elif self._level >= 6:
			self._skills = {
			"1. Charge: " : self._hp // 4,
			"2. SpinSlash: " : self._hp // 3,
			}

	
my_pet = Warrior(9, "[Boss]")
print(my_pet.get_name())
print(my_pet.fight_plot)

my_damage = my_pet.attack()
print(my_damage)
status = my_pet.get_special()
print(status)

my_wolf = Enemy(9, "[Boss]")
print(my_wolf.get_name())
print(my_pet.get_name())
