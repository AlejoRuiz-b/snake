import pygame
import random

from board import Board
from snake import Snake

from cell import Cell
from food import Food
import math, time


class Game(object):
    def __init__(self):
        self.board = Board(800, 600)  # Create board
        self.board.setTitle("Snake")  # Set tittle
        self.cell = Cell(400, 200)  # Create Cell

        self.food = Food(random.randint(0, 784), random.randint(0, 580))  # Create apple

        self.cell1 = Cell(380, 390)  # Create Cell
        self.snake = Snake(self.cell1)


    # Distance between the snake and the apple

    def distance(self, appleX, cellX, appleY, cellY):
        distance = math.sqrt((math.pow(appleX - cellX, 2)) + (math.pow(appleY - cellY, 2)))
        if distance < 15:
            return True

    # Main method that shows board and cell and get events for the movement
    def run(self):
        self.board.showScreen()
        screen = self.board.getScreen()
        cell2 = Cell(390, 390)
        cell3 = Cell(390, 490)
        cell4 = Cell(390, 490)
        self.snake.appendCell(cell2)
        self.snake.appendCell(cell3)


        pygame.display.flip()

        running = True

        while running:

            for event in pygame.event.get():
                # print(event) # to print clicks events and keyboard events
                if event.type == pygame.QUIT:
                    running = False

                # IF keystroke is pressed check whether its right or left
                if event.type == pygame.KEYDOWN:  # KEYDOW is pressing that key or pressing any button on the keyboard
                    if event.key == pygame.K_LEFT:
                        print("Left arrow is pressed")
                        #self.cell.move_left()
                        #self.snake[0].move_left()
                        self.snake.move_left()

                    if event.key == pygame.K_RIGHT:
                        print("Right arrow is pressed")
                        #self.cell.move_right()
                        #self.snake[0].move_right()
                        self.snake.move_right()

                    if event.key == pygame.K_UP:
                        #self.cell.move_up()
                        #self.snake[0].move_up()
                        self.snake.move_up()
                        print("up arrow is pressed")

                    if event.key == pygame.K_DOWN:
                        #self.cell.move_down()
                        #self.snake[0].move_down()
                        self.snake.move_down()
                        print("Down arrow is pressed")

            eat = self.snake.eat(self.food.getPosX(), self.food.getPosY())
            if eat:
                self.food.setPosX(random.randint(0, 784))
                self.food.setPosY(random.randint(0, 580))
                cell = Cell(390, 390)
                self.snake.appendCell(cell)

            self.snake.walk(screen)
            #self.walk(screen, self.snake)
            #self.cell.walk(screen)
            #self.cell.draw(screen)
            self.food.draw(screen)

            time.sleep(0.1)


            pygame.display.update()

    '''def walk( self, screen, snake):
        screen.fill((0, 0, 0))
        print(snake[0].getDirection)
        for i in range(len(snake) - 1, 0, -1):  # range(start, stop, step)
            #print(snake[i-1].getPosX())
            snake[i].setPosX(snake[i-1].getPosX())
            snake[i].setPosY(snake[i-1].getPosY())

        if snake[0].getDirection() == 'left':
            posX = -16
            snake[0].setPosX(snake[0].getPosX()+posX)
            print(snake[0].getPosX())

        if snake[0].getDirection() == 'right':
            posX = 16
            snake[0].setPosX(snake[0].getPosX()+posX)

        if snake[0].getDirection() == 'up':
            posY = -16
            snake[0].setPosY(snake[0].getPosY() + posY)

        if snake[0].getDirection() == 'down':
            posY = 16
            snake[0].setPosY(snake[0].getPosY() + posY)
            print(snake[0].getPosY())

        for i in range(len(snake)):

            screen.blit(snake[0].getCell(), (snake[i].getPosX(), snake[i].getPosY()))'''

