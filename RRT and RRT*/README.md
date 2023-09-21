# RBE 550 - Standard Search Algorithms Implementation

## Overview

In this assignment, I have implemented **RRT** and **RRT*** algorithms. These algorithms were used to find a path in a map of WPI, and the visualized result is attached.

**RRT.py** is the file where I have implemented a RRT class for both the RRT and RRT*.

**main.py** is the script that provides helper functions that load the map from an image and call the classes and functions from **RRT.py**.

**WPI_map.jpg** is a binary WPI map image with school buildings.

Please run
`python main.py`

The **main.py** loads the map image **WPI_map.jpg** and calls classes and functions to run planning tasks. The path will be shown in the graph with the start and end points.

Please keep in mind that, the coordinate system used here is **[row, col]**, which is different from [x, y] in Cartesian coordinates. 

For simplicity, this template uses a class 'Node' and a list 'vertices' in class 'RRT' as a tree structure.

## RRT

In each step, get a new point, get its nearest node, extend the node and check collision to decide whether to add or drop this node. When a new node is added to the tree, the cost and parent of the new node are updated, and a new node is added to the list 'vertices'. If it reaches the neighbor region of the goal, it connects to the goal directly

## RRT*

The first few steps are pretty much the same as RRT. Besides, when a new node is added, the new node and all its neighbor nodes are rewired. Even if a path is found, the algorithm should not stop as adding new nodes will possibly optimize the current found path.
  

