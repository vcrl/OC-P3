class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = 0

    def addtoInventory(self, item):
        print(f"{item} ajouté à l'inventaire.")
        self.inventory += 1
        