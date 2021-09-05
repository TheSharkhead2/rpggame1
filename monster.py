import dictionary as d
import random
import classes as c
import functions as f
import Abilities as a

def make_name():
    if random.randrange(1, 100) == 34:
        return "Ryan The Poonster"
    elif random.randrange(1, 100) == 54:
        return "Theo The Rode"
    elif random.randrange(1, 100) == 98:
        return "Murray The Rodester"
    elif random.randrange(1, 100) == 78:
        return "Timo Rodestar"
    name = ''
    name += random.choice(d.monster1)
    name += ' '
    name += random.choice(d.monster2)
    if random.randrange(0, 10) < 6:
        name += ' '
        name += random.choice(d.monster3)
    return name
    
class Ability_Object:
    def __init__(self, abilitynumber, ability):
        self.ability = ability 
        self.abilitynumber = abilitynumber 
        self.choice = '4'

def choose_move(monster, player):
    #AI code goes here
    if not player.temponfire and random.randrange(1, 100) > 70:
        choice = 0 
        for ability in monster.get_abilities():
            choice += 1
            if ability.damagetype == 'fire':
                abilitychoice = ability 
                choicenumber = choice
        if choicenumber:
            return(Ability_Object(str(choicenumber), abilitychoice))
        else:
            pass
                
    if player.tempbattlemove == 'nothing' and monster.adrenaline > 5:
        return 'attack'
    if player.health < monster.damage and monster.adrenaline > 10:
        return 'attack'
    if monster.health <= (monster.getmaxhealth() * 0.21): 
        abilitychoice = None 
        choicenumber = None
        choice = 0
        for ability in monster.get_abilities():
            choice += 1
            if ability.healmult:
                if abilitychoice != None:
                    if ability.healmult > abilitychoice.healmult:
                        abilitychoice = ability 
                        choicenumber = choice
                else:
                    abilitychoice = ability 
                    choicenumber = choice
        if abilitychoice != None and (monster.getmaxhealth() * abilitychoice.healmult) >= (monster.level * 50):
            if monster.adrenaline - 10 > abilitychoice.adrenaline:
                if random.randrange(1, 100) > 40: 
                    return Ability_Object(str(choicenumber), abilitychoice)
            if monster.adrenaline > 30:
                chance = random.randrange(0, 10)
                if chance in range(0, 6):
                    return 'block'
        else:
            if monster.adrenaline > 30:
                chance = random.randrange(0, 10)
                if chance in range(0, 6):
                    return 'block'
    

    if monster.adrenaline <= 40:
        chance = random.randrange(0, 10)
        if chance in range(0, 7):
            return 'dodge'
    if monster.adrenaline >= 5:
        if player.tempbattlemove != 'attack' and player.tempbattlemove != 'ability':
            if random.randrange(1, 100) > 30:
                return 'attack'
            else:
                return("Nothing")
        else:
            return 'attack'

class Monster(c.Person):

    def level_scale(self, player):
        if player.level > self.maxlevel:
            if player.level - 2 > self.maxlevel:
                self.level = player.level - 2
            else:
                self.level = self.maxlevel
        else:
            self.level = self.maxlevel
    def get_gear(self, player):
        add_level_chance = random.randrange(1, 20/player.heat)
        if add_level_chance == 1:
            add_level = 1
        else:
            add_level = 0
        helmet = c.Helmet.helmet_gen(self.level + add_level)
        arms = c.Arms.arms_gen(self.level + add_level)
        chest = c.Chest.chest_gen(self.level + add_level)
        leggings = c.Leggings.leggings_gen(self.level + add_level)
        boots = c.Boots.boots_gen(self.level + add_level)
        self.equip_helmet(helmet)
        self.equip_arms(arms)
        self.equip_chest(chest)
        self.equip_leggings(leggings)
        self.equip_boots(boots)
    def get_weapon(self):
        y = ['c.Sword.sword_gen(self.level)', 'c.Dagger.dagger_gen(self.level)', 'c.Mace.mace_gen(self.level)', 'c.Club.club_gen(self.level)', 'c.Spear.spear_gen(self.level)', 'c.Frying_Pan.fryingpan_gen(self.level)', 'c.Axe.axe_gen(self.level)', 'c.Heavy_Blunt.heavyblunt_gen(self.level)']
        type = random.choice(y)
        self.equip_weapon(eval(type))
    def loot_drop(self):
        y = ['self.weapon', 'self.helmet', 'self.arms', 'self.chest', 'self.leggings', 'self.boots']
        drop = random.choice(y)
        return eval(drop)
    def attack_damage(self):
        pass
    def __init__(self, name, maxlevel, player):
        self.player = False
        self.devmode = False
        self.name = name
        self.maxlevel = maxlevel
        self.armorperk = 1
        self.damageperk = 1
        self.healthperk = 1
        self.basestuntime = 1
        self.basefiretime = 4
        self.critchanceincrease = 1
        self.dodgechanceincrease = 1
        self.blockchanceincrease = 1
        self.misschanceincrease = 1
        self.critdamageincrease = 1
        self.damageconsistency = 0
        self.firedamageincrease = 1
        self.firetimeincrease = 1
        self.stuntimeincrease = 1
        self.temponfire = False
        self.tempfiretime = None
        self.tempstun = False
        self.tempstuntime = None
        self.tempfiredamage = None
        self.weapon = None
        self.helmet = None
        self.arms = None
        self.chest = None
        self.leggings = None
        self.boots = None
        self.level_scale(player)
        self.get_gear(player)
        self.get_weapon()
        self.health = self.getmaxhealth()
        
        self.tempbattlemove = None
        self.dead = False
        self.adrenaline = 100
        #Temp for ability testing
        self.abilities = a.Abilities()
        self.abilities.train_HomingSword()
        self.abilities.train_HeavyStrike()
        self.abilities.train_SecondWind()
        self.abilities.train_StunAttack()
        self.abilities.train_FireStrike()
    
    def getmaxhealth(self):
        return self.level * 450 * self.healthperk
    @classmethod
    def mercenary_gen(cls, maxlevel, player):
        name = make_name()
        return cls(name, maxlevel, player)
