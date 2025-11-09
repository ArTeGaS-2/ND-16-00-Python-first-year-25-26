import pygame
import sys

# Налаштування
WIDTH, HEIGHT = 800, 600 # Ширина і висота
BG_COLOR = (20, 20, 20)  # колір фону
TEXT_COLOR = (255,255,255) # колір тексту
FPS = 60 # кадри за секунду

BUTTON_IMAGE_PATH = "Lesson_7/button.png"
TEXT_TEMPLATE = "Кліків: {}"

def main():
    pygame.init()
    pygame.display.set_caption("Простий клікер") # Заголовок
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Налаштування екрану
    clock = pygame.time.Clock() # лічильник pygame, налаштовує FPS

    # Шрифт
    font = pygame.font.SysFont("arial", 36)

    # Завантаження зображення кнопки
    button_img = pygame.image.load(BUTTON_IMAGE_PATH).convert_alpha()
    button_img = pygame.transform.scale(button_img, (200,200))

    button_rect = button_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    clicks = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    clicks += 1
        
        screen.fill(BG_COLOR)
        screen.blit(button_img, button_rect)

        text_str = TEXT_TEMPLATE.format(clicks)
        text_surf = font.render(text_str, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(midtop=(WIDTH // 2, 20))
        screen.blit(text_surf, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



