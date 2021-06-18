import os
import pygame


class Asset:
    def __init__(self):
        self.assets = {}

        for root, subdirs, files in os.walk("./assets"):
            for file in files:
                key = root[9:] + ("-" if root[9:] else "") + file[:-4]
                self.assets[key] = pygame.image.load(root + "/" + file)


    def get(self, item):
        return self.assets[item]




