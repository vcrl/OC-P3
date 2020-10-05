from .map import Labyrinthe

class Engine:
    def __init__(self):
        self.map = Labyrinthe()
    def run(self):
        while True:
            print(self.map.player.x, self.map.player.y)
            inp = input("Clé: ")
            if inp != "inv":
                self.map.movePlayer(key=inp)
            else:
                print(self.map.player.inventory)