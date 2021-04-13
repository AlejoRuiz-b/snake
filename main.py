import pygame

from game import Game

def main():
    # Initialize the pygame
    pygame.init()
    game = Game()
    game_over = False

    while not game_over:

        game_over = game.run()



main()


