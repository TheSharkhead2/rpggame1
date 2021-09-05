from reprint import output
import dictionary as d

class Location:
    def __init__(self, name, quest_name, quest_type, oqv, quest_goal, next_location):
        self.name = name
        self.quest_name = quest_name
        self.quest_type = quest_type
        self.original_quest_value = oqv
        self.quest_goal = quest_goal
        self.next_location = next_location
        #generate list of npcs and quests. 
        #add new mercenaries based on maybe a "heat level" of the player out of 10
    def get_complete_quest(self, player):
        if self.quest_type == 'mercenary':
            if player.killed_mercenaries - self.original_quest_value >= self.quest_goal:
                return(True)
            else:
               
                return(float(float(player.killed_mercenaries - self.original_quest_value)/float(self.quest_goal)) * 100)
        elif self.quest_type == 'coins':
            if player.coins - self.original_quest_value >= self.quest_goal:
                return(True)
            else:
                return(float(float(player.coins - self.original_quest_value)/float(self.quest_goal)) * 100)
    def print_quest_percent(self, player):
        print(d.color.BOLD + "Quest" + d.color.END)
        print(self.quest_name)
        with output(output_type='dict') as output_lines:
            adrenaline = self.get_complete_quest(player)
            output_lines['Completed : '] = "[{done}{padding}] {percent}%".format(
                done = d.color.RED + "#" * int(adrenaline/10) + d.color.END,
                padding = " " * (10 - int(adrenaline/10)),
                percent = adrenaline
                )
    def get_next_location(self, player):
        if self.get_complete_quest(player) == True:
            return(self.next_location)
        else:
            return(False)