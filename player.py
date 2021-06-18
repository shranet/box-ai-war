from draw import Image
from settings import TILESIZE


class Player:
    def __init__(self, screen, asset, pos):
        self.pos = pos
        self.tile = Image(screen, asset, "obj-crate", pos + [TILESIZE, TILESIZE])

    def right(self):
        self.tile.rect[0] += 5

    def left(self):
        self.tile.rect[0] -= 5

    def render(self):
        self.tile.render()
