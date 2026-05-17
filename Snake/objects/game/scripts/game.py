import pygame

from settings import BG_COLOR, CELL_SIZE
from settings import FPS, GRID_COLOR, HEIGHT,WIDTH

class game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("OOP Snake Prototype")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

def handle_events(self):
    for event in pygame,event.get():
        if event.type == pygame.QUIT:
            return False
     
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
    return True


def draw_grid(self):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(self.screen,GRID_COLOR, (x,0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(self.screen,GRID_COLOR, (0, y), (x, WIDTH, y))

def draw(self):
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        pygame.display.flip()
def run(self, max_frames=None):
    running = True

    frames = 0
    while running:
        self.clock.tick(FPS)
        running = self.handle_events()
        self.draw()
        frames += 1
        if max_frames is not None and frames >= max_frames:
            running = False