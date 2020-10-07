import pygame, sys, random
from .settings import *

all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group()
walls = pygame.sprite.Group()
npc = pygame.sprite.Group()

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
        # Ramasser les items
        collision_items = pygame.sprite.spritecollide(self, items, False)
        for item in collision_items:
            item.kill()
            self.inventory += 1
        # Rencontre avec le gardien / fion du jeu
        collision_gardien = pygame.sprite.spritecollide(self, npc, False)
        if collision_gardien:
            if self.inventory == 3:
                print("Vous avez gagné !")
                sys.exit()
            else:
                print("Il vous manque des objets.")

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(WALL_IMG)
        #self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item):
        self.groups = all_sprites, items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(random.choice(ITEMS_IMG))
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.type = item

class Gardien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, npc
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(GARDIEN_IMG)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE