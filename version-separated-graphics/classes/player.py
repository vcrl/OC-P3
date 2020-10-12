class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = list()

    def addtoInventory(self, item):
        print(f"{item} ajouté à l'inventaire.")
        self.inventory.append(item)

    def invFull(self):
        #for item in self.map.items.values():
        #    if item in self.inventory:
        #        return True
        if len(self.inventory) == 3:
            return True
        return False