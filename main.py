import pygame

class Labyrinthe():
    def __init__(self):
        self.map = dict()
        self.map_data = list()

        #Données du joueur
        self.player_x = ""
        self.player_y = ""

        #Chargement de la map à chaque instance
        self.loadMap()

    def loadMap(self):
        with open("labyrinthe.txt", "rt") as f:
            for line in f:
                self.map_data.append(line)
                for row, tiles in enumerate(self.map_data):
                    for col, tile in enumerate(tiles):
                        if tile == "1": # Mur
                            self.map[f"{row}, {col}"] = "wall" 
                        elif tile == ".": # Chemin
                            self.map[f"{row}, {col}"] = "ground" 
                        elif tile == "x": # Joueur
                            self.map[f"{row}, {col}"] = "player" 
                            self.player_x = row
                            self.player_y = col

class Player():
    def __init__(self):
        Map = Labyrinthe()
        self.x = Map.player_x
        self.y = Map.player_y
    
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

player = Player()
player.movePlayer("z")
player.movePlayer("z")
player.movePlayer("q")

