import pygame

class Labyrinthe():
    def __init__(self):
        self.map = dict()
        self.map_data = list()

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