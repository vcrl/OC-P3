import pygame, sys, random
from .settings import *

all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group()
walls = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(PLAYER_IMG)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.inventory = 0

    def move(self, dx=0, dy=0):
        self.rect.x += dx * TILESIZE
        self.rect.y += dy * TILESIZE

    def update(self):
        self.current_x = self.rect.x
        self.current_y = self.rect.y

        # Ramasser les items
        collision_items = pygame.sprite.spritecollide(self, items, False)
        for item in collision_items:
            item.kill()
            self.inventory += 1

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(WALL_IMG)
        #self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
