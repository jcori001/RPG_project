from classes.character_list import *
from colorama import init
init() #ANSI coloring support on cmd.exe


'''
NOTES:
-enemies are hard coded to have x3 magnitude heal
-res is hard coded to work with revive only

Possible Upgrades
-define crit roll method under class to delete repetetive dmg calculations
-use defense and magic defense math to reduce dmg
-enable speed damage through magic, elemental weakness
-create special attacks
-add flavor text for out of items
-import characters/magics from csv/excel reads
'''


players = [mage, tank, fighter]
enemies = [enemy2, enemy1, enemy3]
fainted = []

running = True
i = 0

print("\n" + bcolors.FAIL + bcolors.BOLD + "AN EMENY ATTACKS!" + bcolors.ENDC)
print("=============================================================================")


while running:
    for unit in players + enemies: 
        if unit.spd == unit.maxspd and unit.hp > 0:
            input("\nPress enter to continue...")
            
            #turn start stat changes
            unit.manipulate_mp(int(round(unit.maxmp*0.05, 0)))
            #print status banner
            unit.banner(players, enemies)  
            #reset unit ATB after print
            unit.spd = 0
            
            if unit in players:
                #run player loop
                player_turn = True
                if unit.mp < unit.maxmp:
                    print(bcolors.OKBLUE + f'\n\n{unit.name} charged {int(round(unit.maxmp*0.05, 0))} MP.' + bcolors.ENDC)
                
                while player_turn == True:
                    back = False
                    index = unit.choose_action()
                    
                    if index == 0:
                        enemy = unit.choose_target(enemies)
                        if enemy == 'back':
                            continue
                        dmg = unit.generate_damage()           
                        enemies[enemy].take_damage(dmg)
                        
                        print(bcolors.BOLD + f'\n{unit.name} attacked {enemies[enemy].name} for {dmg} points of damage.' + bcolors.ENDC)
                    
                    elif index == 1:
                        magic_loop = True
                        while magic_loop == True:
                            magic_choice = unit.choose_magic()
                            if magic_choice == 'back':
                                back = True
                                break
                            magic = unit.magic[magic_choice]                 
                            unit.manipulate_mp(-magic.cost)
                        
                            if magic.type == "heal":
                                heal_target = unit.choose_target(players)
                                if heal_target == 'back':
                                    continue
                                print(f'\n{unit.name} casts {magic.name}...')
                                magic_dmg = magic.generate_damage()  
                                players[heal_target].heal(magic_dmg)
                                print(bcolors.OKGREEN + f'{magic.name} heals {players[heal_target].name} for {str(magic_dmg)} HP.' + bcolors.ENDC) 
                            elif magic.type == "dmg":
                                enemy = unit.choose_target(enemies)
                                if enemy == 'back':
                                    continue
                                print(f'\n{unit.name} casts {magic.name}...')
                                magic_dmg = magic.generate_damage()            
                                enemies[enemy].take_damage(magic_dmg)
                                print(bcolors.OKBLUE + f'{magic.name} deals {str(magic_dmg)} points of damage to {enemies[enemy].name}.' + bcolors.ENDC)
                            elif magic.type == 'aoe':
                                print(f'\n{unit.name} casts {magic.name}...')
                                magic_dmg = magic.generate_damage() 
                                for enemy in enemies:
                                    enemy.take_damage(magic_dmg)
                                print(bcolors.OKBLUE + f'{magic.name} deals {str(magic_dmg)} points of damage to all enemies.' + bcolors.ENDC)
                            elif magic.type == 'res':
                                if not fainted:
                                    print("There are no fainted allies to revive")
                                    continue
                                else:
                                    res_target = unit.choose_target(fainted)
                                    if res_target == 'back':
                                        continue
                                    print(f'\n{unit.name} used {magic.name}...')
                                    print(bcolors.OKGREEN + f'{fainted[res_target].name} has risen from near death!' + bcolors.ENDC)
                                    fainted[res_target].hp = int(round(fainted[res_target].maxhp/2, 0))
                                    fainted.pop(res_target)
                            magic_loop = False

                    elif index == 2:
                        item_loop = True
                        while item_loop == True:
                            item_choice = unit.choose_item()
                            if item_choice == 'back':
                                back = True
                                break
                            unit.items[item_choice]["quantity"] -= 1
                            item = unit.items[item_choice]["item"]
                            if unit.items[item_choice]["quantity"] == 0:
                                unit.items.pop(item_choice)
                        
                            if item.type == "potion":
                                potion_target = unit.choose_target(players)
                                if potion_target == 'back':
                                    continue
                                players[potion_target].heal(item.properties)
                                print(f'\n{unit.name} used {item.name}...')
                                print(bcolors.OKGREEN + f'{item.name} heals {players[potion_target].name} for {str(item.properties)} HP.' + bcolors.ENDC)
                            elif item.type == "elixir":
                                if item.name == "megaelixir":
                                    for player in players:
                                        player.hp = unit.maxhp
                                        player.mp = unit.maxmp
                                    print(f'\n{unit.name} used {item.name}...')
                                    print(bcolors.OKGREEN + f'{item.name} fully restores HP/MP to all party members.' + bcolors.ENDC)
                                else:
                                    elixir_target = unit.choose_target(players)
                                    if elixir_target == 'back':
                                        continue
                                    players[elixir_target].heal(item.properties)                        
                                    unit.hp = unit.maxhp
                                    unit.mp = unit.maxmp
                                    print(f'\n{unit.name} used {item.name} on {players[elixir_target].name}...')
                                    print(bcolors.OKGREEN + f'{item.name} fully restores HP/MP.' + bcolors.ENDC)
                            elif item.type == "attack":
                                enemy = unit.choose_target(enemies)
                                if enemy == 'back':
                                    continue           
                                enemies[enemy].take_damage(item.properties)
                                print(f'\n{unit.name} used {item.name}...')
                                print(bcolors.FAIL + f'{item.name} deals {str(item.properties)} points of damage to {enemies[enemy].name}.' + bcolors.ENDC)
                            item_loop = False
                    if not back:
                        player_turn = False
          
                #print banner after action and turn ends
                unit.banner(players, enemies)              
                
                #clean up enemy field
                for count, enemy in enumerate(enemies):
                    if enemy.hp == 0:
                        print(f'\n{enemy.name} has died.')
                        enemies.pop(count)
                
                #check if player won
                if not enemies:
                    print(bcolors.OKGREEN + "\nYou win!" + bcolors.ENDC)
                    input("\nPress enter to end the game...")
                    running = False
                else:
                    continue
            
            elif unit in enemies:
                #run enemy loop
                print("\n")
                enemy_choice = random.randrange(0, 2) #no items coded into enemies
                targetable_party = []
                for player in players:
                    if player not in fainted:
                        targetable_party.append(player)
            
                if enemy_choice == 0:
                    target = random.randrange(0, len(targetable_party))
                    enemy_dmg = unit.generate_damage()
                    targetable_party[target].take_damage(enemy_dmg)
                    print(bcolors.FAIL + f'\n{unit.name} attacks {targetable_party[target].name} for {enemy_dmg} points of damage.' + bcolors.ENDC)
                
                elif enemy_choice == 1:
                    magic = unit.choose_enemy_magic()
                    # unit.manipulate_mp(-magic.cost) #mp cost disabled on enemies
                    
                    if magic.type == "heal":
                        print(f'\n{unit.name} casts {magic.name}...')
                        magic_dmg = magic.generate_damage()
                        unit.heal(magic_dmg*3) #set stronger heal for bosses
                        print(bcolors.FAIL + f'{magic.name} heals for {str(magic_dmg)} HP.' + bcolors.ENDC) 
                    elif magic.type == "dmg":
                        target = random.randrange(0, len(targetable_party))
                        print(f'\n{unit.name} casts {magic.name}...')
                        magic_dmg = magic.generate_damage()           
                        targetable_party[target].take_damage(magic_dmg)
                        print(bcolors.FAIL + f'{magic.name} deals {str(magic_dmg)} points of damage to {targetable_party[target].name}.' + bcolors.ENDC)
                    elif magic.type == 'aoe':
                        print(f'\n{unit.name} casts {magic.name}...')
                        magic_dmg = magic.generate_damage()
                        for player in targetable_party:
                            player.take_damage(magic_dmg)
                        print(bcolors.FAIL + f'{magic.name} deals {str(magic_dmg)} points of damage to nearby allies.' + bcolors.ENDC)
                
                #check for fainted players
                for player in players:
                    if player.hp == 0 and player not in fainted:
                        fainted.append(player)
                        player.spd = 0
                        print(f'\n{player.name} has fainted.')           

                #check if enemy won
                if len(fainted) == len(players):
                    #print final banner
                    unit.banner(players, enemies)
                    print (bcolors.FAIL + "\nYour enemies have defeated you!" + bcolors.ENDC)
                    input("\nPress enter to end the game...")
                    running = False

        else:
            if unit.hp > 0:
                unit.spd += 5
            continue
