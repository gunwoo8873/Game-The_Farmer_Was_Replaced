from __builtins__ import *

# Items
# Hay = Entities.Hay
Bush = Entities.Bush
Carrot = Entities.Carrot

#Default Options
Harvest = False
Grassland = True


# Logic

def move_direction(n, dir):
	for i in range(n):
		move(dir)

def Harvest_loop():
	harvest()

def Changed_Grassland(v):
	plant(v)

while True:
	if Harvest:
		Harvest_loop()
	if Grassland:
		Changed_Grassland(Grassland)
