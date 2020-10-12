import pygame, sys
from .constantes import *
from .map import Labyrinthe

class Graphics:
    def __init__(self, engine):
        pygame.init()
        self.engine = engine
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")
        self.map = Labyrinthe()
        self.events()

    def events(self):
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
                if event.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()

    def refresh_screen(self):
        self.screen.fill((0, 0, 0))
        self.draw()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        for x, y in self.map.map:

            if self.map.map[x, y] == "mur":
                self.mur_img = pygame.image.load(MUR_IMG)
                self.mur_img = pygame.transform.scale(self.mur_img, (TILESIZE, TILESIZE))
                self.screen.blit(self.mur_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "player":
                try:
                    self.player_img.kill()
                except Exception:
                    self.player_img = pygame.image.load(PLAYER_IMG)
                    self.player_img = pygame.transform.scale(self.player_img,
                    (TILESIZE, TILESIZE))
                    self.screen.blit(self.player_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "gardien":
                self.gardien_img = pygame.image.load(GARDIEN_IMG)
                self.gardien_img = pygame.transform.scale(self.gardien_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.gardien_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "seringue":
                self.seringue_img = pygame.image.load(SERINGUE_IMG)
                self.seringue_img = pygame.transform.scale(self.seringue_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.seringue_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "aiguille":
                self.aiguille_img = pygame.image.load(AIGUILLE_IMG)
                self.aiguille_img = pygame.transform.scale(self.aiguille_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.aiguille_img, (y*TILESIZE, x*TILESIZE))

            if self.map.map[x, y] == "ether":
                self.ether_img = pygame.image.load(ETHER_IMG)
                self.ether_img = pygame.transform.scale(self.ether_img,
                (TILESIZE, TILESIZE))
                self.screen.blit(self.ether_img, (y*TILESIZE, x*TILESIZE))
        pygame.display.update()
        pygame.display.flip()
