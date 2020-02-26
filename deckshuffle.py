from Deck import Deck
shuffle1 = []
shuffle2 = []
shuffle3 = []
finalDeck = []

deck1 = Deck()
deck1.shuffle()
deck2 = Deck()
deck2.shuffle()
deck3 = Deck()
deck3.shuffle()

shuffle1 = deck1
shuffle2 = deck2
shuffle3 = deck3
finalDeck += deck1[1]

print(deck1)
print(deck2)
print(deck3)

print(shuffle1)

print(finalDeck)
