import pygame

class Labyrinthe():
    def __init__(self):
        self.map = dict()
        self.map_data = list()

        #Données du joueur
        self.player_x = ""
        self.player_y = ""

        #Données des objets
        

        #Chargement de la map à chaque instance
        self.loadMap()

    def loadMap(self):
        with open("labyrinthe.txt", "rt") as f:
            for line in f:
                self.map_data.append(line)
                for row, tiles in enumerate(self.map_data):
                    for col, tile in enumerate(tiles):
                        if tile == "1": # Mur
                            self.map[row, col] = "mur" 
                        elif tile == ".": # Chemin
                            self.map[row, col] = "chemin" 
                        elif tile == "X": # McGyver
                            self.map[row, col] = "player" 
                            self.player_x = row
                            self.player_y = col
                        elif tile == "G": # Gardien
                            self.map[row, col] = "gardien" 
                        elif tile == "S": # Seringue
                            self.map[row,col] = "seringue"
                        elif tile == "E": # Ether
                            self.map[row,col] = "ether"
                        elif tile == "A": # Aiguille
                            self.map[row,col] = "aiguille"
                

class Player():
    def __init__(self):
        self.map = Labyrinthe()
        self.x = self.map.player_x
        self.y = self.map.player_y

        self.inventory = list()
    
    def movePlayer(self, key):
        if key == "z":
            self.y += 1
            print(self.x, self.y)
        elif key == "s":
            self.y -= 1
            print(self.x, self.y)
        elif key == "q":
            self.x -= 1
            print(self.x, self.y)
        elif key == "d":
            self.x += 1
            print(self.x, self.y)
    
    def solidTile(self):
        for x, y in self.map.map:
            print(x, y)

    def addtoInventory(self, item):
        pass

player = Player()
player.movePlayer("z")
player.solidTile()