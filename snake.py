import pygame
import math


class Snake(object):

    def __init__(self, cell):
        self.cell = cell
        self.body = []
        self.body.append(self.cell)
        self.direction = 'down'

    def appendCell(self, cell):
        cell.setPosX(self.body[len(self.body) - 1].getPosX())  # adding the new cell to the last position of the snake
        cell.setPosY(self.body[len(self.body) - 1].getPosY())
        self.body.append(cell)

    def move_left(self):
        self.direction = 'left'
        # self.posX -= 10
        # self.draw(screen)

    def move_right(self):
        self.direction = 'right'
        # self.posX += 10
        # self.draw(screen)

    def move_up(self):
        self.direction = 'up'
        # self.posY -= 10
        # self.draw(screen)

    def move_down(self):
        self.direction = 'down'
        # self.posY += 10
        # self.draw(screen)

    def getHeadPossition(self):
        return [self.body[0].getPosX(), self.body[0].getPosY()]


    def draw(self, screen):
        screen.fill((0, 0, 0))
        for i in range(len(self.body)):
            screen.blit(self.body[0].getCell(), (self.body[i].getPosX(), self.body[i].getPosY()))


    def eat(self, food_posX, food_posY):
        distance = math.sqrt(
            (math.pow(food_posX - self.body[0].getPosX(), 2)) + (math.pow(food_posY - self.body[0].getPosY(), 2)))
        if distance < 15:
            return True

    def walk(self, screen, ):


        for i in range(len(self.body) - 1, 0, -1):  # range(start, stop, step)
            # print(snake[i-1].getPosX())
            self.body[i].setPosX(self.body[i - 1].getPosX())
            self.body[i].setPosY(self.body[i - 1].getPosY())

        if self.direction == 'left':
            posX = -16
            self.body[0].setPosX(self.body[0].getPosX() + posX)

        if self.direction == 'right':
            posX = 16
            self.body[0].setPosX(self.body[0].getPosX() + posX)

        if self.direction == 'up':
            posY = -16
            self.body[0].setPosY(self.body[0].getPosY() + posY)

        if self.direction == 'down':
            posY = 16
            self.body[0].setPosY(self.body[0].getPosY() + posY)

        self.draw(screen)

