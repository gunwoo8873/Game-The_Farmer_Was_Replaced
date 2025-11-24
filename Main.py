from __builtins__ import *

#########################################
# Current Ground Size : 4 * 4
# Items DataType : Float <0.0>
#########################################

# Items <Entities.Name>
Items_Values = [Items.Hay, Items.Carrot, Items.Wood, Items.Water]

# Entities <Entities.Name>
Entities_Types = [Entities.Grass, Entities.Bush, Entities.Carrot]

# Grounds <Grounds.Name>
Grounds_Types = [Grounds.Grassland, Grounds.Soil]

# Directions <0=N, 1=E, 2=S, 3=W>
Directions = [North, East, South, West]

# Configs
def Location_Range(l):
    return range(l)

Max_Location = get_world_size()

# Actions
def Move_Direction(dir):
    return move(dir)

def Move_Locations(x, y):
    return get_pos_x(x), get_pos_y(y)

def Grass_Harvest():
    if get_ground_type() == Grounds_Types[0]:
        if can_harvest():
            harvest()
    elif get_ground_type() != Grounds_Types[0]:
        till()
        # plant(Entities_Types[0])
        if can_harvest():
            harvest()

def Bush_Harvest():
    if get_entity_type() == Entities_Types[1]:
        if can_harvest():
            harvest()
    elif get_entity_type() != Entities_Types[1]:
        plant(Entities_Types[1])
        if can_harvest():
            harvest()

def Carrot_Harvest():
    if get_ground_type() == Grounds_Types[1]:
        plant(Entities_Types[2])
        if can_harvest():
            harvest()
    elif get_ground_type() != Grounds_Types[1]:
        till()
        plant(Entities_Types[2])
        if can_harvest():
            harvest()

# Loop Logics
while True:
    for _ in Location_Range(Max_Location):
        Grass_Harvest()
        Move_Direction(Directions[0])
    Move_Direction(Directions[1])

    for _ in Location_Range(Max_Location):
        Bush_Harvest()
        Move_Direction(Directions[0])
        # plant(Entities_Types[0])
        # if can_harvest():
        #     harvest()
        # elif get_entity_type() != Entities_Types[0]:
        #     plant(Entities_Types[0])
    Move_Direction(Directions[1])

    for _ in Location_Range(Max_Location):
        Carrot_Harvest()
        Move_Direction(Directions[0])
        # if get_entity_type() != Entities_Types[1]:
        #     till()
        #     plant(Entities_Types[1])
        # elif get_entity_type() == Entities_Types[1]:
        #     if can_harvest():
        #         harvest()
    Move_Direction(Directions[1])
