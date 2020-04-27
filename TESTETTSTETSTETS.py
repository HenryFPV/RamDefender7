import pygame, time, random
from pygame.locals import *
import math
from pygame.math import Vector2
pg = pygame
pygame.init()


SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60
BACKGROUND_COLOR = pygame.Color('white')

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

BLACK           = (0, 0, 0)
BLUE            = (50, 50, 255)

BRIGHTGREEN     = (34,139,34)
GREEN           = (0, 255, 0)

RED             = (255, 0, 0)
DARKRED         = (200, 0, 0)


class Hunter(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Hunter, self).__init__()

        self.image = pygame.Surface((32, 32))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        self.speed = 2

    def hunt_player(self, player):
        player_position = player.rect.topleft
        direction = player_position - self.position
        velocity = direction.normalize() * self.speed

        self.position += velocity
        self.rect.topleft = self.position

    def update(self, player):
        self.hunt_player(player)


class Player(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Player, self).__init__()

        self.image = pygame.Surface((32, 32))
        self.image.fill(pygame.Color('blue'))
        self.rect = self.image.get_rect(topleft=position)

        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.walls = None

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0

        if keys[pygame.K_UP]:
            self.velocity.y = -self.speed
        elif keys[pygame.K_DOWN]:
            self.velocity.y = self.speed
        else:
            self.velocity.y = 0

        self.position += self.velocity
        self.rect.topleft = self.position
        



all_sprite_list = pg.sprite.Group()
wall_list = pg.sprite.Group()


player = Player(position=(350, 220))
monster = Hunter(position=(680, 400))










running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    monster.update(player)

    screen.fill(BACKGROUND_COLOR)
    screen.blit(player.image, player.rect)
    screen.blit(monster.image, monster.rect)

    pygame.display.update()