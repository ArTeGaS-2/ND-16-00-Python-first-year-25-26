import os
import sys
import pygame

from objects.game.scripts.game import Game

def main():
    smoke_frames = os.environ.get("SMOKE_TEST_FRAMES")
    max_frames = int(smoke_frames) if smoke_frames else None

    game = Game()
    game.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 