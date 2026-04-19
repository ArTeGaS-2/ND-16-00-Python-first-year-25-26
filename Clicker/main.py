import pygame
import sys

WIDTH, HEIGHT = 800, 600 # Ширина і висота у пікселях
BG_COLOR = (20, 20, 20) # RGB колір - Червоний, Зелений, Синій
TEXT_COLOR = (255, 255, 255) # Колір тексту, теж RGB
FPS = 60 # Кадри за секунду

BUTTON_IMEGE_PATH = "button.png" # Шлях до зображення кнопки
TEXT_TEMPLATE = "Кліків: {}" # Шаблон тексту на екрані

def main():
    pygame.init() # Ініціалізація вікна
    pygame.display.set_caption("Простий клікер") # Встановюємо заголовок
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        pygame.display.flip()

main()

pygame.quit()
sys.exit()