import matplotlib.pyplot as plt
import numpy as np
import math
import random


class Node:
    def __init__(self, row, col):
        self.row = row  # coordinate
        self.col = col  # coordinate
        self.parent = None  # parent node
        self.cost = 0.0  # cost


class RRTx(self, n_pts=1000, neighbor_size=20):
    def __init__(self, map_array, start, goal):
        self.map_array = map_array  # map array, 1->free, 0->obstacle
        self.size_row = map_array.shape[0]  # map size
        self.size_col = map_array.shape[1]  # map size

        self.start = Node(start[0], start[1])  # start node
        self.goal = Node(goal[0], goal[1])  # goal node
        self.vertices = []  # list of nodes
        self.found = False  # found flag

    def init_map(self):
        """Intialize the map before each search
        """
        self.found = False
        self.goal.cost = math.inf
        self.vertices = []
        self.vertices.append(self.start)

    def dis(self, node1, node2):
        """Calculate the euclidean distance between two nodes
        arguments:
            node1 - node 1
            node2 - node 2
        return:
            euclidean distance between two nodes
        """
        return math.dist([node1.row, node1.col], [node2.row, node2.col])

    def check_collision(self, node1, node2):
        """Check if the path between two nodes collide with obstacles
        arguments:
            node1 - node 1
            node2 - node 2

        return:
            True if the new node is valid to be connected
        """
        ### YOUR CODE HERE ###
        row_div = np.linspace(node1.row, node2.row)  # default number of divisions is 50
        col_div = np.linspace(node1.col, node2.col)

        line = zip(row_div, col_div)
        for point in line:
            if self.map_array[int(point[0])][int(point[1])] == 0:
                return False

        return True

    def RRTx(self, n_pts=1000):
        self.init_map()
        print(" --------- RRTx Algorithm ---------- ")

        self.vertices.append[self.start]
        while()
