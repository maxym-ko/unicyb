from tkinter import PhotoImage


def _rgb(arg):
    r, g, b = arg[0], arg[1], arg[2]
    return f'#{r:02x}{g:02x}{b:02x}'


def part(source: PhotoImage, left, upper, w, h) -> PhotoImage:
    dest = PhotoImage(width=w, height=h)
    for j in range(h):
        for i in range(w):
            dest.put(_rgb(source.get(left + i, upper + j)), to=(i, j))
    return dest


def card_image(tile: PhotoImage, card, w, h) -> PhotoImage:
    return part(tile, card.rank_index * w, card.suit_index * h, w, h)
