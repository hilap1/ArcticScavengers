import random
import mercenaryCard
import itemCard


class PlayerDeck:

    def __init__(self):
        self.deck = []

        self.deck.extend(self.add_multiple_cards_of_same_type("Refugee", [0,0,-1], [-1,0,0,-1,-1], [-1, -1, -1, -1, -1], 1, 4))
        self.deck.extend(self.add_multiple_cards_of_same_type("Scavenger", [0,1,-1], [1,1,1,1,-1], [-1,-1,-1,-1,-1], 1, 3))
        self.deck.append(mercenaryCard.MercenaryCard("Brawler", [0,2,-1], [-1,1,-1,2,-1], [-1,-1,-1,-1,-1], 1))
        self.deck.append(itemCard.ItemCard("Pickaxe", [-1,-1,-1,-1,-1], [-1,1,-1,2,-1], "tool"))
        self.deck.append(itemCard.ItemCard("Shovel", [-1,-1,-1,-1,-1], [-1,2,-1,1,-1], "tool"))

        random.shuffle(self.deck)

    def add_multiple_cards_of_same_type(self, name, cost_arr, actions_arr, enhancers_arr, people_count, num):
        temp_deck = []
        junk_card = mercenaryCard.MercenaryCard(name, cost_arr, actions_arr, enhancers_arr, people_count)
        for x in range(num):
            temp_deck.append(junk_card)

        return temp_deck