import pygame
from constants import *
from player import *

pygame.init()

clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while 0 == 0:
        screen.fill((0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return


if __name__ == "__main__":
    main()