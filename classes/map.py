"""
Fichier map, contenant les classes qui
génèrent la carte du jeu
"""
import os
import sys
import random
import time
from .player import Player
from .constantes import WIDTH, HEIGHT, TILESIZE

class Labyrinthe():
    """
    Classe générant la carte
    """
    def __init__(self):
        self.map = dict()
        self.map_data = list()
        #self.player = Player(2,7)
        #Chargement de la map à chaque instance
        self.loadMap()

    def spawn_items(self):
        """
        Spawn des items sur la carte
        """
        aiguille_spawned = 0
        seringue_spawned = 0
        ether_spawned = 0
        while aiguille_spawned < 1:
            rand_x = random.randint(1, 14)
            rand_y = random.randint(1, 14)
            aiguille = False

            if self.map[rand_x, rand_y] == "chemin":
                #aiguille = False
                #if not ether:
                self.map[rand_x, rand_y] = "aiguille"
                aiguille_spawned += 1
                aiguille = True
                print("aiguille spawned")

        while seringue_spawned < 1:
            rand_x = random.randint(1, 14)
            rand_y = random.randint(1, 14)
            seringue = False
            if self.map[rand_x, rand_y] == "chemin":
                #aiguille = False
                #if not ether:
                self.map[rand_x, rand_y] = "seringue"
                seringue_spawned += 1
                seringue = True
                print("seringue spawned")

        while ether_spawned < 1:
            rand_x = random.randint(1, 14)
            rand_y = random.randint(1, 14)
            ether = False

            if self.map[rand_x, rand_y] == "chemin":
                #aiguille = False
                #if not ether:
                self.map[rand_x, rand_y] = "ether"
                ether_spawned += 1
                ether = True
                print("ether spawned")

    def loadMap(self):
        """
        Chargement du fichier labyrinthe.txt
        """
        current_dir = os.path.dirname(__file__)
        with open(os.path.join(current_dir, "labyrinthe.txt"), "r") as f:
            for line in f:
                self.map_data.append(line)
                for row, tiles in enumerate(self.map_data):
                    for col, tile in enumerate(tiles):
                        if tile == "1": # Mur
                            self.map[row, col] = "mur"
                        elif tile == ".": # Chemin
                            self.map[row, col] = "chemin"
                        elif tile == "P": # McGyver
                            self.player = Player(row, col)
                            self.map[row, col] = "player"
                        elif tile == "G": # Gardien
                            self.map[row, col] = "gardien"

        self.spawn_items()

    def moveTo(self, dx=0, dy=0):
        """
        Check les déplacements du joueur
        (si il marche sur un objet, etc)
        """
        dir_x = self.player.x + dx
        dir_y = self.player.y + dy

        if self.map[dir_x, dir_y] == "seringue":
            self.player.addtoInventory("seringue")

        if self.map[dir_x, dir_y] == "ether":
            self.player.addtoInventory("ether")

        if self.map[dir_x, dir_y] == "aiguille":
            self.player.addtoInventory("aiguille")

        if self.map[dir_x, dir_y] == "gardien":
            if self.player.inventory < 3:
                print("Perdu !")
                time.sleep(2)
                sys.exit()
            elif self.player.inventory == 3:
                print("Gagné !")
                time.sleep(2)
                sys.exit()

        if self.map[dir_x, dir_y] != "mur":
            self.map[self.player.x, self.player.y] = "chemin"
            self.map[self.player.x + dx, self.player.y + dy] = "player"
            self.player.x += dx
            self.player.y += dy

    def movePlayer(self, key):
        """
        Déplacement du joueur
        """
        if key == "q":
            self.moveTo(dy=-1)
            print(self.player.x, self.player.y)
        if key == "d":
            self.moveTo(dy=1)
            print(self.player.x, self.player.y)
        if key == "s":
            self.moveTo(dx=1)
            print(self.player.x, self.player.y)
        if key == "z":
            self.moveTo(dx=-1)
            print(self.player.x, self.player.y)
        if key == "x":
            sys.exit()
