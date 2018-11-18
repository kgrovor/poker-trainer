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
        if id is not 0:
            self.is_dealer = False
        else: 
            self.is_dealer = True
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
    
    def dist_cards(self):  # Todo make it a circle around the dealer
        self.pot = 0
        self.shuffle_deck()
        i = 0
        for player_ in self.players:
            player_.dealt_cards = (self.cards[i], self.cards[i + 1])
            i = i + 2
            player_.money -= self.blinds
        self.pot = len(self.players)*self.blinds
        return (self.cards[i], self.cards[i+1], self.cards[i+2]), self.cards[i+3], self.cards[i + 4]
        
        
if __name__ == "__main__":
    run = Engine(3, 500)
    flop, turn, river = run.dist_cards()
    print("\nPot is worth ", run.pot, "\n")
    for i in flop:
        print(i, end =",")
    input("Press Enter to continue...\n")
    print(turn)
    input("Press Enter to continue...\n")
    print(river)
    
