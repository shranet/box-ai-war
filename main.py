import pygame
from pygame.locals import *
from settings import *
from draw import Image


class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = WIDTH, HEIGHT
        self.tiles = []

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.tiles = [
            Image(self.screen, "background.png", (0, 0, WIDTH, HEIGHT)),
            Image(self.screen, "tiles/1.png", (10, 10, TILESIZE, TILESIZE)),
            Image(self.screen, "tiles/2.png", (10+TILESIZE, 10, TILESIZE, TILESIZE)),
        ]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        for tile in self.tiles:
            tile.render()

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
