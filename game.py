import pygame
import random

from board import Board

from cell import Cell
from food import Food
import math



class Game(object):
    def __init__(self):
        self.board = Board(800, 600)  # Create board
        self.board.setTitle("Snake")  # Set tittle
        self.cell = Cell()  # Create Cell
        self.food = Food(random.randint(0,784), random.randint(0,580))  # Create apple
        # screen.blit(self.cell, (200, 300))
        # self.board.setIcon()

    # Main method that shows board and cell and get events for the movement
    def show_Cell_on_Board(self, screen, body, posX, posY):
        if posX <= 0:
            posX = 0
        elif posX >= 784:
            posX = 784
        if posY <= 0:
            posY = 0
        elif posY >= 584:
            posY = 584
        screen.blit(body, (posX, posY))

    def show_Apple_on_Board(self, screen, body, posX, posY):
        screen.blit(body, (posX, posY))

    # Calcule the distance between the snake and the apple

    def eat(self, appleX, cellX, appleY, cellY):
        distance = math.sqrt((math.pow(appleX - cellX, 2)) + (math.pow(appleY - cellY, 2)))
        if distance < 15:
            return True


    def run(self):
        screen = self.board.showScreen()
        body = self.cell.getCell()
        apple = self.food.getApple()
        posX, posY = 380, 380
        running = True
        while running:
            screen.fill((0, 0, 0))

            for event in pygame.event.get():
                # print(event) # to print clicks events and keyboard events
                if event.type == pygame.QUIT:
                    running = False

                # IF keystroke is pressed check whether its right or left
                if event.type == pygame.KEYDOWN:  # KEYDOW is pressing that key or pressing any button on the keyboard
                    if event.key == pygame.K_LEFT:
                        print("Left arrow is pressed")
                        self.cell.setPosX_Change(-0.25)
                    if event.key == pygame.K_RIGHT:
                        print("Right arrow is pressed")
                        self.cell.setPosX_Change(0.25)
                    if event.key == pygame.K_UP:
                        self.cell.setPosY_Change(-0.25)
                        print("up arrow is pressed")
                    if event.key == pygame.K_DOWN:
                        self.cell.setPosY_Change(0.25)
                        print("Down arrow is pressed")

                if event.type == pygame.KEYUP:  # KeyUP is releasing that press
                    if event.key == pygame.K_LEFT:
                        self.cell.setPosX_Change(-0.1)
                        self.cell.setPosY_Change(0)
                    if event.key == pygame.K_RIGHT:
                        self.cell.setPosX_Change(0.1)
                        self.cell.setPosY_Change(0)
                    if event.key == pygame.K_UP:
                        self.cell.setPosY_Change(-0.1)
                        self.cell.setPosX_Change(0)
                    if event.key == pygame.K_DOWN:
                        self.cell.setPosY_Change(0.1)
                        self.cell.setPosX_Change(0)

            posX += self.cell.getPosX_Change()
            posY += self.cell.getPosY_Change()

            # EAT
            eat = self.eat(self.food.getPosX(), posX, self.food.getPosY(), posY)
            if eat:
                print("I ate him")
                self.food.setPosX(random.randint(0,784))
                self.food.setPosY(random.randint(0,580))
                #self.show_Apple_on_Board()

            self.show_Cell_on_Board(screen, body, posX, posY)

            self.show_Apple_on_Board(screen, apple, self.food.getPosX(), self.food.getPosY())

            pygame.display.update()
