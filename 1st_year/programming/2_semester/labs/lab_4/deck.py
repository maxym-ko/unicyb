import random


class Deck:
    SUITS = ('C', 'S', 'H', 'D')
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
    VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12,
              'K': 13}
    ALL_CARDS = ()

    class Card:
        def __init__(self, rank, suit):
            self._rank_index = None
            self._suit_index = None
            if isinstance(rank, str) and isinstance(suit, str):
                self._init_from_str(rank, suit)
            elif isinstance(suit, int) and isinstance(rank, int):
                self._init_from_int(rank, suit)

        def _init_from_str(self, rank, suit):
            self._rank_index = Deck.RANKS.index(rank)
            self._suit_index = Deck.SUITS.index(suit)

        def _init_from_int(self, rank, suit):
            if (rank < 0 or rank >= len(Deck.RANKS)) or (suit < 0 or suit >= len(Deck.SUITS)):
                raise ValueError('No such card')
            self._rank_index = rank
            self._suit_index = suit

        def __str__(self):
            return self.rank + "-" + self.suit

        @property
        def rank(self):
            return Deck.RANKS[self._rank_index]

        @property
        def suit(self):
            return Deck.SUITS[self._suit_index]

        @property
        def rank_index(self):
            return self._rank_index

        @property
        def suit_index(self):
            return self._suit_index

        @property
        def value(self):
            return Deck.VALUES[self.rank]

        def __hash__(self):
            return hash((self.rank_index, self.suit_index))

        def __eq__(self, other):
            if not isinstance(other, Deck.Card):
                return NotImplemented
            return self.rank == other.rank and self.suit == other.suit

        def __lt__(self, other):
            return self.suit == other.suit and self.value < other.value


Deck.ALL_CARDS = list(Deck.Card(r, s) for r in Deck.RANKS for s in Deck.SUITS if r != 'A')


class Decks(list):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, deck_num=1):
        super(Decks, self).__init__()
        self._deck_num = deck_num

    def shuffle(self):
        self.clear()
        for _ in range(self._deck_num):
            self.extend(Deck.ALL_CARDS)
        random.shuffle(self)

    def deal(self):
        return self.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self)==0:
            raise StopIteration
        else:
            return self.deal()

    def debug(self):
        print('{ ' + '  '.join(
            (str(self[i]) + ('\n' if (i + 1) % len(Deck.RANKS) == 0 else '') for i in range(len(self)))) + ' }')
