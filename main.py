from classes.map import Labyrinthe

if __name__ == "__main__":
    # Boucle du jeu
    running = True
    Map = Labyrinthe()
    while running:
        print(Map.player.x, Map.player.y)
        inp = input("Clé: ")
        if inp != "inv":
            Map.movePlayer(key=inp)
        else:
            print(Map.player.inventory)

