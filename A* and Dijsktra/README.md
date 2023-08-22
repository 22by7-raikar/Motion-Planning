# RBE 550 - Basic Search Algorithms Implementation

## Overview

Implementing **BFS** and **DFS**. Visualizing the path found by them.
Files included:

- **search.py** algorithms implementation.
- **main.py** is the script that provides helper functions that load the map from csv files and visualize the map and path.
- **map.csv** is the map file.
- **test_map.csv** restores a test map for doc test purpose only.

## Get Started

**Run**

`python search.py`

When running **search.py** as a main function, it will run a doc test for all the algorithms. It loads **test_map.csv** as the map for testing.
Which just shows that the algorithms are working in this simple **test_map.csv** with its given start and end position. (It may still fail, for example, if you change the goal to an obstacle.)

---

For visualization, please run:

`python main.py`

2 maps shown representing the results of 2 algorithms. As said before, there would be no path shown in the graph as you haven't implemented anything yet. The **main.py** loads the map file **map.csv**, which you are free to modify to create your own map.
