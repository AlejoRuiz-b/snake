import pygame


class Cell(object):
    def __init__(self):
        self.cell = pygame.image.load('square16pix.png')

    def getCell(self):
        return self.cell
