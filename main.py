import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
import sys
from bullet import *


pygame.init()


clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, bullets)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0

    while 0 == 0:
        screen.fill((0,0,0))

        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)

        for sprites in asteroids:
            if sprites.is_colliding(player):
                print("Game Over!")
                sys.exit()
            for bullet in bullets:
                if sprites.is_colliding(bullet):
                    sprites.kill()
                    bullet.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return


if __name__ == "__main__":
    main()