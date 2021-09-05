import random
import dictionary as d

class type:
   EPIC = '\033[95m' + '\033[1m'
   RARE = '\033[94m' + '\033[1m'
   UNCOMMON = '\033[92m' + '\033[1m'
   LEGENDARY = '\033[93m' + '\033[1m'
   COMMON = '\033[1m' + '\033[37m'
   END = '\033[0m'

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m' + '\033[37m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Creation

def makearmor(level, type):
    if type == 'Common':
        x = random.randrange((level * 1), (level * 4))
    elif type == 'Uncommon':
        x = random.randrange((level * 3), (level * 6))
    elif type == 'Rare':
        x = random.randrange((level * 5), (level * 8))
    elif type == 'Epic':
        x = random.randrange((level * 8), (level * 12))
    elif type == 'Legendary':
        x = random.randrange((level * 11), (level * 15))
    else:
        x = 1
    return x

def helmetmakename():
    one = d.helm1
    two = d.helm2
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final

def chestmakename():
    one = d.chest1
    two = d.chest2
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final

def armsmakename():
    one = d.arms1
    two = d.arms2
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final

def leggingsmakename():
    one = d.leggings1
    two = d.leggings2
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final

def bootsmakename():
    one = d.boots1
    two = d.boots2
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final

def armormaketype():
    u = random.randrange(1,101)
    if u in range(1, 41):
        return 'Common'
    if u in range(41, 71):
        return 'Uncommon'
    if u in range(71, 87):
        return 'Rare'
    if u in range(87, 99):
        return 'Epic'
    if u in range(99, 101):
        return 'Legendary'

def armorreturnbufftype(type):
    if type == 'Common':
        return None
    if type == 'Uncommon':
        return None
    if type == 'Rare':
        return 1
    if type == 'Epic':
        return 2
    if type == 'Legendary':
        return 2

def armorperkamount():
    #Subject to change with finished player class
    j = random.randrange(5, 11)
    return str(j) + "% "

def armorperkbase():
    f = random.randrange(0, len(d.perks))
    return d.perks[f]

def lenarmorperkamount():
    j = random.randrange(50, 80)
    return str(j) + "% "

def armormakeperks(type):
    final = []
    number = armorreturnbufftype(type)
    if number == None:
        return None
    g = 1
    while g <= number:
        thing = ''
        g += 1
        thing += armorperkamount()
        thing += armorperkbase()
        final.append(thing)
    if type == 'Legendary':
        leng = ''
        leng += lenarmorperkamount()
        leng += armorperkbase()
        final.append(leng)
    return final

#Inventory

def armorprint(armor):
    print color.BOLD + armor.name + color.END
    if armor.type == 'Legendary':
        print '     ' + type.LEGENDARY + armor.type + type.END
    if armor.type == 'Epic':
        print '     ' + type.EPIC + armor.type + type.END
    if armor.type == 'Rare':
        print '     ' + type.RARE + armor.type + type.END
    if armor.type == 'Uncommon':
        print '     ' + type.UNCOMMON + armor.type + type.END
    if armor.type == 'Common':
        print '     ' + type.COMMON + armor.type + type.END
    print '     ' + color.BOLD + str(armor.armor) + color.END + " armor"
    if armor.perks != None:
        if armor.perks.perks != None:
            for x in armor.perks.perks:
                print "         " + x.get_string()
