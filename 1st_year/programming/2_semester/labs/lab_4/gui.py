from tkinter import *
from tkinter.messagebox import showinfo

import play
from cardfaces import CardFaces
from deck import Deck
from locus import Locus

Locus.coords = Locus.left_bottom


def place_image(parent, image, locus: Locus):
    return parent.create_image(*locus.coords(), image=image, anchor=SW)


class GUICard(play.Deck.Card, CardFaces):
    # noinspection PyMissingConstructor
    def __init__(self, card, parent, locus):
        self._rank_index = card.rank_index
        self._suit_index = card.suit_index
        self._parent = parent
        self._item = place_image(self._parent, CardFaces.get(self), locus)

    def away(self):
        if self._parent is not None:
            self._parent.delete(self._item)
        self._parent = None

    def reset(self, locus):
        if self._parent is not None:
            self._parent.coords(self._item, *locus.coords())

    def move(self, dx, dy):
        if self._parent is not None:
            self._parent.move(self._item, dx, dy)

    def raise_(self):
        self._parent.tag_raise(self._item)


class _LAP(Locus):  # LocusAndParent
    def __init__(self, *, parent, **kwargs):
        self._parent = parent
        super().__init__(**kwargs)


# noinspection PyProtectedMember
class _GUIPlayDeck(play._PlayDeck, _LAP):
    def __init__(self, deck, **kwargs):
        _LAP.__init__(self, **kwargs, width=CardFaces.W, height=CardFaces.H)
        self._iback = None
        self._iback = place_image(self._parent, CardFaces.BACK, self)
        play._PlayDeck.__init__(self, deck)

    def _away(self):
        self.card = GUICard(self.deck.deal(), parent=self._parent, locus=self)
        if not self.deck and self._iback:
            self._parent.delete(self._iback)
            self._iback = None


# noinspection PyProtectedMember
class _GUIStack(play._Stack, _LAP):
    def __init__(self, suit, **kwargs):
        _LAP.__init__(self, **kwargs, width=CardFaces.W, height=CardFaces.H)
        play._Stack.__init__(self, suit)
        self._parent.create_rectangle(*self.rectangle(), width=1, outline=GUI._border)

    def _put(self, card):
        if self:
            self.card.away()
        super()._put(card)
        card.reset(self)

    def ace(self, suit):
        return GUICard(Deck.Card('A', suit), parent=self._parent, locus=self)


# noinspection PyProtectedMember
class _GUIPlayColumn(play._PlayColumn, _LAP):
    def __init__(self, playdeck, h, **kwargs):
        _LAP.__init__(self, **kwargs, width=CardFaces.W, height=CardFaces.H)
        self._parent.create_rectangle(*self.rectangle(), width=1, outline=GUI._border)
        self._h = h
        play._PlayColumn.__init__(self)

    def _card_h(self):
        n = len(self) - 1
        if n <= 0:
            return 0
        h = CardFaces.H
        free = self._h - h
        per_card = free // n
        if per_card > h // 2:
            per_card = h // 2
        elif per_card > h // 3:
            per_card = h // 3
        elif per_card > h // 4:
            per_card = h // 4
        return per_card

    def update(self):
        n = len(self)
        if n == 0:
            return
        self.top().reset(self)
        self.top().raise_()
        per_card = self._card_h()
        tmp = self.up(per_card)
        for i in range(n - 2, -1, -1):
            self.row[i].reset(tmp)
            tmp = tmp.up(per_card)

    def _put(self, card):
        super()._put(card)
        self.update()

    def away(self):
        super().away()
        self.update()


# noinspection PyProtectedMember
class _GUIReservePlayColumn(play._ReservePlayColumn, _GUIPlayColumn):
    def __init__(self, playdeck, h, **kwargs):
        _LAP.__init__(self, **kwargs, width=CardFaces.W, height=CardFaces.H)
        self._parent.create_rectangle(*self.rectangle(), width=1, outline=GUI._border)
        self._h = h
        play._ReservePlayColumn.__init__(self, playdeck)


class _XLocator:
    def __init__(self, n, x0, width, wc):
        self._n = n
        self._x0 = x0
        self._w = width
        self._wc = wc
        self._dx = 0
        self._off = 0
        self._calculate()

    def __getitem__(self, item):
        return self._x0 + self._off + item * (self._wc + self._dx)

    def _calculate(self, offset: bool = True):
        if offset:
            n = 1
        else:
            n = -1
        self._dx = (self._w - self._n * self._wc) // (self._n + n)
        self._off = self._dx


# noinspection PyProtectedMember,PyProtectedMember
class GUI(play.Play):
    _background = '#80ff80'
    _border = '#cd0532'

    class _DragFrom(enum.Enum):
        DECK = 1
        PLAY = 2
        RESERVE_PLAY = 3
        BASE = 4
        NONE = 5

    def __init__(self, root):
        CardFaces.create_global_images()
        self._blocked = False
        self._root = root
        self._config_root()
        self._create_canvas()
        self._create_places()
        self._create_menu()
        super().__init__()
        self._set_bindings()

    def new_play(self):
        if self._blocked:
            return
        self._blocked = True
        self.clear()
        self._deck.shuffle()
        self._playdeck = _GUIPlayDeck(self._deck, parent=self._c, left=self._columns[9], bottom=self._y_base)
        self._root.update()
        it = iter(self._columns)
        suits = iter(('C', 'S', 'H', 'D') * 2)
        self._base = play.Row(self.NBASE,
                              iter(lambda: _GUIStack(next(suits), parent=self._c, left=next(it), bottom=self._y_base),
                                   None))
        self._root.update()
        it = iter(self._columns)
        self._play = play.Row(self.NPLAY, iter(lambda: _GUIPlayColumn(self._playdeck, parent=self._c, left=next(it),
                                                                      bottom=self._y_play, h=self._y_play_height),
                                               None))
        it = iter(range(9, -1, -1))
        self._reserve_play = play.Row(self.N_RESERVE_PLAY, iter(lambda: _GUIReservePlayColumn(self._playdeck,
                                                                                              parent=self._c,
                                                                                              left=self._columns[
                                                                                                  next(it)],
                                                                                              bottom=self._y_play,
                                                                                              h=self._y_play_height),
                                                                None))
        self._in_play = True
        self._blocked = False

    def clear(self):
        tmp = self._c.find_all()
        for i in tmp:
            if i not in self._sysitems:
                self._c.delete(i)
        self._dragging = None

    def _config_root(self):
        self._root.title('Fly')
        self._root.resizable(width=False, height=False)
        self._root.config(bg=GUI._background)
        self._w = w = 900
        self._h = h = 720
        sw = self._root.winfo_screenwidth()
        sh = self._root.winfo_screenheight()
        self._root.geometry(f'{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}')

    def _create_canvas(self):
        dx = 25
        dy = 45
        self._cw = self._w - 2 * dx
        self._ch = self._h - 2 * dy
        self._c = Canvas(self._root, background='#004200', width=self._cw, height=self._ch, bd=-2)
        self._sysitems = []
        self._sysitems.append(self._c.create_line(0, 0, self._cw, 0, fill='red', width=2))
        self._sysitems.append(self._c.create_line(self._cw, 0, self._cw, self._ch, fill='red', width=2))
        self._sysitems.append(self._c.create_line(self._cw, self._ch, 0, self._ch, fill='red', width=2))
        self._sysitems.append(self._c.create_line(0, 0, 0, self._ch, fill='red', width=2))
        self._c.place(x=dx, y=dy)

    def _create_places(self):
        self._y_base = CardFaces.H + 50
        self._y_play = self._ch - 50
        self._y_play_height = self._y_play - self._y_base - 40
        # self._x = 0
        self._ch = CardFaces.H
        self._columns = _XLocator(10, 0, self._cw, CardFaces.W)

    def _create_menu(self):
        self._menu = Menu(self._root)
        self._root.config(menu=self._menu)
        self._create_file_menu()
        self._create_help_menu()

    def _create_file_menu(self):
        file = Menu(self._menu, tearoff=0)
        file.add_command(label='New game F5', command=self.new_play)
        file.add_command(label='Close', command=self._root.destroy)
        self._menu.add_cascade(label='File', menu=file)

    def _create_help_menu(self):
        help = Menu(self._menu, tearoff=0)
        help.add_command(label='Help', command=self._help)
        help.add_command(label='About', command=lambda: showinfo('About', 'Author: Koval Maxym\nGroup: K-12'))
        self._menu.add_cascade(label='Help', menu=help)

    def _set_bindings(self):
        self._c.bind('<Button-1>', self.on_press)
        self._c.bind('<B1-Motion>', self.on_move)
        self._c.bind('<ButtonRelease-1>', self.on_release)
        self._root.bind('<F5>', lambda x: self.new_play())
        self._dragging = None
        self._drag_from = None
        self._posx = None
        self._posy = None

    def on_press(self, event):
        if self._blocked:
            return
        self._which_is_dragged(event)
        if self._dragging:
            self._posx, self._posy = event.x, event.y

    def on_move(self, event):
        if self._dragging:
            x, y = self._posx, self._posy
            self._posx, self._posy = event.x, event.y
            dx = self._posx - x
            dy = self._posy - y
            self._dragging.move(dx, dy)
            self._rectangle[0] += dx
            self._rectangle[1] += dy
            self._rectangle[2] += dx
            self._rectangle[3] += dy

    def on_release(self, event):
        if self._dragging:
            to = self._locate_release(event.x, event.y)
            if to is not None:
                to = to[0]
                s = GUI.area(*to.rectangle(), *self._rectangle)
                self._dragging.reset(to)
            if to is None or not self.move(self._drag_from, to):
                self._rollback()
            self.win()
            self._dragging = None
            self._drag_from = None

    def win(self):
        if super().win():
            showinfo('You won', 'Congratulation, you\'ve moved all the cards to the foundation.')

    def _rollback(self):
        self._dragging.reset(self._drag_from)

    def _locate(self, x, y):
        res = None
        if y < self._y_base:
            if self._playdeck.inside(x, y):
                return self._playdeck, self._DragFrom.DECK
            for el in self._base:
                if el.inside(x, y):
                    res = el, self._DragFrom.BASE
                    break
            return res

        for el in self._play:
            if el.inside(x, y):
                res = el, self._DragFrom.PLAY
                break
        if not res:
            for el in self._reserve_play:
                if el.inside(x, y):
                    res = el, self._DragFrom.RESERVE_PLAY
                    break
        return res

    def _locate_release(self, x, y):
        area = -1
        elem = None
        if y < self._y_base * 2:
            for el in self._base:
                tmp = GUI.area(*el.rectangle(), *self._rectangle)
                if tmp > area:
                    area = tmp
                    elem = el
            if area:
                return elem, self._DragFrom.BASE

        for el in self._play:
            tmp = GUI.area(*el.rectangle(), *self._rectangle)
            if tmp > area:
                area = tmp
                elem = el
        if not area:
            for el in self._reserve_play:
                tmp = GUI.area(*el.rectangle(), *self._rectangle)
                if tmp > area:
                    area = tmp
                    elem = el
            if area == 0:
                return None
            return elem, self._DragFrom.PLAY
        if area == 0:
            return None
        return elem, self._DragFrom.RESERVE_PLAY

    @staticmethod
    def area(xmin, ymax, xmax, ymin, xmin2, ymax2, xmax2, ymin2):
        dx = min(xmax, xmax2) - max(xmin, xmin2)
        dy = min(ymax, ymax2) - max(ymin, ymin2)
        if (dx >= 0) and (dy >= 0):
            return dx * dy
        else:
            return 0

    def _which_is_dragged(self, event):
        tmp = self._locate(event.x, event.y)
        if tmp and tmp[1] != self._DragFrom.BASE:
            self._drag_from = tmp[0]
            self._rectangle = list(tmp[0].rectangle())
        if self._drag_from:
            self._dragging = self._drag_from.top()
            self._dragging.raise_()
        else:
            self._drag_from = None

    def _help(self):
        win = Toplevel(self._root)
        win.title('Fly')
        win.resizable(width=False, height=False)
        win.configure(bg='White')
        s = self._root.geometry()
        rest = s.split('+', maxsplit=1)[1]
        win.geometry('650x450+' + rest)
        text = """\
        Кількість колод: 1
        Кількість карт у колоді: 52
        Мета пасьянсу: необхідно зібрати всі карти на базових стопках у висхідних послідовностях незалежно від масті.

        Правила пасьянсу. 8 тузів вилучаються з колоди й викладаються в базовий ряд. Далі колода ретельно тасується й викладаються 13 карт в одну стопку - це резерв. Верхня карта резерву відкривається. Нижче розташовуються місця для п'яти ігрових стопок. Колода, що залишилась, кладеться поруч. Дозволяється переміщати в базовий ряд верхні карти ігрових стопок, резерву й колоди, що залишилася, у висхідній послідовності незалежно від масті. Карти, які не підходять для переміщення, викладаються в 5 ігрових стопок у довільному порядку. Забороняється переміщати карти з однієї ігрової стопки на іншу, а також забороняється переміщати карти з резерву на ігрові стопки. Колода не перездається.
        Пасьянс зійшовся, якщо всі карти зібрані на базових стопках у висхідних послідовностях незалежно від масті.
"""
        Message(win, text=text, justify=LEFT, bg='White', foreground='Black', font=('Times',)).pack(padx=5, pady=5,
                                                                                                    ipadx=5, ipady=5,
                                                                                                    anchor=CENTER,
                                                                                                    expand=YES)
        win.bind('<Escape>', lambda event: win.destroy())
        win.focus_set()
        win.grab_set()
        win.wait_window()