"""
This is the dev version for the fighting mechanics in this game.
THis is the main file which should be run inside terminal through
python 2.7. All of the modules being used in this game should be
                already installed with python 2.
"""

import fight as fi
import classes as c
import time
import functions as f
import Game
import os
import Perks as p
import blacksmith
import Location
f.clear()

def dev_build_fight():
    menu = """
                  Welcome to the dev build for the fighting mechanics!
        Please remember there will be numerous glitches and bugs in this version
    """
    time.sleep(0.5)
    print(menu)
    f.takeallinput()
    player = c.Person(raw_input("Name? "))
    helmet1 = c.Helmet.helmet_gen(1)
    chest1 = c.Chest.chest_gen(1)
    arms1 = c.Arms.arms_gen(1)
    leggings1 = c.Leggings.leggings_gen(1)
    boots1 = c.Boots.boots_gen(1)
    player.equip_helmet(helmet1)
    player.equip_arms(arms1)
    player.equip_chest(chest1)
    player.equip_leggings(leggings1)
    player.equip_boots(boots1)
    player.gethelmetinventory()
    player.getarmsinventory()
    player.getchestinventory()
    player.getleggingsinventory()
    player.getbootsinventory()
    loot = c.Sword.sword_gen(1)
    player.equip_weapon(loot)
    player.getweaponinventory()

    fi.mercenary_fight(player, 1)

# dev_build_fight()

def dev_build_gameLoop():
    menu = """
                  Welcome to this mostly-complete RPG game that has no name! 
                Type your name to start. You have a few goals to complete... 
    """
    time.sleep(0.5)
    print(menu)
    f.takeallinput()
    player = c.Person(raw_input("Name? "))
    helmet1 = c.Helmet("Rusty Bucket", 1, "Common", 4, p.Perks(1, "Common"))
    chest1 = c.Chest("Leather Tunic", 1, "Common", 3, p.Perks(1, "Common"))
    arms1 = c.Arms("Mechanic Gloves", 1, "Common", 3, p.Perks(1, "Common"))
    leggings1 = c.Leggings("Baggy Pants", 1, "Legendary", 13, p.Perks(1, "Legendary"))
    boots1 = c.Boots("Dirty Boots", 1, "Common", 4, p.Perks(1, "Common"))
    player.equip_helmet(helmet1)
    player.equip_arms(arms1)
    player.equip_chest(chest1)
    player.equip_leggings(leggings1)
    player.equip_boots(boots1)
    player.equip_weapon(c.Sword(1, "Three Pronged Stick", "Legendary", p.Perks(1, "Legendary"), 65))
   
    
    
    Game.game_loop(player, Location.Location("Athens", "Kill 2 Mercenaries", "mercenary", player.killed_mercenaries, 2, Location.Location("Babylon", "Get 200 coins", "coins", None, 200, None)), blacksmith.Blacksmith(player))
dev_build_gameLoop()


