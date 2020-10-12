from .map import Labyrinthe
from .pygame_graphics import Graphics

class Engine:
    def __init__(self):
        self.map = Labyrinthe()
        self.graphics = Graphics(self)
    def run(self):
        
        while True:
            self.graphics.events()
            self.graphics.draw()
            # récupération du mouvement par rapport aux flèches clavier
            # déclencher la méthode pour bouger le personnage
            # actualiser l'affichage pygame
            # déterminer quelles sont les images à modifier de la forme
            # macgyver était sur la case (3,5), il bouge sur la (3,4)
            # dictionaire_dimages_a_modifier = {
            # (3, 5) : "chemin",
            # (3, 4) : "macgyver"
            # }
            #self.graphics.update(dictionaire_dimages_a_modifier)