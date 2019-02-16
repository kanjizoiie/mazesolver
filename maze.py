import node
import edge
class Maze():
    edges = []
    nodes = []
    def __init__(self, size):
        self.generate_nodes(size)
        self.generate_edges()
        print(len(self.edges))
    def generate_nodes(self, size):
        # Create a list of nodes, this will represent the tiles in the maze.
        self.nodes = [[node.Node(x, y) for x in range(0, size[0])] for y in range(0, size[1])]
    def generate_edges(self):
        for outer_nodes in self.nodes:
            for node in outer_nodes:
                if (not(node.x >= len(self.nodes) - 1)):
                    self.edges.append(edge.Edge(node, self.nodes[node.x + 1][node.y]))
                if (not(node.y >= len(outer_nodes) - 1)):
                    self.edges.append(edge.Edge(node, self.nodes[node.x][node.y + 1]))
    # TODO: create function to remove edges, thus creating a wall in the maze.