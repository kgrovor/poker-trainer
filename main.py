#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:01:02 2018

@author: kshitij
"""
from random import shuffle
def sanitize(num):
    if num == 1:
        num = "A"
    elif num == 11:
        num = "J"
    elif num == 12:
        num = "Q"
    elif num == 13:
        num = "K"

    return num


class Card:
    def __init__(self, number, suit):
        self.number = sanitize(number)
        self.suit = suit

    def __str__(self):
        return str(self.number) + " of " + self.suit

class Player:
    def __init__(self, money, id):
        self.dealt_cards = ()
        self.money = money
        self.id = id
        self.is_dealer = False
        self.folded = False

    def check_pot(self, pot):
        return pot # Unchanged
    def raise_pot(self, pot, amount):
        # TODO: Require everyone to either call or fold
        self.money -= amount
        return pot+amount
        pass
    def fold(self):
        self.folded = True
    def call_pot(self):
        # TODO: Add logic to call based on previous call/raise
        pass

    def get_move(self, pot):
        # Temporary placeholder till we have GUI to decide move
        # return self.check_pot(pot)
        return self.raise_pot(pot, 12)

    def __str__(self):
        statement = "[ player:" + str(self.id) + "{" + str(self.money) + "} " + str(self.dealt_cards[0]) + "  &  " + str(self.dealt_cards[1]) + "]"
        if self.is_dealer is True:
            statement = statement + "*"
        return statement

class Engine:
    blinds = 10
    def __init__(self, num_players, buy_in):
        suits_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = []
        self.players = []
        self.pot = 0
        for i in range(1, 14):
            for j in suits_list:
                self.cards.append(Card(i, j))

        for i in range(num_players):
            self.players.append(Player(buy_in, i))

    def shuffle_deck(self):
        shuffle(self.cards)

    def dealer(self):
        for i in range(self.players):
            if self.player[i].is_dealer == True:
                return i
        return -1

    def bidding(self):
        for player_ in self.players:
            self.pot = player_.get_move(self.pot)

    def rank_players(self):
        ranked = self.players
        # TODO: Add logic for comparing hands
        return ranked

    def dist_cards(self, dealer=0):  # Todo make it a circle around the dealer
        self.pot = 0
        self.shuffle_deck()
        i = 0
        for pid in range(len(self.players)):
            player_ = self.players[(dealer+pid)%len(self.players)]
            player_.dealer = False
            player_.dealt_cards = (self.cards[i], self.cards[i + 1])
            i += 2
            player_.money -= self.blinds
            self.pot += self.blinds
        self.players[dealer].dealer = True
        return (self.cards[i], self.cards[i+1], self.cards[i+2]), self.cards[i+3], self.cards[i + 4]


if __name__ == "__main__":
    run = Engine(3, 500)
    flop, turn, river = run.dist_cards(dealer = 0)
    print("\nPot is worth ", run.pot, "\n")
    for i in flop:
        print(i, end =",")
    print()
    run.bidding()
    input("Press Enter to continue...\n")
    print(turn)
    run.bidding()
    input("Press Enter to continue...\n")
    print(river)
    run.bidding()
    results = run.rank_players()
    for rank in range(len(results)):
        print("Rank #" + str(rank) + " = " + str(results[rank]))
