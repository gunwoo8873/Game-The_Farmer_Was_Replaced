from __builtins__ import *

#########################################
# Current Ground Size : 6 * 6
# Items DataType : Float <0.0>
#########################################

# Current haved item list
Item_Values = [
	Items.Hay,
	Items.Carrot, 
	Items.Wood, 
	Items.Water
	]

# Current Unlock Entitie List
Entitie_Types = [
	Entities.Grass, 
	Entities.Bush, 
	Entities.Carrot
	]

# Current Unlock Ground List
Ground_Types = [
	Grounds.Grassland, # The Default use of standard Seed Ground
	Grounds.Soil # Add a new Type of Carrot Seed Ground
	]

# Directions <0=N, 1=E, 2=S, 3=W>
Directions = [
	North, 
	East, 
	South, 
	West,
	]

# Location Size
Max_Count = get_world_size()

# Default Configs
Default_Count = 0
Default_Harvest = False


# Configs
def Location_Range(i):
	return range(i)

# Actions
def Move_Direction(dir):
	return move(dir)

def Ground_Type():
	for _ in Location_Range(Max_Count):
		if get_ground_type() == Ground_Types[0]:
			if can_harvest():
				return harvest()
		elif get_ground_type() != Ground_Types[1]:
			return till()
			
def Plant_Entity():
	if get_pos_x() % 2 == 0:
		if get_entity_type() != Entitie_Types[0]:
			return plant(Entitie_Types[0])
	else:
		if get_entity_type() != Entitie_Types[1]:
			return plant(Entitie_Types[1])

# TODO: Need to Harvest feature logic refactor
def Grass_Harvest():
	if get_ground_type() == Ground_Types[0]:
		if can_harvest():
			harvest()
	elif get_ground_type() != Ground_Types[0]:
		till()
		if can_harvest():
			harvest()

def Bush_Harvest():
	if get_entity_type() == Entitie_Types[0]:
		if can_harvest():
			harvest()
	elif get_entity_type() != Entitie_Types[1]:
		plant(Entitie_Types[1])
		if can_harvest():
			harvest()

def Carrot_Harvest():
	if get_ground_type() == Ground_Types[1]:
		plant(Entitie_Types[2])
		if can_harvest():
			harvest()
	elif get_ground_type() != Ground_Types[1]:
		till()
		plant(Entitie_Types[2])
		if can_harvest():
			harvest()

# Loop Logics
while True:
	for _ in Location_Range(Max_Count):
		Grass_Harvest()
		Move_Direction(Directions[Default_Count])
	Move_Direction(Directions[1])

	for _ in Location_Range(Max_Count):
		Bush_Harvest()
		Move_Direction(Directions[Default_Count])
	Move_Direction(Directions[1])

	for _ in Location_Range(Max_Count):
		Carrot_Harvest()
		Move_Direction(Directions[Default_Count])
	Move_Direction(Directions[1])
