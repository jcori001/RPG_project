from classes.game import Unit
from classes.magic import *
from classes.inventory import *


# Instantiate Magic lists
bm_trio_1 = [fire_1, thunder_1, blizzard_1]
heal = [cure_1, cure_2] # + revive?
player_inv = [{"item": potion, "quantity": 5}, {"item": elixir, "quantity": 1}, {"item": grenade, "quantity": 3}, {"item": h_bomb, "quantity": 1}]
enemy_spells = [fire_1, meteor, cure_1]


# Instantiate characters (10 character limit on names)

# (
#  name, 
#  hp, mp, atk, spd, 
#  magic, items)

mage = Unit(
    "Mage", 
    1000, 300, 30, 100, 
     bm_trio_1 + [cure_2, meteor], player_inv)
tank = Unit(
    "Tank", 
     1800, 200, 80, 120, 
     heal + [revive, blizzard_1], player_inv)
fighter = Unit(
    "Fighter", 
     1300, 60, 150, 70, 
     [cure_1, quake], player_inv)

enemy1 = Unit(
    "Boss", 
     7000, 300, 400, 125, 
     [chaos, cure_2], [])
enemy2 = Unit(
    "mini boss", 
     900, 100, 250, 80, 
     [meteor], [])
enemy3 = Unit(
    "mini boss", 
     900, 100, 250, 80, 
     [meteor], [])
