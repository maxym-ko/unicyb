from deck import Decks, Deck


class _AbstractStack:
    # Абстрактна стопка карт. Можна покласти, скинути та подивитись верхню.
    def __len__(self):
        raise NotImplementedError

    def top(self):
        raise NotImplementedError

    def can_put(self, card):
        raise NotImplementedError

    def put(self, card):
        if self.can_put(card):
            self._put(card)
            return True
        else:
            return False

    def _put(self, card):
        raise NotImplementedError

    def away(self):
        pass


class _Stack(_AbstractStack):
    # Складові (8 стопок) базового ряду; першою картою є туз
    def __init__(self, suit):
        self.card = None
        self.put(self.ace(suit))

    def top(self):
        return self.card

    def ace(self, suit):
        return Deck.Card('A', suit)

    def __len__(self):
        if self.card is None:
            return 0
        return self.card.value

    def full(self):
        return len(self) == len(Deck.RANKS)

    def can_put(self, card):
        return not self or (not self.full() and card.value == self.top().value + 1)

    def _put(self, card):
        self.card = card


class _PlayColumn(_AbstractStack):
    # Вертикальний ігровий ряд.
    def __init__(self):
        self.row = []

    def can_put(self, card):
        return True

    def _put(self, card):
        self.row.append(card)

    def __len__(self):
        return len(self.row)

    def top(self):
        return self.row[-1]

    def away(self):
        self.row.pop()


class _ReservePlayColumn(_PlayColumn):
    # Вертикальний резервний ігровий ряд.
    def __init__(self, play_deck):
        self.row = []
        for _ in range(13):
            self._put(play_deck.top())
            play_deck.away()

    def can_put(self, card):
        return False


class Row(tuple):
    """
    Кортеж фіксованого розміру.
    Конструктор отримує кількість елементів та iterable.
    """

    def __new__(cls, n, it):
        it = iter(it)
        obj = super().__new__(cls, (next(it) for _ in range(n)))
        return obj


class _PlayDeck:
    def __init__(self, deck):
        self.deck = deck
        self.card = None
        self.away()

    def top(self):
        return self.card

    def __len__(self):
        return len(self.deck) + (self.card is not None)

    def away(self):
        if self.deck:
            self._away()
        else:
            self.card = None

    def _away(self):
        self.card = self.deck.deal()

    def put(self, card):
        return False


class Play:
    NBASE = 8
    NPLAY = 5
    N_RESERVE_PLAY = 1

    def __init__(self):
        self._deck = Decks(2)
        self._playdeck = None  # колода на столі
        self._base = None  # базовий ряд
        self._play = None  # гральні вертикальні ряди
        self._reserve_play = None  # резервний гральний вертикальний ряд
        self._in_play = False
        self.new_play()

    def new_play(self):
        self._deck.shuffle()
        self._playdeck = _PlayDeck(self._deck)
        self._base = Row(self.NBASE, (_Stack(s) for s in ('C', 'S', 'H', 'D') * 2))
        self._play = Row(self.NPLAY, iter(lambda: _PlayColumn, None))
        self._reserve_play = _ReservePlayColumn(self._playdeck)
        self._in_play = True

    def win(self):
        res = all(stack.full() for stack in self._base)
        self._in_play = not res
        return res

    @staticmethod
    def move(stack_from, stack_to):
        flag = Play.can_move(stack_from, stack_to)
        if not flag:
            return False
        card = stack_from.top()
        if card is None:
            return False
        res = stack_to.put(card)
        if not res:
            return False
        stack_from.away()
        return True

    @staticmethod
    def can_move(stack_from, stack_to):
        if isinstance(stack_to, _PlayColumn) and not isinstance(stack_from, _PlayDeck):
            return False
        return True

    def play_play(self, i_from, i_to):
        assert (0 <= i_from < len(self._play))
        assert (0 <= i_to < len(self._play))
        if i_from != i_to:
            return self.move(self._play[i_from], self._play[i_to])
        return True

    def play_base(self, i_from, i_to):
        assert (0 <= i_from < len(self._play))
        assert (0 <= i_to < len(self._base))
        return self.move(self._play[i_from], self._base[i_to])

    def deck_play(self, i_to):
        assert (0 <= i_to < len(self._play))
        return self.move(self._playdeck, self._play[i_to])

    def deck_base(self, i_to):
        assert (0 <= i_to < len(self._base))
        return self.move(self._playdeck, self._base[i_to])
