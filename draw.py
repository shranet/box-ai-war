from settings import *
import pygame as pg


class Image:
    def __init__(self, screen, asset, name, rect):
        self.screen = screen
        self.rect = rect
        self.file = asset.get(name)
        self.file = pg.transform.scale(self.file, self.rect[2:])

    def render(self):
        self.screen.blit(self.file, self.rect[0:2])


class Tile(Image):
    def __init__(self, screen, asset, name, pos):
        super().__init__(screen, asset, name,
                         (pos[0] * TILESIZE, pos[1] * TILESIZE, TILESIZE, TILESIZE))


class Row:
    def __init__(self, screen, asset, xs, xe, y, k = 1):
        self.tiles = [
            Tile(screen, asset, "tiles-{}".format(k), (xs, y)),
            *[Tile(screen, asset, "tiles-{}".format(k + 1), (n, y)) for n in range(xs + 1, xe)],
            Tile(screen, asset, "tiles-{}".format(k + 2), (xe, y)),
        ]

    def render(self):
        for tile in self.tiles:
            tile.render()

