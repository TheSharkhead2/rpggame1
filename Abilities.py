import random
import functions as f
import dictionary as d

class Ability(object):
    def __init__(self, name, misschance, damagemult, healmult, block, adrenaline, level, damagetype = False):
        self.misschance = misschance
        self.damagemult = damagemult
        self.healmult = healmult
        self.block = block
        self.adrenaline = adrenaline
        self.damagetype = damagetype
        self.level = level
        self.name = name




class Abilities(object):
    def __init__(self):
        self.abilities = {}
    def train_HomingSword(self):
        if 'HomingSword' not in self.abilities:
            HomingSword = Ability("Homeing Sword", False, 50, False, False, 10, 1, 'normal')
            self.abilities['HomingSword'] = HomingSword
        elif self.abilities['HomingSword'].level == 1:
            self.abilities['HomingSword'].level = 2
            self.abilities['HomingSword'].damagemult = 75
        elif self.abilities['HomingSword'].level == 2:
            self.abilities['HomingSword'].level = 3
            self.abilities['HomingSword'].damagemult = 200
            self.abilities['HomingSword'].adrenaline = 125
        else:
            #Can't upgrade past level 3
            pass
    def train_HeavyStrike(self):
        if 'HeavyStrike' not in self.abilities:
            HeavyStrike = Ability("Heavy Strike", 0.7, 125, False, False, 60, 1, 'normal')
            self.abilities['HeavyStrike'] = HeavyStrike
        elif self.abilities['HeavyStrike'].level == 1:
            self.abilities['HeavyStrike'].level = 2
            self.abilities['HeavyStrike'].damagemult = 150
            self.abilities['HeavyStrike'].adrenaline = 50
        elif self.abilities['HeavyStrike'].level == 2:
            self.abilities['HeavyStrike'].level = 3
            self.abilities['HeavyStrike'].damagemult = 225
            self.abilities['HeavyStrike'].adrenaline = 50
        else:
            #Can't upgrade past level 3
            pass
    def train_SecondWind(self):
        if 'SecondWind' not in self.abilities:
            SecondWind = Ability("Second Wind", False, False, 0.15, False, 20, 1)
            self.abilities['SecondWind'] = SecondWind
        elif self.abilities['SecondWind'].level == 1:
            self.abilities['SecondWind'].level = 2
            self.abilities['SecondWind'].healmult = 0.25
            self.abilities['SecondWind'].adrenaline = 20
        elif self.abilities['SecondWind'].level == 2:
            self.abilities['SecondWind'].level = 3
            self.abilities['SecondWind'].healmult = 0.4
            self.abilities['SecondWind'].adrenaline = 30
        else:
            #Can't upgrade past level 3
            pass
    def train_StunAttack(self):
        if 'StunAttack' not in self.abilities:
            StunAttack = Ability("Stun Attack", 0.8, 5, False, False, 10, 1, 'stun')
            self.abilities['StunAttack'] = StunAttack
        elif self.abilities['StunAttack'].level == 1:
            self.abilities['StunAttack'].level = 2
            self.abilities['StunAttack'].damagemult = 10
            self.abilities['StunAttack'].adrenaline = 10
        elif self.abilities['StunAttack'].level == 2:
            self.abilities['StunAttack'].level = 3
            self.abilities['StunAttack'].damagemult = 15
            self.abilities['StunAttack'].adrenaline = 8
        else:
            #Can't upgrade past level 3
            pass
    def train_FireStrike(self):
        if 'FireStrike' not in self.abilities:
            FireStrike = Ability("Fire Strike", 0.7, 7, False, False, 20, 1, 'fire')
            self.abilities['FireStrike'] = FireStrike
        elif self.abilities['FireStrike'].level == 1:
            self.abilities['FireStrike'].level = 2
            self.abilities['FireStrike'].damagemult = 10
            self.abilities['FireStrike'].adrenaline = 20
        elif self.abilities['FireStrike'].level == 2:
            self.abilities['FireStrike'].level = 3
            self.abilities['FireStrike'].damagemult = 13
            self.abilities['FireStrike'].adrenaline = 15
        else:
            #Can't upgrade past level 3
            pass
    # def train_BlindingBlow(self):
    #     if 'BlindingBlow' not in self.abilities:
    #         BlindingBlow = Ability(20, False, False, 15, 1, 'stun')
    #         self.abilities['BlindingBlow'] = BlindingBlow
    #     elif self.abilities['BlindingBlow'].level == 1:
    #         self.abilities['BlindingBlow'].level = 2
    #         self.abilities['BlindingBlow'].heal = 0.25
    #         self.abilities['BlindingBlow'].adrenaline = 20
    #     elif self.abilities['BlindingBlow'].level == 2:
    #         self.abilities['BlindingBlow'].level = 3
    #         self.abilities['BlindingBlow'].heal = 0.4
    #         self.abilities['BlindingBlow'].adrenaline = 30
    #     else:
    #         #Can't upgrade past level 3
    #         pass



#Abilities in game
