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

    # Шрифт, вибір з системних
    font = pygame.font.SysFont("arial", 36)

    # Завантажуємо зображення і вмикаємо прозорість
    button_img = pygame.image.load(BUTTON_IMEGE_PATH).convert_alpha()
    # Міняємо розмір
    button_img = pygame.transform.scale(button_img, (200, 200))
    # Розміщуємо прямокутник зображення по центру
    button_rect = button_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    clicks = 0 # Скільки кліків зроблено

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicks += 1

 
        screen.blit(button_img, button_rect)
        screen.fill(BG_COLOR)

        pygame.display.flip()

main()

pygame.quit()
sys.exit()