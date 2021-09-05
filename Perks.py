import random
import dictionary as d
import functions as f

class Perk(object):
    def generate_level(self):
        perklevel = f.rounddown(self.level)/10
        perkstrength = 8 + perklevel
        self.perkstrength = perkstrength
        self.perklevel = perklevel
    def generate_perk(self):
        y = random.randrange(0, len(d.perks))
        self.perk = d.perks[y]
        self.perk_string = d.perk_strings[self.perk]
    def __init__(self, level):
        self.level = level
        self.generate_level()
        self.generate_perk()
    def get_string(self):
        return (d.color.BOLD + str(self.perkstrength) + '%' + d.color.END + ' ' + self.perk_string)
    def get_strength(self):
        return float(self.perkstrength)/100

class LegendaryPerk(Perk):
    def generate_perk(self):
        self.perkstrength = random.randrange(40, 55)
        self.perk = random.choice(d.perks)
        self.perk_string = d.perk_strings[self.perk]
    def __init__(self):
        self.generate_perk()
        self.level = None

class Perks(object):
    def generate_perks(self):
        perks = []
        for x in range(self.numperks):
            perk = Perk(self.level)
            perks.append(perk)
        if self.type == 'Legendary':
            perk = LegendaryPerk()
            perks.append(perk)
        self.perks = perks
    def __init__(self, level, type):
        self.type = type
        self.level = level
        if self.type == 'Common':
            self.numperks = 0
        elif self.type == 'Uncommon':
            self.numperks = 0
        elif self.type == 'Rare':
            self.numperks = 1
        elif self.type == 'Epic':
            self.numperks = 3
        elif self.type == 'Legendary':
            self.numperks = 2
        else:
            raise Exception('Error when creating perks of an item. Possible corruption in files. ')
        self.generate_perks()
    def get_health_strength(self):
        final = 0
        for x in self.perks:
            if x.perk == 'morehealth':
                final += x.get_strength()
        return final
    def get_damage_strength(self):
        final = 0
        for x in self.perks:
            if x.perk == 'moredamage':
                final += x.get_strength()
        return final
    def get_armor_strength(self):
        final = 0
        for x in self.perks:
            if x.perk == 'morearmor':
                final += x.get_strength()
        return final
    def get_crit_chance(self):
        final = 0
        for x in self.perks:
            if x.perk == 'critchance':
                final += x.get_strength()
        return final
