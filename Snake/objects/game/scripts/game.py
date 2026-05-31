import pygame

from settings import (BG_COLOR,
                    CELL_SIZE,
                    FPS,
                    GRID_COLOR,
                    HEIGHT,
                    WIDTH,
                    MOVE_DELAY_MS)

from objects.snake.scripts.snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("OOP Snake Prototype")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.move_timer_ms = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.snake.change_direction((0, -1))
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    self.snake.change_direction((0, 1))
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    self.snake.change_direction((-1, 0))
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.snake.change_direction((1, 0))

        return True

    def draw_grid(self):
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen ,GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WIDTH, y))

    def draw(self):
            self.screen.fill(BG_COLOR)
            self.draw_grid()
            self.snake.draw(self.screen)
            pygame.display.flip()

    def run(self, max_frames=None):
        running = True
 
        frames = 0
        while running:
            dt_ms = self.clock.tick(FPS)
            running = self.handle_events()
            self.update(dt_ms)
            self.draw()
            frames += 1
            if max_frames is not None and frames >= max_frames:
                running = False
    
    def update(self, dt_ms):
        self.move_timer_ms += dt_ms
        if self.move_timer_ms < MOVE_DELAY_MS:
            return
        self.move_timer_ms = 0
        self.snake.move()