import pygame

class Labyrinthe():
    def __init__(self):
        self.map = dict()
        self.map_data = list()

        #Données du joueur
        self.player_x = 0
        self.player_y = 0

        #Données des objets
        self.walls = dict()
        self.items = dict()
        self.npc = dict()

        #Chargement de la map à chaque instance
        self.loadMap()

    def loadMap(self):
        with open("labyrinthe.txt", "r") as f:
            for line in f:
                self.map_data.append(line)
                for row, tiles in enumerate(self.map_data):
                    for col, tile in enumerate(tiles):
                        if tile == "1": # Mur
                            self.map[row, col] = "mur" 
                        elif tile == ".": # Chemin
                            self.map[row, col] = "chemin" 
                        elif tile == "P": # McGyver
                            self.map[row, col] = "player" 
                            self.player_x = row
                            self.player_y = col
                        elif tile == "G": # Gardien
                            self.map[row, col] = "gardien" 
                            self.npc[row, col] = "gardien"
                        elif tile == "S": # Seringue
                            self.map[row,col] = "seringue"
                            self.items[row, col] = "seringue"
                        elif tile == "E": # Ether
                            self.map[row,col] = "ether"
                            self.items[row, col] = "ether"
                        elif tile == "A": # Aiguille
                            self.map[row,col] = "aiguille"
                            self.items[row, col] = "aiguille"

        self.isWall()

    def isWall(self):
        for x, y in self.map:
            if self.map[x, y] == "mur":
                self.walls[x, y] = "mur"
                

class Player():
    def __init__(self):
        self.map = Labyrinthe()
        self.x = self.map.player_x
        self.y = self.map.player_y

        self.inventory = list()
    
    def move(self, dx=0, dy=0):
        if not self.isSolid(dx, dy):
            self.x += dx
            self.y += dy

    def movePlayer(self, key):
        self.pickItem()
        if key == "q":
            self.move(dy=-1)
            print(self.x, self.y)
        if key == "d":
            self.move(dy=1)
            print(self.x, self.y)
        if key == "s":
            self.move(dx=1)
            print(self.x, self.y)
        if key == "z":
            self.move(dx=-1)
            print(self.x, self.y)

    def isSolid(self, dx=0, dy=0):
        walls = self.map.walls
        for x, y in walls:
            if self.x + dx == x and self.y + dy == y:
                return True
        return False
           
    def pickItem(self):
        items = self.map.items.copy()
        for x, y in items:
            if self.x == x and self.y == y:
                if items[x, y] == "seringue":
                    if "seringue" not in self.inventory:
                        self.addtoInventory("seringue")
                        print("Seringue ajoutée à l'inventaire.")
    
                elif items[x, y] == "ether":
                    if "ether" not in self.inventory:
                        self.addtoInventory("ether")
                        print("Ether ajouté à l'inventaire.")
                        
                elif items[x, y] == "aiguille":
                    if "aiguille" not in self.inventory:
                        self.addtoInventory("aiguille")
                        print("Aiguille ajoutée à l'inventaire.")

    def addtoInventory(self, item):
        self.inventory.append(item)

    def invFull(self):
        #for item in self.map.items.values():
        #    if item in self.inventory:
        #        return True
        if len(self.inventory) == 3:
            return True

    def winGame(self):
        for x, y in self.map.npc:
            if self.map.npc[x, y] == "gardien":
                if self.x == x and self.y == y:
                    if self.invFull:
                        print("Vous avez gagné!")

if __name__ == "__main__":
    running = True
    player = Player()
    while running:
        inp = input("Clé de déplacement : ")
        player.movePlayer(key=inp)
    
