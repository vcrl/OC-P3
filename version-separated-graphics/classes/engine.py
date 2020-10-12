from .map import Labyrinthe
from .pygame_graphics import Graphics

class Engine:
    def __init__(self):
        self.map = Labyrinthe()
        self.graphics = Graphics(self)
    def run(self):
        while True:
            self.graphics.draw()
            self.graphics.events()
            inp = input("Clé: ")
            if inp != "inv":
                self.map.movePlayer(key=inp)
                print(self.map.player.x, self.map.player.y)
            else:
                print(self.map.player.inventory)