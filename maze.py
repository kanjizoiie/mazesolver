import node
class Maze():
    edges = []
    nodes = []
    def __init__(self, size):
        # Create a list of nodes, this will represent the tiles in the maze.
        self.nodes = [node.Node(x / size[0], x / size[1]) for x in range(0, size[0] * size[1])]
        print(len(self.nodes))

        # TODO: Build edges for the maze, where an edge removes a wall between two nodes in the maze.
        