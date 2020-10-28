"""
Gestion des graphismes
"""
import pygame
import sys
from .constantes import WIDTH, HEIGHT, TILESIZE, MUR_IMG, SERINGUE_IMG
from .constantes import PLAYER_IMG, GARDIEN_IMG, AIGUILLE_IMG, ETHER_IMG
from .map import Labyrinthe

class Graphics:
    """
    Permet de générer les graphismes pygame dans le jeu
    """
    def __init__(self, engine):
        pygame.init()
        self.engine = engine
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")
        self.map = Labyrinthe()
        self.images = {
            "mur" : pygame.image.load(MUR_IMG),
            "player" : pygame.image.load(PLAYER_IMG),
            "gardien" : pygame.image.load(GARDIEN_IMG),
            "aiguille" : pygame.image.load(AIGUILLE_IMG),
            "ether" : pygame.image.load(ETHER_IMG),
            "seringue" : pygame.image.load(SERINGUE_IMG),
        }
        self.events()

    def events(self):
        """
        Gestion des événements Pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.map.movePlayer(key="q")
                    #self.refresh_screen()
                if event.key == pygame.K_RIGHT:
                    self.map.movePlayer(key="d")
                    #self.refresh_screen()
                if event.key == pygame.K_UP:
                    self.map.movePlayer(key="z")
                    #self.refresh_screen()
                if event.key == pygame.K_DOWN:
                    self.map.movePlayer(key="s")
                    #self.refresh_screen()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def refresh_screen(self):
        """
        Rafraîchissement de l'écran à chaque itération de la boucle
        du jeu
        """
        self.screen.fill((0, 0, 0))
        self.draw()

    def draw(self):
        """
        Affichage des images à l'écran
        """
        self.screen.fill((0, 0, 0))
        for x, y in self.map.map:
            if self.map.map[x, y] == "mur":
                self.mur_img = self.images["mur"]
                self.mur_img = pygame.transform.scale(self.mur_img, (TILESIZE, TILESIZE))
                self.screen.blit(self.mur_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "player":
                self.player_img = self.images["player"]
                self.player_img = pygame.transform.scale(self.player_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.player_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "gardien":
                self.gardien_img = self.images["gardien"]
                self.gardien_img = pygame.transform.scale(self.gardien_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.gardien_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "seringue":
                self.seringue_img = self.images["seringue"]
                self.seringue_img = pygame.transform.scale(self.seringue_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.seringue_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "aiguille":
                self.aiguille_img = self.images["aiguille"]
                self.aiguille_img = pygame.transform.scale(self.aiguille_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.aiguille_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "ether":
                self.ether_img = self.images["ether"]
                self.ether_img = pygame.transform.scale(self.ether_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.ether_img, (y*TILESIZE, x*TILESIZE))
        pygame.display.update()
        pygame.display.flip()
