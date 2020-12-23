import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Unit:
    def __init__(self, name, hp, mp, atk, spd, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk = atk
        self.maxspd = spd
        self.spd = 0
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def menu_name_string(self):
        if len(self.name) > 10:
            return self.name[0:10]
        else:
            i = 0
            space = ""
            while i < 10 - len(self.name):
                space += " "
                i += 1
            return self.name + space

    def generate_damage(self):
        crit_mod = 1
        if random.randrange(1,101) <= round((100 - self.maxspd)/2, 0):
            crit_mod = 2
            print(bcolors.FAIL + bcolors.BOLD + '\nCRITICAL!' + bcolors.ENDC)
        low = round(self.atk*0.95*crit_mod, 0)
        high = round(self.atk*1.05*crit_mod, 0)
        return random.randrange(low, high)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
    
    def heal(self, dmg):
        self.hp += dmg
        if self.hp> self.maxhp:
            self.hp = self.maxhp
        
    def manipulate_mp(self, mp):
        self.mp += mp
        if self.mp > self.maxmp:
            self.mp = self.maxmp
    
    def choose_action(self):
        i, valid = 1, []
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for action in self.actions:
            print(f'   {str(i)}. {action}')
            valid.append(str(i))
            i += 1
        choice = input("Choose action: ")
        if choice not in valid:
            print("Not a valid choice. Please try again.")
            choice = self.choose_action() + 1
        return int(choice) - 1
    
    def choose_target(self, targets):
        i, valid = 1, []
        print("\n" + bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for target in targets:
            print(f'   {str(i)}. {target.name}')
            valid.append(str(i))
            i += 1
        print(f'   {str(i)}. --- Back')
        choice = input("Choose target: ")
        if choice == str(i):
            return 'back'
        elif choice not in valid:
            print("Not a valid choice. Please try again.")
            choice = self.choose_target(targets)
            if choice == 'back':
                return 'back'
            else:
                choice = int(choice) + 1
        return int(choice) - 1

    def choose_magic(self):
        i, valid = 1, []
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for magic in self.magic:
            j = ""
            while len(j) + len(magic.name) != 15:
                j += " "
            print(f'   {str(i)}. {magic.name}  {j}> MP cost: {str(magic.cost)}')
            valid.append(str(i))
            i += 1
        print(f'   {str(i)}. --- Back')
        choice = input("Choose magic: ")
        if choice == str(i):
            return 'back'
        elif choice not in valid:
            print("Not a valid choice. Please try again.")
            choice = self.choose_magic()
            if choice == 'back':
                return 'back'
            else:
                choice = int(choice) + 1
        elif self.magic[int(choice) - 1].cost > self.mp:
            print("Not enough MP")
            choice = self.choose_magic()
            if choice == 'back':
                return 'back'
            else:
                choice = int(choice) + 1
        return int(choice) - 1
            
    def choose_item(self):
        i, valid = 1, []
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print(f'   {str(i)}. {item["item"].name}: {item["item"].description}, (x{str(item["quantity"])})')
            valid.append(str(i))
            i += 1
        print(f'   {str(i)}. --- Back')
        choice = input("Choose item: ")
        if choice == str(i):
            return 'back'
        elif choice not in valid:
            print("Not a valid choice. Please try again.")
            choice = self.choose_item()
            if choice == 'back':
                return 'back'
            else:
                choice = int(choice) + 1
        return int(choice) - 1    

    def choose_enemy_magic(self):
        magic_choice = random.randrange(0, len(self.magic))
        magic = self.magic[magic_choice]
        hp_pct = self.hp / self.maxhp * 100
        if self.mp < magic.cost or magic.type == "heal" and hp_pct > 15:
            magic = self.choose_enemy_magic()
        return magic
    
    def banner(self, players, enemies):
        print("\n\n" + bcolors.BOLD +
            "PARTY            ATB                         HP                                      MP" + bcolors.ENDC)
        print("______________________________________________________________________________________________")
        for player in players:
            player.get_stats()
        print("\n\n")
        print(bcolors.BOLD +
            "ENEMY PARTY      ATB                       HP" + bcolors.ENDC)
        print("______________________________________________________________________________________________") 
        for enemy in enemies:
            enemy.get_enemy_stats()  

    def get_stats(self):
        spd_bar = ""
        spd_bar_ticks = (self.spd / self.maxspd) * 100 / 10        
                
        hp_bar = ""
        hp_bar_ticks = (self.hp / self.maxhp) * 100 / 4
        
        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10
        
        while spd_bar_ticks > 0:
            spd_bar += "█"
            spd_bar_ticks -= 1
        while len(spd_bar) < 10:
            spd_bar += " "        
        
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "
        
        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "  
        
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)            
            while decreased > 0:
                current_hp += " "
                decreased -= 1            
            current_hp += hp_string
        else:
            current_hp = hp_string
        
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""
        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)            
            while decreased > 0:
                current_mp += " "
                decreased -= 1            
            current_mp += mp_string
        else:
            current_mp = mp_string            
        
        print("                 __________                 _________________________               __________")
        print(bcolors.BOLD + self.menu_name_string() + "      |" +
              bcolors.OKBLUE + spd_bar + bcolors.ENDC + "|     " +
              current_hp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|     " + 
              current_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
    
    def get_enemy_stats(self):
        spd_bar = ""
        spd_bar_ticks = (self.spd / self.maxspd) * 100 / 10   
        
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2
        
        while spd_bar_ticks > 0:
            spd_bar += "█"
            spd_bar_ticks -= 1
        while len(spd_bar) < 10:
            spd_bar += " "  

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)            
            while decreased > 0:
                current_hp += " "
                decreased -= 1            
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                 __________                 __________________________________________________")
        print(bcolors.BOLD + self.menu_name_string() + "      |" +
              bcolors.OKBLUE + spd_bar + bcolors.ENDC + "|   " +
              current_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|") 
