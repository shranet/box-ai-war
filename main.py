import pygame
from pygame.locals import *
from settings import *
from draw import Image, Tile, Row
from assets import Asset
from player import Player


class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = WIDTH, HEIGHT
        self.tiles = []

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self._running = True

        self.asset = Asset()

        self.player1 = Player(self.screen, self.asset, [0, 0])
        self.player2 = Player(self.screen, self.asset, [100, 100])

        self.tiles = [
            Image(self.screen, self.asset, "background", (0, 0, WIDTH, HEIGHT)),

            Row(self.screen, self.asset, 0, 15, 11),

            Row(self.screen, self.asset, 0, 6, 9, 13),
            Row(self.screen, self.asset, 9, 15, 9, 13),

            Row(self.screen, self.asset, 2, 13, 7, 13),

            Tile(self.screen, self.asset, "obj-mushroom-1", (4, 6)),
            Tile(self.screen, self.asset, "obj-mushroom-1", (11, 6))
        ]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.player1.right()
            elif event.key == pygame.K_LEFT:
                self.player1.left()

    def on_loop(self):
        B2_WORLD.Step(1 / 60.0, 6, 3)

    def on_render(self):
        for tile in self.tiles:
            tile.render()

        self.player1.render()
        self.player2.render()

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

            self.clock.tick(60)

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
