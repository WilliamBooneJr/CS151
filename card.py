import stdio
import random

#create class Card and Deck

class Card:
    def __init__(self, rank, suit, value):
        self._rank = rank
        self._suit = suit
        self._value = value

    def get_value(self):
            
            return self._value
        
    def set_value(self, value):
            
            self._value = value

    def __str__(self):
            
            return self._rank + ' of ' + self._suit
        
class Deck:

    def __init__(self):
            self._cards = []
            for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
                  for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                               'Jack', 'Queen', 'King', 'Ace']:
                        if rank == 'Jack' or rank == 'Queen' or rank == 'King':
                              value = 10
                        elif rank == 'Ace':
                              value = 11
                        else:
                              value = int(rank)
                        card = Card(rank, suit, value)
                        self._cards.append(card)
            random.shuffle(self._cards)
    
    def print_deck(self):
            for card in self._cards:
                  stdio.writeln(card)
    
    def deal_card(self):
            return self._cards.pop(0)
    
    def shuffle(self):
            random.shuffle(self._cards)

    def deck_size(self):
            return len(self._cards)
    
    def __str__(self):
            s = ''
            for card in self._cards:
                  s = s + str(card) + '\n'
            return s
    
#test client

def main():
    deck = Deck()
    stdio.writeln(deck)
    stdio.writeln('Deck size = ' + str(deck.deck_size()))
    stdio.writeln()
    stdio.writeln('Dealing ...')
    stdio.writeln()
    card1 = deck.deal_card()
    stdio.writeln('Card 1 = ' + str(card1))
    stdio.writeln('Deck size = ' + str(deck.deck_size()))

if __name__ == '__main__':
    main()
    
            