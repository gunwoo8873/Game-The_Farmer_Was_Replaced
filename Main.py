from __builtins__ import *

#########################################
# Current Ground Size : 4 * 4
#########################################

# Items <Entities.SeedName>
Bush = Entities.Bush
Carrot = Entities.Carrot
SeedTypes = [Bush, Carrot]

# Directions <0=N, 1=E, 2=S, 3=W>
Directions = [North, East, South, West]

# Functions
def move_direction(dir):
    return move(dir)

def range_check(v):
    return range(v)

def Locaition_check(x, y):
    return get_pos_x() == x and get_pos_y() == y

def Bush_Tared():
    return plant(SeedTypes[0])

def Carrot_Tared():
    return till(), plant(SeedTypes[1])

# Loop Logic
while True:
    for _ in range_check(4):
        move_direction(Directions[0])
        harvest()
    move_direction(Directions[1])

    for _ in range_check(4):
        move_direction(Directions[0])
        Bush_Tared()
        
        if can_harvest():
            harvest()
    move_direction(Directions[1])

    for _ in range_check(4):
        move_direction(Directions[0])
        Carrot_Tared()
        
        if can_harvest():
            harvest()
    move_direction(Directions[1])
