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



    '''def move_left(self):
        self.direction ='left'
        #self.posX -= 10
        #self.draw(screen)

    def move_right(self):
        self.direction = 'right'
        #self.posX += 10
        #self.draw(screen)

    def move_up(self):
        self.direction = 'up'
        #self.posY -= 10
        #self.draw(screen)

    def move_down(self):
        self.direction = 'down'
        #self.posY += 10
        #self.draw(screen)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for i in range(self.length):

            screen.blit(self.cell, (self.posX[i], self.posY[i]))
        # pygame.display.flip()'''

    '''def walk(self, screen):
        # assign the position to n of n-1
        for i in range (self.length-1,0,-1): #range(start, stop, step)
            print('pos Y 0 ',self.posY[0])
            print('pos Y 1 ', self.posY[1])
            self.posX[i] = self.posX[i - 1]
            self.posY[i] = self.posY[i - 1]

        if self.direction =='left':
            self.posX[0] -= SIZE
        if self.direction == 'right':
            self.posX[0] += SIZE
        if self.direction == 'up':
            self.posY[0] -= SIZE
        if self.direction =='down':
            self.posY[0] += SIZE
       

        self.draw(screen)'''







