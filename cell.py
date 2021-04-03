import pygame


class Cell(object):
    def __init__(self, posX, posY):
        self.cell = pygame.image.load('square16pix.png')
        self.posX = posX
        self.posY = posY
        self.posX_change = 0
        self.posY_change = 0


    def setPosX(self, posX):
        self.posX = posX

    def setPosY(self, posY):
        self.posY = posY

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY



    def setPosX_Change(self,posX_change):
        self.posX_change = posX_change

    def setPosY_Change(self, posY_change):
        self.posY_change = posY_change

    def getPosY_Change(self):
        return self.posY_change

    def getPosX_Change(self):
        return self.posX_change

    def getCell(self):
        return self.cell





