import pygame


class Food(object):
    def __init__(self, posX, posY):
        self.apple = pygame.image.load('apple.png')
        self.posX = posX
        self.posY = posY
        self.appleX_change = 0
        self.appleY_change = 0

    def setAppleX_change(self, appleX_change):
        self.appleX_change = appleX_change

    def setAppleY_change(self, appleY_change):
        self.appleY_change = appleY_change

    def getAppleY_change(self):
        return self.appleY_change

    def getAppleX_change(self):
        return self.appleX_change

    def setPosX(self, posX):
        self.posX = posX

    def setPosY(self, posY):
        self.posY = posY

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def getApple(self):
        return self.apple

    def draw(self, screen):
        # screen.fill((0, 0, 0)) # I use update function instead
        screen.blit(self.apple, (self.posX, self.posY))
        # pygame.display.flip()
