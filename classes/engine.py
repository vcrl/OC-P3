from .sprites import Player, Wall, Item, Gardien, all_sprites, walls, items
import pygame, sys, os
from .settings import *

class Engine:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
    
    def load_map(self):
        self.player = Player(12, 11)
        # Chargement de labyrinthe.txt
        self.map_data = list()
        current_dir = os.path.dirname(__file__)
        with open(os.path.join(current_dir, "labyrinthe.txt"), "r") as f:
            for line in f:
                self.map_data.append(line)
                for row, tiles in enumerate(self.map_data):
                    for col, tile in enumerate(tiles):
                        if tile == "1": # Mur
                            self.walls = Wall(col, row)
                            pass
                        elif tile == ".": # Chemin
                            pass  
                        elif tile == "G": # Gardien
                            Gardien(col, row)
                        elif tile == "S": # Seringue
                            Item(col, row, "seringue")
                        elif tile == "E": # Ether
                            self.items = Item(col, row, "ether")
                        elif tile == "A": # Aiguille
                            self.items = Item(col, row, "aiguille")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move(dy=-1)
                if event.key == pygame.K_DOWN:
                    self.player.move(dy=+1)
                if event.key == pygame.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pygame.K_RIGHT:
                    self.player.move(dx=1)

    def update(self):
        all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        all_sprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        # Boucle du jeu
        self.load_map()
        while True:
            self.events()
            self.update()
            self.draw()
            
            
