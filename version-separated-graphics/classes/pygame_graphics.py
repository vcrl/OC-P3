import pygame, sys
from .map import Labyrinthe

class Graphics:
    def __init__(self, engine):
        pygame.init()
        self.engine = engine
        self.screen = pygame.display.set_mode((32*15, 32*15))
        self.map = Labyrinthe()
        self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("test")
                pygame.quit()
                sys.exit()                        
    
    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        for x, y in self.map.map:
            if self.map.map[x, y] == "mur":
                self.img = pygame.image.load("/home/mint/Documents/_Python/_PygameLab/_OrcEscape/img/mur.png")
                self.img = pygame.transform.scale(self.img, (32, 32))
                self.screen.blit(self.img, (y*32, x*32))
            if self.map.map[x, y] == "player":
                self.img = pygame.image.load("/home/mint/Documents/_Python/_PygameLab/_OrcEscape/img/MacGyver.png")
                self.img = pygame.transform.scale(self.img, (32, 32))
                self.screen.blit(self.img, (y*32, x*32))
        pygame.display.flip()