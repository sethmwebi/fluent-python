import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card("7", "diamonds")
deck = FrenchDeck()
from random import choice

# print(choice(deck))
# print(choice(deck))
# print(choice(deck))
# print(deck[:3])
# print(deck[12::13])
# for card in deck:
#     print(card)
# print(Card("Q", "hearts") in deck)
# print(Card("7", "beasts") in deck)
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):  # type: ignore
    print(card)
