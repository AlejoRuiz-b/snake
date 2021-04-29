import math
import random
import time

import pygame

from board import Board
from cell import Cell
from food import Food
from snake import Snake


class Game(object):
    def __init__(self):

        # Create board
        self.width = 750
        self.height = 550
        self.board = Board(self.width, self.height)  # Create board ancho, alto
        self.board.setTitle("Snake")  # Set tittle

        # Create snake
        self.cell1 = Cell((self.height / 2) + 10, (self.width / 2) + 10)  # Create Cell
        cell2 = Cell(390, 390)
        self.snake = Snake(self.cell1)
        self.snake.appendCell(cell2)

        # Create food
        self.food = Food(random.randint(0, self.width - 10), random.randint(0, self.height - 10))

        # Create Score
        self.score = 0

        # AI
        self.reward = 0

    def addScore(self, point):
        self.score += 1

    def showScore(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 18)
        score = font.render("Score: " + str(self.score), True, (255, 255, 255))
        screen.blit(score, (10, 10))

    # Calculate distance between the head and the snake body
    def isCollition(self, headPosx, cellX, headPosy, cellY):
        distance = math.sqrt((math.pow(headPosx - cellX, 2)) + (math.pow(headPosy - cellY, 2)))
        if distance <= 0 or headPosx >= self.width - 20 or headPosy >= self.height - 18 or headPosx <= -1.5 or headPosy <= 0.9:
            return True

    # Shows Game over title
    def gameOver(self, screen):

        font = pygame.font.Font('freesansbold.ttf', 40)
        game = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game, (220, (self.height) / 2))
        pygame.display.flip()

    def restart(self):
        self.__init__()

    # Main method that shows board and cell and get events for the movement
    def run(self):

        game_over = False

        self.board.showScreen()

        screen = self.board.getScreen()

        running = True

        while running:

            for event in pygame.event.get():
                # print(event) # to print clicks events and keyboard events
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True

                # IF keystroke is pressed check whether its right or left
                if event.type == pygame.KEYDOWN:  # KEYDOW is pressing that key or pressing any button on the keyboard

                    if event.key == pygame.K_RETURN:
                        self.restart()
                        game_over = False

                    if self.snake.direction == 'down':
                        if event.key == pygame.K_LEFT:
                            self.snake.move_left()

                        if event.key == pygame.K_RIGHT:
                            self.snake.move_right()
                    if self.snake.direction == 'left':
                        if event.key == pygame.K_UP:
                            self.snake.move_up()

                        if event.key == pygame.K_DOWN:
                            # self.cell.move_down()
                            # self.snake[0].move_down()
                            self.snake.move_down()
                    if self.snake.direction == 'right':
                        if event.key == pygame.K_UP:
                            self.snake.move_up()

                        if event.key == pygame.K_DOWN:
                            # self.cell.move_down()
                            # self.snake[0].move_down()
                            self.snake.move_down()

                    if self.snake.direction == 'up':
                        if event.key == pygame.K_LEFT:
                            self.snake.move_left()

                        if event.key == pygame.K_RIGHT:
                            self.snake.move_right()

            if not game_over:
                # EAT
                eat = self.snake.eat(self.food.getPosX(), self.food.getPosY())
                if eat:
                    # Move the apple each time the snake eat it
                    self.food.setPosX(random.randint(20, self.width - 18))
                    self.food.setPosY(random.randint(20, self.height - 16))

                    # create a new cell and add it to the snake
                    cell = Cell(390, 390)
                    self.snake.appendCell(cell)
                    # Add score
                    self.addScore(1)

                # Show Snake, food and score
                self.snake.walk(screen)
                self.food.draw(screen)
                self.showScore(screen)

                # validate when snake eats himself
                # Get head position
                head = [self.snake.getHeadPossition()[0], self.snake.getHeadPossition()[1]]

                body = self.snake.getBody()
                for i in range(1, len(body)):
                    if self.isCollition(head[0], body[i].getPosX(), head[1], body[i].getPosY()):
                        game_over = True

                time.sleep(0.07)
                pygame.display.update()

            else:
                self.gameOver(screen)

        return game_over
