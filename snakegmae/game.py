import pygame
from settings import *
from utils import * 

class Snakegame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Sysfont("Arial", 25)
        self.score_font = pygame.font.Sysfont("Arial", 35)
        self.reset_game()
    def reset_game(self):
        self.game_over = False
        self.game_close = False

        self.xl = WINDOW_WIDTH // 2
        self.xl = WINDOW_HEIGHT // 2
        self.xl_change = 0
        self.xl_change = 0

        self.snake_list = []
        self.snake_length = 1

        self.foodx, self.foody = generate_food_poistion(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_BLOCK)