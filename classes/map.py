from .sprites import Player, Wall, Item
from .settings import *
import pygame
import os

class Labyrinthe():
    def __init__(self, game):
        self.game = game
        self.map = dict()
        self.map_data = list()
        self.player = None
        #Chargement de la map à chaque instance
        self.loadMap()

    def loadMap(self):
        "On génère la map à partir de labyrinthe.txt"
        current_dir = os.path.dirname(__file__)
        with open(os.path.join(current_dir, "labyrinthe.txt"), "r") as f:
            for line in f:
                self.map_data.append(line)
                for row, tiles in enumerate(self.map_data):
                    for col, tile in enumerate(tiles):
                        if tile == "1": # Mur
                            self.map[row, col] = "mur"
                            self.wall = Wall(row, col) 
                            self.game.all_sprites.add(self.wall) 
                            self.game.walls.add(self.wall)
                        elif tile == "P": # McGyver
                            self.playerRandomPos(row, col)
                        elif tile == "G": # Gardien
                            self.map[row, col] = "gardien" 
                        elif tile == "I": # Item
                            self.itemsRandomPos(row, col)

    # Méthodes liées à l'environnement
    def itemsRandomPos(self, x, y):
        "Méthode pour spawn les items aléatoirement sur la map, sans conflit avec les objets"
        item_spawned = False
        print("itemrandompos")
        while not item_spawned:
            self.item = Item(x, y)
            conflict = pygame.sprite.spritecollide(self.item, self.game.all_sprites, False)
            if  len(conflict) == 0:
                self.game.all_sprites.add(self.item)
                self.game.items.add(self.item)
                item_spawned = True

    # Méthodes liées au joueur
    def playerRandomPos(self, x, y):
        "Méthode pour spawn le joueur aléatoirement sur la map, sans conflit avec les objets"
        player_spawned = False
        while not player_spawned:
            self.player = Player(x, y)
            conflict = pygame.sprite.spritecollide(self.player, self.game.walls, False)
            if  len(conflict) == 0:
                self.game.all_sprites.add(self.player)
                player_spawned = True
    
    # ERREUR: Le code n'a pas l'air d'aller jusque là. Erreur plus haut?
    def moveTo(self, dx=0, dy=0):
        dir_x = self.player.rect.x + dx
        dir_y = self.player.rect.y + dy
        
        if self.map[dir_x, dir_y] != "mur":
            self.player.rect.x += dx
            self.player.rect.y += dy

        if "seringue" not in self.player.inventory:
            if self.map[dir_x, dir_y] == "seringue":
                self.player.addtoInventory("seringue")
        if "ether" not in self.player.inventory:
            if self.map[dir_x, dir_y] == "ether":
                self.player.addtoInventory("ether")
        if "aiguille" not in self.player.inventory:
            if self.map[dir_x, dir_y] == "aiguille":
                self.player.addtoInventory("aiguille")

    def movePlayer(self, key):
        if key == "q":
            self.moveTo(dy=-TILESIZE)
            print(self.player.x, self.player.y)
        if key == "d":
            self.moveTo(dy=TILESIZE)
            print(self.player.x, self.player.y)
        if key == "s":
            self.moveTo(dx=TILESIZE)
            print(self.player.x, self.player.y)
        if key == "z":
            self.moveTo(dx=-TILESIZE)
            print(self.player.x, self.player.y)