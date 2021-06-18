from settings import *
import pygame as pg


class Image:
    def __init__(self, screen, file, rect):
        self.screen = screen
        self.rect = rect
        self.file = pg.image.load("assets/{}".format(file))
        self.file = pg.transform.scale(self.file, self.rect[2:])

    def render(self):
        self.screen.blit(self.file, self.rect[0:2])
