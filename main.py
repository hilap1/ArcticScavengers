import card
import random


def add_multiple_cards_of_same_type(card_name, num):
    temp_deck = []
    card_obj = cardFactory.factory(card_name)
    for x in range(num):
        temp_deck.append(card_obj)

    return temp_deck


def build_player_deck():
    deck = []

    deck.extend(add_multiple_cards_of_same_type("Refugee", 4))
    deck.extend(add_multiple_cards_of_same_type("Scavenger", 3))
    deck.append(cardFactory.factory("Brawler"))
    deck.append(cardFactory.factory("Spear"))
    deck.append(cardFactory.factory("Shovel"))

    random.shuffle(deck)

    return deck


def build_junkyard():
    junkyard = []

    junkyard.extend(add_multiple_cards_of_same_type("Junk", 7))
    junkyard.extend(add_multiple_cards_of_same_type("Multitool", 4))
    junkyard.extend(add_multiple_cards_of_same_type("Net", 4))
    junkyard.extend(add_multiple_cards_of_same_type("Spear", 6))
    junkyard.extend(add_multiple_cards_of_same_type("Pickaxe", 4))
    junkyard.extend(add_multiple_cards_of_same_type("Shovel", 6))
    junkyard.extend(add_multiple_cards_of_same_type("Medkit", 6))
    junkyard.extend(add_multiple_cards_of_same_type("Pills", 9))

    random.shuffle(junkyard)

    return junkyard


if __name__ == '__main__':
    cardFactory = card.Card()

    action_used = [] #Draw, Dig, Hunt, Fight, Hire, Trash
    special_action_used = [] #Disarm, Snipe

    player_deck = build_player_deck()
    junkyard_deck = build_junkyard()

    for card in player_deck:
        print(card.name)

    for card in junkyard_deck:
        print(card.name)
