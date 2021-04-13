import pygame
import random

from board import Board
from snake import Snake

from cell import Cell
from food import Food
import math, time


class Game(object):
    def __init__(self):
        self.width = 750
        self.height = 650
        self.board = Board(self.width, self.height)  # Create board ancho, alto
        self.board.setTitle("Snake")  # Set tittle
        self.cell = Cell(self.width / 2, self.height / 2)  # Create Cell
        self.score = 0
        self.food = Food(random.randint(0, self.width - 10), random.randint(0, self.height - 10))  # Create apple

        self.cell1 = Cell((self.height / 2) + 10, (self.width / 2) + 10)  # Create Cell
        self.snake = Snake(self.cell1)


    # Distance between the snake and the apple

    @staticmethod
    def distance(appleX, cellX, appleY, cellY):
        distance = math.sqrt((math.pow(appleX - cellX, 2)) + (math.pow(appleY - cellY, 2)))
        if distance < 12:
            return True

    def addScore(self, point):
        self.score += 1

    def showScore(self, screen, font):
        score = font.render("Score: " + str(self.score), True, (255, 255, 255))
        screen.blit(score, (10, 10))

    def gameOver(self, screen):

        font = pygame.font.Font('freesansbold.ttf', 50)
        game = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game, (self.width / 2, self.width / 2))
        pygame.display.flip()

    # Main method that shows board and cell and get events for the movement
    def run(self):

        font = pygame.font.Font('freesansbold.ttf', 18)
        game_over = False
        self.board.showScreen()

        screen = self.board.getScreen()
        cell2 = Cell(390, 390)
        self.snake.appendCell(cell2)

        # pygame.display.flip()

        running = True

        while running:

            for event in pygame.event.get():
                # print(event) # to print clicks events and keyboard events
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True

                # IF keystroke is pressed check whether its right or left
                if event.type == pygame.KEYDOWN:  # KEYDOW is pressing that key or pressing any button on the keyboard
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()

                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()

                    if event.key == pygame.K_UP:
                        self.snake.move_up()

                    if event.key == pygame.K_DOWN:
                        # self.cell.move_down()
                        # self.snake[0].move_down()
                        self.snake.move_down()
                        print("Down arrow is pressed")

            # EAT
            eat = self.snake.eat(self.food.getPosX(), self.food.getPosY())
            if eat:
                # Move the apple each time the snake eat it
                self.food.setPosX(random.randint(10, self.width - 10))
                self.food.setPosY(random.randint(10, self.height - 16))

                # create a new cell and add it to the snake
                cell = Cell(390, 390)
                self.snake.appendCell(cell)
                # Add score
                self.addScore(1)

            if not game_over:

                # Show Snake, food and score
                self.snake.walk(screen)
                self.food.draw(screen)
                self.showScore(screen, font)

                # Get head position
                head = [self.snake.getHeadPossition()[0], self.snake.getHeadPossition()[1]]
                print('head: ', head[1])
                #print(self.height - 16)
                time.sleep(0.1)
                if head[0] >= self.width- 20 or head[1] >= self.height - 25 or head[0] <= 0 or head[1] <= 16:
                    game_over = True



                pygame.display.update()

            else:
                self.gameOver(screen)
                # pygame.display.update()

        return game_over

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
