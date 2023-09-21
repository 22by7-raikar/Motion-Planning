# RBE 550 - Basic Search Algorithms Implementation

## Overview

Implemented **Dijkstra** and **A*** algorithms.

Files included:

- **search.py** contains the implementation of the algorithms.
- **main.py** is the script that provides helper functions that load the map from CSV files and visualize the map and path.
- **map.csv** 
- **test_map.csv** restores a test map for doc test purpose only

Run:

`python search.py`

## Details

1. The coordinate system used here is **[row, col]**, which could be different from [x, y] in Cartesian coordinates. 
2. The cost to move each step is set to be 1. The heuristic for each node is its Manhattan distance to the goal.
3. Nodes explored as **"right, down, left, up"**, which means "[0, +1], [+1, 0], [0, -1], [-1, 0]" in coordinates.
