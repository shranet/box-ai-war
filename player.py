from draw import Image
from settings import *
from Box2D import *


class Player:
    def __init__(self, screen, asset, pos):
        self.pos = pos
        self.tile = Image(screen, asset, "obj-crate", pos + [TILESIZE, TILESIZE])

        bodyDef = b2BodyDef()
        bodyDef.position.Set(*pos)

        self.body:b2Body = B2_WORLD.CreateBody(bodyDef)

        shape = b2PolygonShape()
        shape.SetAsBox(TILESIZE, TILESIZE)

        self.body.CreateFixture(shape=shape)

    def right(self):
        self.tile.rect[0] += 5

    def left(self):
        self.tile.rect[0] -= 5

    def render(self):
        self.tile.rect[0] = self.body.position.x
        self.tile.rect[1] = self.body.position.y
        # print(self.body.position.x)
        self.tile.render()
