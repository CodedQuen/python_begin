values = range(1, 14)  #+  'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]

from random import shuffle
from pprint import pprint
shuffle(deck)
pprint(deck[:12])
['1 of diamonds',
 '3 of clubs',
 '1 of spades'
 '2 of diamonds',
 '4 of clubs',
 '2 of hearts',
 '2 of spades',
 '3 of diamonds',
 '6 of clubs',
 '3 of hearts',
 '8 of spades',
 'Queen of diamonds',
 'Queen of hearts',
 'Kind of hearts',
 'Jack of diamonds',
 'Queen of clubs']

while deck: input(deck.pop())
