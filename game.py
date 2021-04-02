import pygame

from board import Board

from cell import Cell


class Game(object):
    def __init__(self):
        self.board = Board(800, 600)
        self.board.setTitle("Snake")
        self.cell = Cell
        #screen.blit(self.cell, (200, 300))
        # self.board.setIcon()

    def run(self):
        screen = self.board.showScreen()
        running = True
        while running:
            screen.fill((0, 0, 0))

            for event in pygame.event.get():
                # print(event) # to print clicks events and keyboard events
                if event.type == pygame.QUIT:
                    running = False
            cell1=self.cell.getCell()
            screen.blit(cell1, (300, 380))
            pygame.display.update()
