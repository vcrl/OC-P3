from .pygame_graphics import Graphics
from .map import Labyrinthe

class Engine:
    "Moteur du jeu"
    def __init__(self):
        self.map = Labyrinthe()
        self.graphics = Graphics(self)

    def run(self):
        "Boucle du jeu"
        while True:
            self.graphics.events()
            self.graphics.draw()
