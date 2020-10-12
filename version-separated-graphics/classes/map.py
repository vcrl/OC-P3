from .player import Player
import os

class Labyrinthe():
    def __init__(self):
        self.map = dict()
        self.map_data = list()
        self.player = Player(0,0)
        #Chargement de la map à chaque instance
        self.loadMap()

    def loadMap(self):
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
                            #self.player = Player(row, col)
                            self.map[row, col] = "player" 
                        elif tile == "G": # Gardien
                            self.map[row, col] = "gardien" 
                        elif tile == "S": # Seringue
                            self.map[row,col] = "seringue"
                        elif tile == "E": # Ether
                            self.map[row,col] = "ether"
                        elif tile == "A": # Aiguille
                            self.map[row,col] = "aiguille"

    def moveTo(self, dx=0, dy=0):
        dir_x = self.player.x + dx
        dir_y = self.player.y + dy
        
        if self.map[dir_x, dir_y] != "mur":
            self.player.x += dx
            self.player.y += dy

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