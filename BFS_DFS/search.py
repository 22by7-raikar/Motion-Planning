# Class for each node in the grid
class Node:
    def __init__(self, row, col, is_obs):
        self.row = row  # coordinate
        self.col = col  # coordinate
        self.is_obs = is_obs  # obstacle
        self.parent = None  # previous node

    def trace_path(self):
        """
        Returns path from start_node (node with parent = None) to goal_node
        return:
        path - Path (list)
        """
        # Declare an iterator for going through the nodes
        node = self
        path = []
        while node.parent is not None:
            path.append([node.row, node.col])  # Add each of the nodes to the path
            node = node.parent  # Define the current node's parent as the new current node

        path.append([node.row, node.col])  # Add the start node to the path as start doesn't have a parent out of
        # loop
        return path[::-1]  # Reverse the path as we have added nodes from the goal backwards

    def valid_connections(self, grid, vis):
        """
        This function finds the new nodes resulting from movement along current node
        We need this since connections are not implied in a 2D array as we see in graphs
        """
        dc = [1, 0, -1, 0]
        dr = [0, 1, 0, -1]

        connections = []
        for i in range(4):
            row = self.row + dr[i]
            col = self.col + dc[i]
            # Check if this new node is free or has an obstacle and is free or has an obstacle
            if (row >= 0) and (col >= 0) and (row < len(grid)) and (col < len(grid[0])) and grid[row][col] == 0 and not vis[row][col]:
                connections.append([row, col])
        return connections


def entry(start, goal, grid):
    """ This function initializes the start node, goal node, a visited matrix with False values and
        it also checks if the start or goal node are obstacles to handle errors in input.
    """
    obs = 0
    start_node = Node(start[0], start[1], grid[start[0]][start[1]])
    goal_node = Node(goal[0], goal[1], grid[goal[0]][goal[1]])

    if start_node.is_obs or goal_node.is_obs:
        obs = 1

    vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

    return start_node, goal_node, vis, obs


def bfs(grid, start, goal):
    """Return a path found by BFS alogirhm
       and the number of steps it takes to find it.
    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal -  The goal node in the map. e.g. [2, 2]
    return:
    path -  A nested list that represents coordinates of each step (including start and goal node),
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution,
            i.e. the number of nodes visited before finding a path (including start and goal node)
    >>> from main import load_map
    >>> grid, start, goal = load_map('test_map.csv')
    >>> bfs_path, bfs_steps = bfs(grid, start, goal)
    It takes 10 steps to find a path using BFS
    >>> bfs_path
    [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]]
    """
    ### YOUR CODE HERE ###
    path = []
    steps = 0
    found = False

    start_node, goal_node, vis, obs = entry(start, goal, grid)
    if obs:
        print("No path found")
        return path, steps

    vis[start_node.row][start_node.col] = True

    Q = [start_node]  # Create a queue(A list to store the nodes)---> Q = 0

    while len(Q) > 0:  # ---> while Q!= 0
        curr_node = Q.pop(0)  # ---> u = Dequeue
        steps += 1  # ---> Update number of steps

        if [curr_node.row, curr_node.col] == [goal_node.row, goal_node.col]:
            found = True
            goal_node.parent = curr_node.parent
            break

        # Iterating adjacent node coordinates
        for connection in curr_node.valid_connections(grid, vis):  # --->for each v in G.Adj[u]
            # --->if v.color = GRAY
            # Create a node object out of
            # the visited co-ordinate
            v = Node(connection[0], connection[1], grid[connection[0]][connection[1]])
            v.parent = curr_node  # ---> v.pi = u
            Q.append(v)  # ---> ENQUEUE(Q,v)
            # ---> u.color = BLACK
            vis[v.row][v.col] = True  # v.color = GRAY

    path = goal_node.trace_path()

    if found:
        print(f"It takes {steps} steps to find a path using BFS")
    else:
        print("No path found")
    return path, steps


def dfs(grid, start, goal):
    """Return a path found by DFS alogirhm
       and the number of steps it takes to find it.
    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal -  The goal node in the map. e.g. [2, 2]
    return:
    path -  A nested list that represents coordinates of each step (including start and goal node),
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution,
            i.e. the number of nodes visited before finding a path (including start and goal node)
    >>> from main import load_map
    >>> grid, start, goal = load_map('test_map.csv')
    >>> dfs_path, dfs_steps = dfs(grid, start, goal)
    It takes 9 steps to find a path using DFS
    >>> dfs_path
    [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 3], [3, 3], [3, 2], [3, 1]]
    """
    ### YOUR CODE HERE ###
    path = []
    steps = 0
    found = False

    start_node, goal_node, vis, obs = entry(start, goal, grid)
    if obs:
        print("No path found")
        return path, steps

    #  Iterate for each vertex u belonging to the graph
    found, steps = dfs_visit(grid, start_node, goal_node, vis, steps, found)  # Going to the recursive DFS-VISIT

    path = goal_node.trace_path()  # Find path

    if found:
        print(f"It takes {steps} steps to find a path using DFS")
    else:
        print("No path found")
    return path, steps


def dfs_visit(grid, curr_node, goal_node, vis, steps, found):
    vis[curr_node.row][curr_node.col] = True
    steps += 1  # ---> Increment step/time

    if [curr_node.row, curr_node.col] == [goal_node.row, goal_node.col]:  # End the loop if and once goal is found
        found = True
        goal_node.parent = curr_node.parent
        return found, steps

    # for each node's adjacent to the current node
    for connection in curr_node.valid_connections(grid, vis):
        v = Node(connection[0], connection[1], 0)  # Make of node object
        v.parent = curr_node  # ---> v.pi = u
        found, steps = dfs_visit(grid, v, goal_node, vis, steps, found)  # DFS-Visit(G,v)
        # --->u.color = BLACK
        if found == 1:
            return found, steps
    return found, steps


# Doctest
if __name__ == "__main__":
    # load doc test
    from doctest import testmod, run_docstring_examples

    # Test all the functions
    testmod()
