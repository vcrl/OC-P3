from .map import Labyrinthe
from .settings import *
import pygame
import sys

class Engine:
    def __init__(self):
        # Paramètres de la fenêtre
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        # Gestion du temps
        self.clock = pygame.time.Clock()
        # Gestion des sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        # Chargement de la map
        self.map = Labyrinthe(self) #ERREUR ICI: le programme s'arrête ici, sans passer par les méthodes plus bas (donc probable erreur dans classes/map.py)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        print("draw")
        self.all_sprites.draw()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.draw()
            self.events()
    
    