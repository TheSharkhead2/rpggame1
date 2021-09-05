import random
import time
import dictionary as d
import math
from os import system, name
import WeaponExtras as we
import ArmorExtras as ae
import termios, fcntl, sys, os


def split_listto9(list, index, final_list={}):
    
    if len(list) <= 9:
        final_list[index] = list 
        return(final_list)
    else:
        final_list[index] = list[0:9]
        return(split_listto9(list[9:], (index + 1), final_list))


def get_user_index_inventory(list, index=0):
    list_index = 1
    for item in list[index]:
        print(str(list_index) + ':')
        print_loot(item)
        list_index += 1
    print("(-/+ to navigate pages)")
    takeallinput()    
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
    
    if input == '+':
        try:
            return(get_user_index_inventory(list, index + 1))
        except:
            print("Invalid Input")
            return(get_user_index_inventory(list))
    elif input == '-':
        try:
            return(get_user_index_inventory(list, index - 1))
        except:
            print("Invalid Input")
            
            return(get_user_index_inventory(list))
    else:
        try:
            if int(input) + index <= (len(list[index])) and int(input) != 0 and input != '-':

                return(int(input) - 1 + index)
            else:
                print("Invalid Input")
                return(get_user_index_inventory(list))
        except:
            print("Invalid Input")
            return(get_user_index_inventory(list))
    return(1)
    

def get_item_upgrade_cost(item, tolevel):
    if item.gear == 'weapon':
        return(((tolevel * 13 * item.level * d.blacksmith_type_modifiers[item.type]), (tolevel * 18 * item.level * d.blacksmith_type_modifiers[item.type]), (tolevel * 2 * item.level * d.blacksmith_type_modifiers[item.type]), (tolevel * 2 * item.level * d.blacksmith_type_modifiers[item.type])))
    else:
        return(((tolevel * 2 * item.level * d.blacksmith_type_modifiers[item.type]), (tolevel * 11 * item.level * d.blacksmith_type_modifiers[item.type]), (tolevel * 18 * item.level * d.blacksmith_type_modifiers[item.type]), (tolevel * 3 * item.level * d.blacksmith_type_modifiers[item.type])))

def get_sell_return(item):
    return(item.level * 18 * d.blacksmith_type_modifiers[item.type])

def get_dismantle_return(item):
    if item.gear == 'weapon':
        return(((item.level * 10 * d.blacksmith_type_modifiers[item.type]), (item.level * 13 * d.blacksmith_type_modifiers[item.type]), (item.level * 1 * d.blacksmith_type_modifiers[item.type])))
    else:
        return(((item.level * 1 * d.blacksmith_type_modifiers[item.type]), (item.level * 8 * d.blacksmith_type_modifiers[item.type]), (item.level * 13 * d.blacksmith_type_modifiers[item.type])))

def rounddown(x):
    return int(math.floor(x / 10.0)) * 10

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def print_loot(loot):
    if loot.gear == 'weapon':
        we.weaponprint(loot)
    elif loot.gear in ['helmet', 'arms', 'chest', 'leggings', 'boots']:
        ae.armorprint(loot)

def takeallinput():
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    try:
        while 1:
            try:
                c = sys.stdin.read(1)
            except IOError:
                return None
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
