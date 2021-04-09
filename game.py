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
        self.cell = Cell( 380, 380,2)  # Create Cell
        self.food = Food(random.randint(0, 784), random.randint(0, 580))  # Create apple
        self.snake =[]
        # screen.blit(self.cell, (200, 300))
        # self.board.setIcon()


    # Distance between the snake and the apple

    def eat(self, appleX, cellX, appleY, cellY):
        distance = math.sqrt((math.pow(appleX - cellX, 2)) + (math.pow(appleY - cellY, 2)))
        if distance < 15:
            return True

    # Main method that shows board and cell and get events for the movement
    def run(self):
        self.board.showScreen()
        screen = self.board.getScreen()
        cell2 = Cell(390, 390,2)
        #self.snake(cell2)
        self.snake.append(self.cell)
        self.snake.append(cell2)
        print(self.snake[0])
        posX, posY = self.snake[0].getPosX(), self.snake[0].getPosY()

        self.cell.draw(screen)

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
                        self.cell.move_left()
                        #self.snake[0].move_left()

                    if event.key == pygame.K_RIGHT:
                        print("Right arrow is pressed")
                        self.cell.move_right()
                        #self.snake[0].move_right()

                    if event.key == pygame.K_UP:
                        self.cell.move_up()
                        #self.snake[0].move_up()
                        print("up arrow is pressed")

                    if event.key == pygame.K_DOWN:
                        self.cell.move_down()
                        #self.snake[0].move_down()
                        print("Down arrow is pressed")

            #self.snake[0].walk(screen)
            self.cell.walk(screen)
            #self.cell.draw(screen)
            self.food.draw(screen)
            time.sleep(0.1)


            pygame.display.update()
