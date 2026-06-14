import random

import pygame

from settings import CELL_SIZE, COLS, FOOD_COLOR, ROWS

class Food:
    def __init__ (self, snake):
        self.position = (0, 0) # Початкова позиція їжі 
        self.move_to_free_cell(snake)
    
    def move_to_free_cell(self, snake):
        while True:
            new_position = (random.randrange(COLS), random.randrange(ROWS))
            if new_position not in snake.body:
                self.position = new_position
                return
            
    def draw(self, screen):
        x, y = self.position
        center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE // 2 - 4)
        pygame.draw.circle(screen, FOOD_COLOR, center, CELL_SIZE // 2 - 4)