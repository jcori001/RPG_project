import random
from classes.game import bcolors


class Magic:
    def __init__(self, name, cost, dmg, crit, spd_dmg, typ):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.crit = crit
        self.spd_dmg = spd_dmg
        self.type = typ
        
    def generate_damage(self):
        crit_mod = 1
        if random.randrange(1,101) <= self.crit:
            crit_mod = 1.5
            print(bcolors.FAIL + bcolors.BOLD + '\nCRITICAL!' + bcolors.ENDC)
        low = round(self.dmg*0.95*crit_mod, 0)
        high = round(self.dmg*1.05*crit_mod, 0)
        return random.randrange(low, high)
    
    
# Create Offensive Magic

# (
#  name, 
#  cost, dmg, crit, spd_dmg, 
#  typ

fire_1 = Magic(
    "Fire", 
    30, 250, 5, 0, 
    "dmg")
thunder_1 = Magic(
    "Thunder", 
    30, 225, 33, 0, 
    "dmg")
blizzard_1 = Magic(
    "Blizzard", 
    30, 200, 2.5, 25, 
    "dmg")
chaos = Magic(
    "Chaos", 
    70, 550, 0, 0, 
    "dmg")

quake = Magic(
    "Quake", 
    50, 200, 0, 15, 
    "aoe")
meteor = Magic(
    "Meteor", 
    80, 400, 5, 0, 
    "aoe")


# Create Defensive Magic

# (
#  name, 
#  cost, dmg, crit, spd_dmg, 
#  typ

cure_1 = Magic(
    "Cure", 
    15, 250, 0, 0, 
    "heal")
cure_2 = Magic(
    "Cure 2", 
    50, 600, 0, 0, 
    "heal")
revive = Magic(
    "Revive", 
    50, 9999, 0, 0, 
    "res")
