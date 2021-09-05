import dictionary as d
import monster as m
import random
import time
import functions as f
import curses
import termios, fcntl, sys, os


def mercenary_fight(player, fight_level):
    f.clear()
    mercenary = m.Monster.mercenary_gen(fight_level, player)
    print("You have entered a fight with " + mercenary.name)
    return((fight(mercenary, player), mercenary.level))


def fight(monster, player):
    people = [monster, player]
    random.shuffle(people)
    if player.devmode:
        print("Your Gear: ")
        player.tempprintallgear()
        print("Monster Gear: ")
        monster.tempprintallgear()
        print("\n\n")
    time.sleep(1)
    print("{} goes first!".format(people[0].name))
    while people[0].dead == False and people[1].dead == False:
        for person in people:
            time.sleep(1)
            print(d.color.BOLD + "\nIt is {}'s turn!".format(person.name) + d.color.END)
            person.add_adrenaline(1)
            time.sleep(0.5)
            if person.player == people[0].player:
                otherplayer = people[1]
            elif person.player == people[1].player:
                otherplayer = people[0]
            else:
                raise Exception("There was a failure in the process of determining the other player on {}'s turn".format(person.name))
            if person.temponfire:
                person.tempfiretime -= 1
                print("{} is still on fire!".format(person.name))
                person.take_battledamage(person.tempfiredamage)
                if person.tempfiretime <= 0:
                    person.temponfire = False
                    person.tempfiredamage = None
            if person.tempstun:
                print("{} is stunned!".format(person.name))
                person.tempstuntime -= 1
                if person.tempstuntime <= 0:
                    person.tempstun = False
            else:
                if person.player:
                    f.takeallinput()
                    person.tempbattlemove = None
                    print("\n\nEnemy Stats:\n\nHealth : {}              Base_Damage : {}              Armor : {}\n                      ".format(d.color.RED + str(otherplayer.health) + d.color.END, d.color.RED + str(otherplayer.damage) + d.color.END, d.color.RED + str(otherplayer.armor) + d.color.END))
                    print("\n\nYour Stats:\n\nHealth : {}              Base_Damage : {}              Armor : {}".format(d.color.RED + str(person.health) + d.color.END, d.color.RED + str(person.damage) + d.color.END, d.color.RED + str(player.armor) + d.color.END))
                    print("\n")
                    person.print_adrenaline()
                    print("\n\n")
                    time.sleep(0.5)
                    print("What would you like to do? ")
                    print(d.color.BOLD + """
                    Attack(1)
                    Block(2)
                    Dodge(3)
                    Use Ability(4)
                    Do Nothing
                    """ + d.color.END)
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
                else:
                    person.tempbattlemove = None
                    print("\n\n")
                    input = m.choose_move(person, otherplayer)

                if input in ['Attack', 'attack', 'a', 'A', '1', 'one', '!']:
                    if person.adrenaline >= 5:
                        person.lose_adrenaline(5)
                        attackdamage = person.calculate_attackdamage()
                        person.tempbattlemove = 'attack'
                        chance = random.randrange(0, 100)
                        if chance in range(0, int(10 * person.misschanceincrease)):
                            print("{} misses their attack!".format(person.name))
                            person.tempbattlemove = None
                        else:
                            if otherplayer.tempbattlemove not in ['block', 'dodge']:
                                print("{} attacks dealing {} damage!".format(person.name, d.color.RED + str(attackdamage) + d.color.END))
                                otherplayer.take_battledamage(attackdamage)
                            else:
                                if otherplayer.tempbattlemove == 'dodge':
                                    otherplayer.add_adrenaline(40)
                                    print("{} dodges {}'s attack".format(otherplayer.name, person.name))
                                elif otherplayer.tempbattlemove == 'block':
                                    print("{} blocks {}'s attack".format(otherplayer.name, person.name))
                                    otherplayer.blockheal()
                    else:
                        print("{} doesn't have enough adrenaline to perform an attack so they do nothing".format(person.name))
                elif input in ['Block', 'block', 'b', 'B', '2', 'two', '@']:
                    if person.adrenaline >= 20:
                        if person.player:
                            print("You prepare to block!")
                        person.lose_adrenaline(20)
                        chance = random.randrange(0, 100)
                        if chance in range(0, int(80 * person.blockchanceincrease)):
                            person.tempbattlemove = 'block'
                            person.lose_adrenaline(20)
                        else:
                            print("{} failed to block!".format(person.name))
                    else:
                        print("{} doesn't have enough adrenaline to block so they do nothing!".format(person.name))
                elif input in ['Dodge', 'dodge', 'd', 'C', '3', 'three', '#']:
                    chance = random.randrange(0, 100)
                    if chance in range(0, int(80 * person.dodgechanceincrease)):
                        if person.player:
                            print("You prepare to dodge!")
                        person.tempbattlemove = 'dodge'
                    else:
                        print("{} failed to dodge!".format(person.name))
                elif input in ['Use Ability', 'use Ability', 'UseAbility', 'useability', 'u', 'U', 'ua', 'UA', '4', 'four'] or isinstance(input, m.Ability_Object):
                    if person.player:
                        abilities = person.displayabilities()
                        #
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
                                    abilityinput = c
                                    inputing = False
                                except IOError: pass
                        finally:
                            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
                    else:
                        abilities = person.get_abilities()
                        abilityinput = input.abilitynumber
                    if abilityinput.isdigit():
                        ability = abilities[int(abilityinput) - 1]
                        fail = False
                        if person.adrenaline - ability.adrenaline >= 0:
                            print("{} uses {}!".format(person.name, ability.name))
                            person.lose_adrenaline(ability.adrenaline)
                            if ability.misschance:
                                if random.randrange(0, 100) < int(ability.misschance * 100):
                                    person.tempbattlemove = 'ability'
                                else:
                                    print("{} fails to use the ability {}!".format(person.name, ability.name))
                                    fail = True
                                    person.tempbattlemove = None
                            if ability.healmult:
                                if not fail:
                                    healamount = person.getmaxhealth() * ability.healmult
                                    print("{} heals {} health!".format(person.name, healamount))
                                    person.addhealth(healamount)
                            if ability.damagemult and not fail:
                                if ability.damagetype:
                                    attackdamage = person.calculate_abilitydamage(ability.damagemult)
                                    if ability.damagetype == 'normal':
                                        if otherplayer.tempbattlemove not in ['block', 'dodge']:
                                            print("{} deals {} damage with {}!".format(person.name, d.color.RED + str(attackdamage) + d.color.END, ability.name))
                                            otherplayer.take_battledamage(attackdamage)
                                        else:
                                            if otherplayer.tempbattlemove == 'dodge':
                                                otherplayer.add_adrenaline(40)
                                                print("{} dodges {}'s ability".format(otherplayer.name, person.name))
                                            elif otherplayer.tempbattlemove == 'block':
                                                print("{} blocks {}'s ability".format(otherplayer.name, person.name))
                                                otherplayer.blockheal()
                                    elif ability.damagetype == 'stun':
                                        basetime = person.basestuntime
                                        if otherplayer.tempbattlemove not in ['block', 'dodge']:
                                            print("{} stuns {}!".format(person.name, otherplayer.name))
                                            otherplayer.tempstun = True
                                            otherplayer.tempstuntime = int(basetime * person.stuntimeincrease)
                                            otherplayer.take_battledamage(attackdamage)
                                        else:
                                            if otherplayer.tempbattlemove == 'dodge':
                                                otherplayer.add_adrenaline(40)
                                                print("{} dodges {}'s ability".format(otherplayer.name, person.name))
                                            elif otherplayer.tempbattlemove == 'block':
                                                print("{} blocks {}'s ability".format(otherplayer.name, person.name))
                                                otherplayer.blockheal()
                                    elif ability.damagetype == 'fire':
                                        basetime = person.basefiretime
                                        if otherplayer.tempbattlemove not in ['block', 'dodge']:
                                            print("{} hits {} with fire!".format(person.name, otherplayer.name))
                                            otherplayer.temponfire = True
                                            otherplayer.tempfiretime = int(basetime * person.firetimeincrease)
                                            otherplayer.tempfiredamage = attackdamage
                                        else:
                                            if otherplayer.tempbattlemove == 'dodge':
                                                otherplayer.add_adrenaline(40)
                                                print("{} dodges {}'s ability".format(otherplayer.name, person.name))
                                            elif otherplayer.tempbattlemove == 'block':
                                                print("{} blocks {}'s ability".format(otherplayer.name, person.name))
                                                otherplayer.blockheal()
                                    else:
                                        raise Exception("Something went wrong with using your ability... Contact support...")
                                else:
                                    raise Exception("Something went wrong with using your ability... Contact support...")
                        else:
                            print("{} doesn't have enough adrenaline to use their ability".format(person.name))
                            person.tempbattlemove = 'nothing'
                    else:
                        print("{} does nothing!".format(person.name))
                        person.tempbattlemove = 'nothing'
                else:
                    print("{} does nothing!".format(person.name))
                    person.tempbattlemove = 'nothing'
                if people[0].dead == False and people[1].dead == False:
                    pass
                else:
                    time.sleep(3)
                    if people[0].player == True:
                        return(people[1].loot_drop())
                    elif people[1].player == True :
                        return(people[0].loot_drop())
