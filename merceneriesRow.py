import mercenaryCard


class MerceneriesRow:

    def __init__(self):
        self.brawlers = self.add_multiple_cards_of_same_type("Brawler", [0,2,-1], [-1,1,-1,2,-1], [-1,-1,-1,-1,-1], 1, 10)
        self.hunters = self.add_multiple_cards_of_same_type("Hunter", [1,0,-1], [-1,-1,2,1,-1], [-1,-1,-1,-1,-1], 1, 8)
        self.saboteurs = self.add_multiple_cards_of_same_type("Saboteur", [1,1,-1], [-1,1,-1,1,-1], [-1,-1,-1,-1,-1], 1, 8)
        self.scouts = self.add_multiple_cards_of_same_type("Scout", [1,2,-1], [2,-1,-1,2,-1], [-1,-1,-1,-1,-1], 1, 8)
        self.group_leaders = self.add_multiple_cards_of_same_type("Group Leader", [2,2,-1], [-1,-1,-1,-1,-1], [2,2,2,2,-1], 2, 5)
        self.sniper_teams = self.add_multiple_cards_of_same_type("Sniper Team", [2,2,-1], [-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1], 2, 5)
        self.thugs = self.add_multiple_cards_of_same_type("Thug", [0,0,6], [-1,1,-1,3,-1], [-1,-1,-1,-1,-1], 3, 5)
        self.scavengers = self.add_multiple_cards_of_same_type("Scavenger", [0,1,-1], [1,1,1,1,-1], [-1,-1,-1,-1,-1], 1, 20)

        self.scavengers = self.add_multiple_cards_of_same_type("Medic", [0,3,-1], [1,-1,-1,-1,1],[-1,-1,-1,-1,-1], 1, 20)
        self.scavengers = self.add_multiple_cards_of_same_type("Engineer", [1,2,-1], [1,2,-1,2,-1],[-1,-1,-1,-1,-1], 1, 20)

    def add_multiple_cards_of_same_type(self, name, cost_arr, actions_arr, enhancers_arr, people_count, num):
        temp_deck = []
        junk_card = mercenaryCard.MercenaryCard(name, cost_arr, actions_arr, enhancers_arr, people_count)
        for x in range(num):
            temp_deck.append(junk_card)

        return temp_deck