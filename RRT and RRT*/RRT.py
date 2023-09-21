import matplotlib.pyplot as plt
import numpy as np
import math
import random

goal_bias = 0.1
max_dist = 20
goal_bias_star = 0.1
max_dist_star = 10


# Class for each tree node
class Node:
    def __init__(self, row, col):
        self.row = row  # coordinate
        self.col = col  # coordinate
        self.parent = None  # parent node
        self.cost = 0.0  # cost


# Class for RRT
class RRT:
    # Constructor
    def __init__(self, map_array, start, goal):
        self.map_array = map_array  # map array, 1->free, 0->obstacle
        self.size_row = map_array.shape[0]  # map size
        self.size_col = map_array.shape[1]  # map size

        self.start = Node(start[0], start[1])  # start node
        self.goal = Node(goal[0], goal[1])  # goal node
        self.vertices = []  # list of nodes
        self.found = False  # found flag

    def init_map(self):
        """Initialize the map before each search
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

    def get_new_point(self, goal_bias):
        """Choose the goal or generate a random point
        arguments:
            goal_bias - the possibility of choosing the goal instead of a random point
        return:
            point - the new point
        """
        ### YOUR CODE HERE ###
        t = random.random()  # Generate a (random)probability value in 0 to 1 range
        new_point = Node(np.random.randint(0, self.size_row), np.random.randint(0, self.size_col))

        return self.goal if t <= goal_bias else new_point

        """ALTERNATIVELY
        return np.random.choice([self.goal, random_node], p=[goal_bias, 1 - goal_bias])
        """

    def get_nearest_node(self, point):
        """Find the nearest node in self.vertices with respect to the new point
        arguments:
            point - the new point
        return:
            the nearest node
        """
        ### YOUR CODE HERE ###
        min_dist = math.inf
        for vertex in self.vertices:
            if self.dis(vertex, point) < min_dist:
                min_dist = self.dis(vertex, point)
                nearest_node = vertex
        return nearest_node

    def extend(self, node1, node2, max_dist):
        dx = node2.row - node1.row
        dy = node2.col - node1.col

        dist = self.dis(node1, node2)

        factor = max_dist / dist
        x_step, y_step = dx * factor, dy * factor
        x = node1.row + x_step
        y = node1.col + y_step

        # Check if out of map
        if x < 0:
            x = 0
        elif x > self.size_row:
            x = self.size_row - 1
        if y < 0:
            y = 0
        elif y > self.size_col:
            y = self.size_col - 1

        new_node = Node(x, y)
        new_node.parent = node1
        new_node.cost = node1.cost + self.dis(new_node, node1)
        return new_node

    def get_neighbors(self, new_node, neighbor_size):
        """Get the neighbors that are within the neighbor distance from the node
        arguments:
            new_node - a new node
            neighbor_size - the neighbor distance
        return:
            neighbors - a list of neighbors that are within the neighbor distance
        """
        ### YOUR CODE HERE ###
        neighbors = []
        for vertex in self.vertices:
            if self.dis(vertex, new_node) < neighbor_size:
                neighbors.append(vertex)
        return neighbors

    def rewire(self, new_node, neighbors):
        """Rewire the new node and all its neighbors
        arguments:
            new_node - the new node
            neighbors - a list of neighbors that are within the neighbor distance from the node
        Rewire the new node if connecting to a new neighbor node will give the least cost.
        Rewire all the other neighbor nodes.
        """
        ### YOUR CODE HERE ###
        for neighbor in neighbors:
            new_cost = new_node.cost + self.dis(neighbor, new_node)
            if new_cost < neighbor.cost and self.check_collision(new_node, neighbor):
                neighbor.cost = new_cost
                neighbor.parent = new_node

    def draw_map(self):
        '''Visualization of the result
        '''
        # Create empty map
        fig, ax = plt.subplots(1)
        img = 255 * np.dstack((self.map_array, self.map_array, self.map_array))
        ax.imshow(img)

        # Draw Trees or Sample points
        for node in self.vertices[1:-1]:
            plt.plot(node.col, node.row, markersize=3, marker='o', color='y')
            plt.plot([node.col, node.parent.col], [node.row, node.parent.row], color='y')

        # Draw Final Path if found
        if self.found:
            cur = self.goal
            while cur.col != self.start.col or cur.row != self.start.row:
                plt.plot([cur.col, cur.parent.col], [cur.row, cur.parent.row], color='b')
                cur = cur.parent
                plt.plot(cur.col, cur.row, markersize=3, marker='o', color='b')

        # Draw start and goal
        plt.plot(self.start.col, self.start.row, markersize=5, marker='o', color='g')
        plt.plot(self.goal.col, self.goal.row, markersize=5, marker='o', color='r')

        # show image
        plt.show()

    def RRT(self, n_pts=1000):
        """RRT main search function
        arguments:
            n_pts - number of points try to sample,
                    not the number of final sampled points
        In each step, extend a new node if possible, and check if reached the goal
        """
        # Remove previous result
        self.init_map()
        print(" --------- RRT Algorithm ---------- ")

        ### YOUR CODE HERE ###

        # In each step,
        # get a new point,
        # get its nearest node,
        # extend the node and check collision to decide whether to add or drop,
        # if added, check if reach the neighbor region of the goal.

        goal_dist = 10
        for n in range(n_pts):
            # Sample new point and get its nearest neighbor in the tree
            new_point = self.get_new_point(goal_bias)
            near_vertex = self.get_nearest_node(new_point)

            # Extend in the direction of the random node if no collision
            extendable = True if (self.dis(near_vertex, new_point) <= max_dist) and (
                    new_point.row != self.goal.row) and (new_point.col != self.goal.col) else False

            step_node = new_point if extendable else self.extend(near_vertex, new_point, max_dist=max_dist)

            if self.check_collision(near_vertex, step_node):
                step_node.parent = near_vertex
                step_node.cost = near_vertex.cost + self.dis(step_node, near_vertex)
                self.vertices.append(step_node)

            if (self.dis(step_node, self.goal) <= goal_dist) and self.check_collision(step_node, self.goal):
                self.found = True
                self.goal.parent = step_node
                self.goal.cost = step_node.cost + self.dis(step_node, self.goal)
                break

        # Output
        if self.found:
            self.vertices.append(self.goal)
            steps = len(self.vertices) - 2
            length = self.goal.cost
            print("It took %d nodes to find the current path" % steps)
            print("The path length is %.2f" % length)
        else:
            print("No path found")

        print(" -------------------------------- ")

        # Draw result
        self.draw_map()

    def RRT_star(self, n_pts=1000, neighbor_size=20):
        '''RRT* search function
        arguments:
            n_pts - number of points try to sample,
                    not the number of final sampled points
            neighbor_size - the neighbor distance

        In each step, extend a new node if possible, and rewire the node and its neighbors
        '''
        # Remove previous result
        self.init_map()
        print(" --------- RRT* Algorithm ---------- ")

        ### YOUR CODE HERE ###

        # In each step,
        # get a new point,
        # get its nearest node,
        # extend the node and check collision to decide whether to add or drop,
        # if added, rewire the node and its neighbors,
        # and check if reach the neighbor region of the goal if the path is not found.

        for n in range(n_pts):
            # Sample new point and get its nearest neighbor in the tree
            new_point = self.get_new_point(goal_bias_star)
            near_vertex = self.get_nearest_node(new_point)

            # Find the node to extend in the direction of new node
            extendable = True if (self.dis(near_vertex, new_point) <= max_dist_star) and (
                    new_point.row != self.goal.row) and (new_point.col != self.goal.col) else False

            step_node = new_point if extendable else self.extend(near_vertex, new_point, max_dist=max_dist_star)

            if self.check_collision(near_vertex, step_node):
                neighbors = self.get_neighbors(step_node, neighbor_size)
                min_node = near_vertex
                min_cost = near_vertex.cost + self.dis(near_vertex, step_node)

                for neighbor in neighbors:
                    if self.check_collision(neighbor, step_node) and (
                            neighbor.cost + self.dis(neighbor, step_node)) < min_cost:
                        min_node = neighbor
                        min_cost = neighbor.cost + self.dis(neighbor, step_node)

                step_node.parent = min_node
                step_node.cost = min_cost
                self.vertices.append(step_node)
                self.rewire(step_node, neighbors)

            # Check for neighbors of goal node and connect if there's a neighbor with lower cost than current goal cost
            # This method keeps exploring the tree, even if goal is reached to find a better path to the goal node
            goal_neighbors = self.get_neighbors(self.goal, neighbor_size)

            for neighbor in goal_neighbors:
                if self.check_collision(neighbor, self.goal) and (
                        neighbor.cost + self.dis(neighbor, self.goal)) < self.goal.cost:
                    self.goal.parent = neighbor
                    self.goal.cost = neighbor.cost + self.dis(neighbor, self.goal)
                    self.found = True

        # Output
        if self.found:
            self.vertices.append(self.goal)
            steps = len(self.vertices) - 2
            length = self.goal.cost
            print("It took %d nodes to find the current path" % steps)
            print("The path length is %.2f" % length)
        else:
            print("No path found")

        print(" -------------------------------- ")

        # Draw result
        self.draw_map()
