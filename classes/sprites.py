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
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.inventory = 0

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx 
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        # Ramasser les items
        collision_items = pygame.sprite.spritecollide(self, items, False)
        for item in collision_items:
            item.kill()
            self.inventory += 1
        # Rencontre avec le gardien / fion du jeu
        collision_gardien = pygame.sprite.spritecollide(self, npc, False)
        if collision_gardien:
            if self.inventory >= 3:
                print("Vous avez gagné !")
                sys.exit()
            else:
                print("Il vous manque des objets.")

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(WALL_IMG)
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item):
        self.groups = all_sprites, items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(random.choice(ITEMS_IMG))
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.type = item

class Gardien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, npc
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(GARDIEN_IMG)
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE