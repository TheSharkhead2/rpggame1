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
   WHITE = '\033[37m'
   END = '\033[0m'

monster1 = ['Alex', 'Bob', 'Kira', 'David', 'Susan', 'Hela', 'Daphne', 'Murray', 'Zooger', 'Sadrur', 'Emma', 'Alanna']
monster2 = ['The Indestructable', 'The Undefeated', 'The Immortal', 'The Powerful', 'The Indifferent']
monster3 = ['Goblin', 'Sage', 'Human', 'Monster', 'Ork', 'Spider', 'Giant']

weapon1 = ['Wooden', 'Dark Steel', 'Metal', 'Engraved Metal', 'Steel', 'Iron', 'Gold', 'Bronze', 'Copper', 'Energy', 'Hard Wood', 'Silver']
weapon2 = ['Mace', 'Club', 'Sword', 'Dagger', 'Spear', 'Frying Pan', 'Axe', 'Ceremonial Axe', 'Heavy Blunt']

sword = ['Sword', 'Sword', 'Sword', 'Ceremonial Sword', 'Spartan Sword']
dagger = ['Dagger', 'Dagger', 'Dagger', 'Dagger', 'Dagger', 'Ceremonial Dagger', 'Lightweight Dagger', 'Assassin Dagger']
mace = ['Mace', 'Mace', 'Mace', 'Mace', 'Heavy Mace']
club = ['Club', 'Club', 'Club', 'Heavy Club', 'Lightweight Club']
spear = ['Spear', 'Spear', 'Spear', 'Spear', 'Short Spear', 'Lightweight Spear', 'Spartan Spear']
fryingpan = ['Frying Pan', 'Frying Pan', 'Frying Pan', 'Broken Frying Pan']
axe = ['Axe', 'Axe', 'Ceremonial Axe', 'Spartan Axe', 'Hatchet', 'Heavy Axe', 'Dual Bladed Axe']
heavyblunt = ['Heavy Blunt', 'Heavy Blunt', 'Heavy Blunt', 'Blunt', 'Bludgeon']

perks = ['morehealth', 'moredamage', 'morearmor', 'critchance']
perk_strings = {
        'morehealth' : 'More Health',
        'moredamage' : 'More Damage',
        'morearmor' : 'More Armor',
        'critchance' : 'Higher Crit Chance'
}


helm1 = ['Leather', 'Metal', 'Golden', 'Silver', 'Spartan', 'Rock', 'Titanium']
helm2 = ['Helm', 'Helmet', 'Mask', 'Facegaurd']

chest1 = ['Leather', 'Gold', 'Golden', 'Steel', 'Silver', 'Leather', 'Titanium']
chest2 = ['Chestplate', 'Breastpeice', 'Chest', 'Tunic']

arms1 = ['Leather', 'Steel', 'Iron', 'Gold', 'Bronze', 'Silver', 'Golden', 'Titanium']
arms2 = ['Handguards', 'Arms', 'Gauntlets', 'Gloves', 'Grips', 'Warfists']

leggings1 = ['Leather', 'Gold', 'Silver', 'Steel', 'Iron', 'Bronze', 'Golden', 'Titanium', 'Spartan']
leggings2 = ['Skirt', 'Legplates', 'Leggings', 'Legguards', 'Legs']

boots1 = ['Leather', 'Gold', 'Silver', 'Steel', 'Iron', 'Bronze', 'Golden', 'Titanium']
boots2 = ['Greaves', 'Boots', 'Sandals']

blacksmith_type_modifiers = {
        "Common" : 1, 
        "Uncommon" : 2, 
        "Rare" : 4, 
        "Epic" : 6,
        "Legendary" : 9,
}

blacksmith_rfbm = [
        "My wife is making meatloaf tonight!",
        "I close in 4 hours!",
        "I am about to retire!",
        "It's my 99th birthday!"

]