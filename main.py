import junkyard
import playerDeck
import merceneriesRow

if __name__ == '__main__':
    # action_used = [] #Draw, Dig, Hunt, Fight, Hire, Trash
    # special_action_used = [] #Disarm, Snipe

    junkyard = junkyard.Junkyard()
    player_hand = playerDeck.PlayerDeck()
    merc_row = merceneriesRow.MerceneriesRow()

    for card in junkyard.deck:
        print(card.name)

    for card in player_hand.deck:
        print(card.name)

    print(len(merc_row.thugs))
    print(len(merc_row.hunters))
    print(len(merc_row.scavengers))
    print(len(merc_row.sniper_teams))
    print(len(merc_row.brawlers))
    print(len(merc_row.saboteurs))
    print(len(merc_row.scouts))
    print(len(merc_row.group_leaders))


