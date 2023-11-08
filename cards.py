import stdio
import sys
import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []

for suit in suits:
    for rank in ranks:
        card = rank + ' of ' + suit
        deck += [card]

random.shuffle(deck)

hands = int(sys.argv[1])

for i in range(hands):
    stdio.writeln("Hand " + str(i + 1) + ":" )
    stdio.writeln("Card 1:" + deck[random.randrange(0, len(deck))])
    stdio.writeln("Card 2:" + deck[random.randrange(0, len(deck))])
    stdio.writeln("Card 3:" + deck[random.randrange(0, len(deck))])
    stdio.writeln("Card 4:" + deck[random.randrange(0, len(deck))])
    stdio.writeln("Card 5:" + deck[random.randrange(0, len(deck))])


