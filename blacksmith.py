import dictionary as d 
import classes as c 
import random
import time 
from datetime import datetime
import functions as f
import termios, fcntl, sys, os
import WeaponExtras as we
import ArmorExtras as ae

class Blacksmith: 
    def calculate_armor_price(self, item):
        base = item.level * item.armor * (self.player_heat/1)
        return(int(base * d.blacksmith_type_modifiers[item.type]))
    def calculate_weapon_price(self, item):
        base = item.level * item.damage * (self.player_heat/1)
        return(int((base * d.blacksmith_type_modifiers[item.type])/9))

    def generate_selling_items(self, player_level):
        self.woodstock = int((random.randrange(30, 100) * (1 - (self.player_heat/10))))
        self.metalstock = int((random.randrange(30, 100) * (1 - (self.player_heat/10))))
        self.leatherstock = int((random.randrange(30, 100) * (1 - (self.player_heat/10))))
        self.woodstock_price = self.woodstock * 2 
        self.metalstock_price = self.metalstock * 2 
        self.leatherstock_price = self.leatherstock * 2
        self.itemstock = []
        self.possibleweapons = [c.Sword.sword_gen(player_level), c.Dagger.dagger_gen(player_level), c.Mace.mace_gen(player_level), c.Club.club_gen(player_level), c.Spear.spear_gen(player_level), c.Frying_Pan.fryingpan_gen(player_level), c.Axe.axe_gen(player_level), c.Heavy_Blunt.heavyblunt_gen(player_level)]
        weapon = random.choice(self.possibleweapons)
        self.itemstock.append((weapon, self.calculate_weapon_price(weapon)))
        helmet = c.Helmet.helmet_gen(1)
        self.itemstock.append((helmet, self.calculate_armor_price(helmet)))
        chest = c.Chest.chest_gen(1)
        self.itemstock.append((chest, self.calculate_armor_price(chest)))
        arms = c.Arms.arms_gen(1)
        self.itemstock.append((arms, self.calculate_armor_price(arms)))
        legs = c.Leggings.leggings_gen(1)
        self.itemstock.append((legs, self.calculate_armor_price(legs)))
        boots = c.Boots.boots_gen(1)
        self.itemstock.append((boots, self.calculate_armor_price(boots)))
        self.last_stock_gen = datetime.today()

    def upgrade_items(self, player): 
        f.clear()
        print("Now which one is it?! ('X' to exit)")
        print("""
1. Helmets 
2. Chests 
3. Arms 
4. Leggings
5. Boots
6. Weapon
        """)
        f.takeallinput()    
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            inputing = True
            while inputing:
                try:
                    c = sys.stdin.read(1)
                    input = c
                    inputing = False
                except IOError: pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        if input in ['1', '!']:
            printable_list = f.split_listto9(player.helmetinventory, 0)
            item = player.helmetinventory[f.get_user_index_inventory(printable_list)]

        elif input in ['2', '@']:
            printable_list = f.split_listto9(player.chestinventory, 0)
            item = player.chestinventory[f.get_user_index_inventory(printable_list)]

        elif input in ['3', '#']:
            printable_list = f.split_listto9(player.armsinventory, 0)
            item = player.armsinventory[f.get_user_index_inventory(printable_list)]

        elif input in ['4', '$']:
            printable_list = f.split_listto9(player.leggingsinventory, 0)
            item = player.leggingsinventory[f.get_user_index_inventory(printable_list)]

        elif input in ['5', '%']:
            printable_list = f.split_listto9(player.bootsinventory, 0)
            item = player.bootsinventory[f.get_user_index_inventory(printable_list)]

        elif input in ['6', '^']:
            printable_list = f.split_listto9(player.weaponinventory, 0)
            item = player.weaponinventory[f.get_user_index_inventory(printable_list)]

        elif input in ['X', 'x']:
            return(False)
        else:
            return(False)
        
        if item.level >= player.level:
            print("You can't upgrade that...")
            time.sleep(1)
            return(False)
        print("You want to upgrade:")
        f.print_loot(item)
        cost = f.get_item_upgrade_cost(item, player.level - item.level)
        print("That will cost you {} wood, {} metal, {} leather, and {} coins!".format(cost[0], cost[1], cost[2], cost[3]))
        print("Are you sure 'y/n'")
        f.takeallinput()    
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            inputing = True
            while inputing:
                try:
                    c = sys.stdin.read(1)
                    input = c
                    inputing = False
                except IOError: pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        if input in ['y', 'Y']:
            if player.woodstock - cost[0] >= 0 and player.metalstock - cost[1] >= 0 and player.leatherstock - cost[2] >= 0 and player.coins - cost[3] >= 0:
                player.woodstock -= cost[0]
                player.metalstock -= cost[1]
                player.leatherstock -= cost[2]
                player.coins -= cost[3]
                if item.gear == 'weapon':
                    item.level = player.level
                    item.damage = we.weaponmakedamage(item.level, item.type)
                else:
                    item.level = player.level
                    item.armor = ae.makearmor(item.level, item.type)
                return(True)
            else:
                print("Not enough reasources!")
                time.sleep(1)
                return(False)
        else:
            return(False)


    def store(self, player_heat, player_level, player):
        f.clear()
        itemnumber = 1
        for item in self.itemstock: 
            print(str(itemnumber) + ':')
            f.print_loot(item[0])
            itemnumber += 1
            print("Price: " + d.color.YELLOW + str(item[1]) + d.color.END + " coins")
            print("\n")
        
        print("7:")
        print(d.color.BOLD + str(self.woodstock) + d.color.END + " Wood")
        print("Price: " + d.color.YELLOW + str(self.woodstock_price) + d.color.END + " coins")
        print("\n")
        print("8:")
        print(d.color.BOLD + str(self.metalstock) + d.color.END + " Metal")
        print("Price: " + d.color.YELLOW + str(self.metalstock_price) + d.color.END + " coins")
        print("\n")
        print("9:")
        print(d.color.BOLD + str(self.leatherstock) + d.color.END + " Leather")
        print("Price: " + d.color.YELLOW + str(self.leatherstock_price) + d.color.END + " coins")
        print("\n")
        print("Your such a pain! Which item?! ('X' to exit)")
        f.takeallinput()    
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            inputing = True
            while inputing:
                try:
                    c = sys.stdin.read(1)
                    input = c
                    inputing = False
                except IOError: pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

        if input in ["X", 'x']:
            return(False)
        elif input in ['7', '8', '9', '&', '*', '(']:
            if input in ['7', '&']:
                if not player.buy_material('Wood', self.woodstock_price, self.woodstock):
                    print("Not Enough Coins!")
                    return(False)
                else:
                    print("You bought {} wood for {} coins!".format(str(self.woodstock), d.color.YELLOW + str(self.woodstock_price) + d.color.END))
                    self.woodstock = 0
                    self.woodstock_price = 0
            elif input in ['8', '*']:
                if not player.buy_material('Metal', self.metalstock_price, self.metalstock):
                    print("Not Enough Coins!")
                    return(False)
                else:
                    print("You bought {} metal for {} coins!".format(str(self.metalstock), d.color.YELLOW + str(self.metalstock_price) + d.color.END))
                    self.metalstock = 0
                    self.metalstock_price = 0
            elif input in ['9', '(']:
                if not player.buy_material('Leather', self.leatherstock_price, self.leatherstock):
                    print("Not Enough Coins!")
                    return(False)
                else:
                    print("You bought {} leather for {} coins!".format(str(self.leatherstock), d.color.YELLOW + str(self.leatherstock_price) + d.color.END))
                    self.leatherstock = 0
                    self.leatherstock_price = 0
        else:
            try: 
                item = self.itemstock[int(input) - 1]
                if not player.buy_item(item):
                    print("Not Enough Coins!")
                    return(False)
                else:
                    print("You bought a {} for {} coins!".format(item[0].name, d.color.YELLOW + str(item[1]) + d.color.END))
                    self.itemstock.pop(int(input) - 1)
                    return(True)
            except: 
                print("Invalid Input!") 
                return(False)

    def interact(self, player):
        self.player_heat = player.heat
        if (datetime.today() - self.last_stock_gen).seconds > 500:
            self.generate_selling_items(player.level)
        print(d.color.BOLD + "Blacksmith \n" + d.color.END)
        time.sleep(0.5)
        print("Blacksmith: What do YOU want!?")
        time.sleep(0.5)
        print("Blacksmith: " + random.choice(d.blacksmith_rfbm))
        time.sleep(0.5)
        print(
        """
1. Buy Items 
2. Upgrade Items 
3. Sell Items 
('X' to exit)

        """
        )
        f.takeallinput()    
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            inputing = True
            while inputing:
                try:
                    c = sys.stdin.read(1)
                    input = c
                    inputing = False
                except IOError: pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        if input in ['1', '!']:
            self.store(player.heat, player.level, player)
        elif input in ['2', '@']:
            self.upgrade_items(player)
        elif input in ['3', '#']:
            f.clear()
            print("""
Choose item to sell:
1. Helmets 
2. Chests 
3. Arms 
4. Leggings
5. Boots
6. Weapon
('X' to exit)
        """)
            f.takeallinput()    
            fd = sys.stdin.fileno()
            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
            try:
                inputing = True
                while inputing:
                    try:
                        c = sys.stdin.read(1)
                        input = c
                        inputing = False
                    except IOError: pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
            
            if input in ['1', '!']:
                printable_list = f.split_listto9(player.helmetinventory, 0)
                index = f.get_user_index_inventory(printable_list)
                item = player.helmetinventory[index]
                
            elif input in ['2', '@']:
                printable_list = f.split_listto9(player.chestinventory, 0)
                index = f.get_user_index_inventory(printable_list)
                item = player.chestinventory[index]

            elif input in ['3', '#']:
                printable_list = f.split_listto9(player.armsinventory, 0)
                index = f.get_user_index_inventory(printable_list)
                item = player.armsinventory[index]

            elif input in ['4', '$']:
                printable_list = f.split_listto9(player.leggingsinventory, 0)
                index = f.get_user_index_inventory(printable_list)
                item = player.leggingsinventory[index]

            elif input in ['5', '%']:
                printable_list = f.split_listto9(player.bootsinventory, 0)
                index = f.get_user_index_inventory(printable_list)
                item = player.bootsinventory[index]

            elif input in ['6', '^']:
                printable_list = f.split_listto9(player.weaponinventory, 0)
                index = f.get_user_index_inventory(printable_list)
                item = player.weaponinventory[index]
            elif input in ['X', 'x']:
                return(False)
            else:
                print("Invalid Input!")
                return(False)
            print("\nAre you sure you want to sell:")
            f.print_loot(item)
            print("y/n?")
            f.takeallinput()    
            fd = sys.stdin.fileno()
            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
            try:
                inputing = True
                while inputing:
                    try:
                        c = sys.stdin.read(1)
                        input = c
                        inputing = False
                    except IOError: pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

        if input in ['Y', 'y']:
            if item.gear == 'weapon' and player.weapon != item:
                player.weaponinventory.pop(index)
                sell_return = f.get_sell_return(item)
            elif item.gear == 'helmet' and player.helmet != item:
                player.helmetinventory.pop(index)
                sell_return = f.get_sell_return(item)
            elif item.gear == 'chest' and player.chest != item:
                player.chestinventory.pop(index)
                sell_return = f.get_sell_return(item)
            elif item.gear == 'arms' and player.arms != item:
                player.armsinventory.pop(index)
                sell_return = f.get_sell_return(item)
            elif item.gear == 'leggings' and player.leggings != item:
                player.leggingsinventory.pop(index)
                sell_return = f.get_sell_return(item)
            elif item.gear == 'boots' and player.boots != item:
                player.bootsinventory.pop(index)
                sell_return = f.get_sell_return(item)
            else:
                print("You can't sell something you have equipped!")
                time.sleep(1)
                return(False)
            print("You got {} coins from selling that item".format(sell_return))
            player.coins += sell_return
            time.sleep(1)
        else:
            return(False)
            
        

        
        

    def __init__(self, player):
        self.player_heat = player.heat
        self.generate_selling_items(player.level)
        


