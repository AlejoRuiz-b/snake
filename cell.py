import pygame

SIZE = 16
class Cell(object):

    def __init__(self, posX, posY):
        #self.screen = screen

        self.cell = pygame.image.load('square16pix.png')
        '''self.length = length
        self.posX = [SIZE]*length
        self.posY = [SIZE]*length'''
        self.direction= 'down'
        self.posX = posX
        self.posY = posY

    def setPosX(self, posX):
        self.posX = posX

    def setPosY(self, posY):
        self.posY = posY

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def getCell(self):
        return self.cell



