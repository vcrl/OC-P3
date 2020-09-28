import pygame
import os

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
                        if tile == "1":
                            self.map[f"{row}, {col}"] = "wall"
                        elif tile == ".":
                            self.map[f"{row}, {col}"] = "ground"
                        elif tile == "x":
                            self.map[f"{row}, {col}"] = "player"


lab = Labyrinthe()
lab.loadMap()
print(lab.map)