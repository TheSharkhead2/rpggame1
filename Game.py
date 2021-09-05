import fight as fi
import classes as c
import time
import functions as f
import dictionary
import Location
import termios, fcntl, sys, os
import random

def game_loop(player, location, blacksmith):
    if location.original_quest_value == None:
        if location.quest_type == 'coins':
            location.original_quest_value = player.coins
    f.clear()
    print(dictionary.color.BOLD + location.name + dictionary.color.END)
    print("   Coins: {}      Level: {}      ".format(player.coins, player.level))
    print("\n")
    player.print_heat()
    print("\n")
    location.print_quest_percent(player)
    print("""
    What would you like to do? 
    1. Fight a Mercenary
    2. Blacksmith 
    3. Your Inventory
    4. Wait
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
        loot = fi.mercenary_fight(player, player.level)
        if player.dead == False:
            player.addxp(loot[1] * 300)
            player.adrenaline = 100
            player.health = player.getmaxhealth()
            player.coins += 50 * loot[1]
            player.killed_mercenaries += 1
            if random.randrange(0, 5) > 2:
                player.heat += 1
            print("You found a:")
            f.print_loot(loot[0])
            if loot[0].gear == 'weapon':
                player.addweaponinventory([loot[0]])
            elif loot[0].gear == 'helmet':
                player.addhelmetinventory([loot[0]])
            elif loot[0].gear == 'chest':
                player.addchestinventory([loot[0]])
            elif loot[0].gear == 'arms':
                player.addarmsinventory([loot[0]])
            elif loot[0].gear == 'leggings':
                player.addleggingsinventory([loot[0]])
            elif loot[0].gear == 'boots':
                player.addbootsinventory([loot[0]])
            time.sleep(3)
        else:
            return(False)

    elif input in ['2','@']:
        blacksmith.interact(player)
    elif input in ['3', '#']:
        f.clear()
        print(dictionary.color.BOLD + "Inventory" + dictionary.color.END + '\n')
        print("   Coins: {}      Wood: {}      Metal: {}      Leather: {}".format(player.coins, player.woodstock, player.metalstock, player.leatherstock))
        print("""
Choose item to interact with:
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
            game_loop(player, location, blacksmith)
        else:
            print("Invalid Input!")
            game_loop(player, location, blacksmith)
        print("\nWhat do you want to do with:")
        f.print_loot(item)
        print("""
1. Dismantle
2. Equip
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
            if item.gear == 'weapon' and player.weapon != item:
                player.weaponinventory.pop(index)
                dismantle_return = f.get_dismantle_return(item)
            elif item.gear == 'helmet' and player.helmet != item:
                player.helmetinventory.pop(index)
                dismantle_return = f.get_dismantle_return(item)
            elif item.gear == 'chest' and player.chest != item:
                player.chestinventory.pop(index)
                dismantle_return = f.get_dismantle_return(item)
            elif item.gear == 'arms' and player.arms != item:
                player.armsinventory.pop(index)
                dismantle_return = f.get_dismantle_return(item)
            elif item.gear == 'leggings' and player.leggings != item:
                player.leggingsinventory.pop(index)
                dismantle_return = f.get_dismantle_return(item)
            elif item.gear == 'boots' and player.boots != item:
                player.bootsinventory.pop(index)
                dismantle_return = f.get_dismantle_return(item)
            else:
                print("You can't dismantle something you have equipped!")
                time.sleep(1)
                game_loop(player, location, blacksmith)
            print("You got {} wood, {} metal, and {} leather from dismantling that item!".format(dismantle_return[0], dismantle_return[1], dismantle_return[2]))
            player.woodstock += dismantle_return[0]
            player.metalstock += dismantle_return[1]
            player.leatherstock += dismantle_return[2]
            time.sleep(1)

        elif input in ['2', '@']:
            if item.gear == 'weapon' and player.weapon != item:
                player.weapon = item
            elif item.gear == 'helmet' and player.helmet != item:
                player.helmet = item
            elif item.gear == 'chest' and player.chest != item:
                player.chest = item
            elif item.gear == 'arms' and player.arms != item:
                player.arms = item
            elif item.gear == 'leggings' and player.leggings != item:
                player.leggings = item
            elif item.gear == 'boots' and player.boots != item:
                player.boots = item
            else:
                print("You can't equip something you have equipped!")
                game_loop(player, location, blacksmith) 
            print()
        elif input in ['X', 'x']:
            game_loop(player, location, blacksmith)
        else:
            print("Invalid Input!")
            game_loop(player, location, blacksmith)

       

    elif input in ['4', '$']:
        if player.heat <= 2:
            print("Your heat is too low to need to wait out a turn.")
            time.sleep(2)
        else:
            print("Waiting will cost you {} coins but reduce your heat by 20%".format(player.get_wait_cost()) )
            print("Are you sure you want to wait? (y/n)")
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
                if player.coins - player.get_wait_cost() >= 0:
                    player.coins -= player.get_wait_cost()
                    player.heat -= 2 
                    game_loop(player, location, blacksmith)
                else:
                    print("Not Enough Coins!")
            else:
                print("Cancling Action")
    if location.get_next_location(player) == False:

        game_loop(player, location, blacksmith)
    
    else:
        game_loop(player, location.get_next_location(player), blacksmith)