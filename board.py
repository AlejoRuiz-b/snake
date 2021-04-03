import pygame
from cell import Cell


class Board(object):
    def __init__(self, pixelsX, pixelsY):
        # create the screen

        self.pixelsX = pixelsX
        self.pixelsY = pixelsY
        #self.screen = pygame.display.set_mode((self.pixelsX, self.pixelsY))

        #pygame.display.set_caption("Snake")

    def showcell(self, screen):
        cell = pygame.image.load('square16pix.png')
        screen.blit(cell, (300, 380))

    def showScreen(self):
        screen = pygame.display.set_mode((self.pixelsX, self.pixelsY))

        return screen

    def setTitle(self, title):
        pygame.display.set_caption(title)

    def setIcon(self):
        icon = pygame.image.load('snake.png')
        pygame.display.set_icon(icon)

    # Title and Icon
    def running(self):
        screen = self.showScreen()

        running = True
        while running:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                # print(event) # to print clicks events and keyboard events
                if event.type == pygame.QUIT:
                    running = False

            self.showcell(screen)
            pygame.display.update()


'''board=Board(800,600)
board.running()
board.setTitle("Snake")'''