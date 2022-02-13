import random
import itemCard


class Junkyard:

    def __init__(self):
        self.deck = []

        self.deck.extend(self.add_multiple_cards_of_same_type("Junk", [-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1], "tool", 7))
        self.deck.extend(self.add_multiple_cards_of_same_type("Multitool", [-1,-1,-1,-1,-1], [-1,1,1,1,-1], "tool", 4))
        self.deck.extend(self.add_multiple_cards_of_same_type("Net", [-1,-1,-1,-1,-1], [-1,-1,2,1,-1], "tool", 4))
        self.deck.extend(self.add_multiple_cards_of_same_type("Spear", [-1,-1,-1,-1,-1], [-1,-1,1,2,-1], "tool", 6))
        self.deck.extend(self.add_multiple_cards_of_same_type("Pickaxe", [-1,-1,-1,-1,-1], [-1,1,-1,2,-1], "tool", 4))
        self.deck.extend(self.add_multiple_cards_of_same_type("Shovel", [-1,-1,-1,-1,-1], [-1,2,-1,1,-1], "tool", 6))
        self.deck.extend(self.add_multiple_cards_of_same_type("Medkit", [-1,-1,-1,-1,2], [-1,-1,-1,-1,-1], "tool", 6))
        self.deck.extend(self.add_multiple_cards_of_same_type("Pills", [-1,-1,-1,-1,1], [-1,-1,-1,-1,-1], "tool", 9))

        random.shuffle(self.deck)

    def add_multiple_cards_of_same_type(self, name, actions_arr, enhancers_arr, type, num):
        temp_deck = []
        junk_card = itemCard.ItemCard(name, actions_arr, enhancers_arr, type)
        for x in range(num):
            temp_deck.append(junk_card)

        return temp_deck
