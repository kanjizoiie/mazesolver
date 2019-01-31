import mazetile

class Maze():
    tiles = []

    def __init__(self, size):
        for x in range(0, size[0]):
            temp = []
            for y in range(0, size[1]):
                temp.append(mazetile.MazeTile())
        self.tiles.append(temp)

    def __str__(self):
        return str(self.tiles)