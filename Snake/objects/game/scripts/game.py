import pygame
 
from settings import (BG_COLOR,
                    TEXT_COLOR,
                    CELL_SIZE,
                    FPS,
                    GRID_COLOR,
                    HEIGHT,
                    WIDTH,
                    MOVE_DELAY_MS)

from objects.snake.scripts.snake import Snake
from objects.food.scripts.food import Food
 
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("OOP Snake Prototype")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)

        self.snake = Snake()
        self.move_timer_ms = 0
        self.reset()

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

                # Якщо натиснуто R і завершена гра
                if event.key == pygame.K_r and self.game_over:
                    # Перезапускаємо гру
                    self.reset()

        return True

    def draw_grid(self):
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen ,GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WIDTH, y))

    def draw(self):
            self.screen.fill(BG_COLOR)   # Заливаємо фон
            self.draw_grid()             # Малюємо сітку
            self.snake.draw(self.screen) # Малюємо змійку
            self.food.draw(self.score)   # Малюємо їжу
            
            pygame.display.flip()        # Оновлюємо екран.

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
        # Зупиняємо гру якщо спрацював прапорець
        if self.game_over:
            return

        self.move_timer_ms += dt_ms
        if self.move_timer_ms < MOVE_DELAY_MS:
            return
        self.move_timer_ms = 0
        self.snake.move()

        # Якщо голова змійки на клітинці їжі
        if self.snake.head() == self.food.position:
            # Нараховуємо бал
            self.score += 1
            # Змійка зростає
            self.snake.grow()
            # Їжа переміщується у вільну від змійки клітинку
            self.food.move_to_free_cell(self.snake)

        # Перевіряємо стикання з краєм мапи і частинами змійки
        if self.snake.hit_wall() or self.snake.hit_self():
            # Позначаємо, що гра завершена
            self.game_over = True

    def reset(self):
        # Створюємо змійку, або перезаписуємо її
        self.snake = Snake()
        # Створюємо їжу, з посиланням на поточну змійку
        self.food = Food(self.snake)
        # Обнуляємо рахунок
        self.score = 0
        # Скидаємо прапорець завершення гри
        self.game_over = False
        # Скидаємо час між кроками змійки
        self.move_timer_ms = 0

    def draw_text(self):
        # Малюємо поверхню з текстом рахунку
        score_text = self.font.render(f"Рахунок: {self.score}", True, TEXT_COLOR)
        # Малюємо рахунок в лівому верхньому куті
        self.screen.blit(score_text, (16, 12))