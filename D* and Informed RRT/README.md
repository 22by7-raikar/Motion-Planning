  # RBE 550 - Advanced Search Algorithms Implementation

## Overview

In this assignment, you are going to implement **D*** and **Informed RRT*** algorithms.

## Instruction

Run

`python main.py`

For the **Informed RRT***, the **main.py** loads the map image **WPI_map.jpg** and calls classes and functions to run planning tasks.

For the **D***,  the **main.py** loads two maps, a static one and a dynamic one. The static one is for the initial planning, while the dynamic one tells where the new obstacles are.

The coordinate system used here is **[row, col]**, which is different from [x, y] in Cartesian coordinates. 

## D*

Functions included:

1. The **run** function is the main function of the D* algorithm, which includes two main steps. 
The first step is to search from goal to start in the static map. 
The second step is to move from start to goal. If any change is detected in the second step, the cost should be updated and a new path should be replanned.

2. The **process_state** function pops the node from the open list and processes the node and its neighbors based on the state. 
3. The **prepare_repair** function senses the neighbors of the given node and locates the new obstacle nodes for cost modification.
4. The **modify_cost** function modifies the cost from the obstacle node and its neighbor and puts them in the Open list for future search.
5. The **repair_replan** that replans a path from the current node to the goal


**Reference: [Optimal and Efficient Path Planning for Partially-Known Environments](http://web.mit.edu/16.412j/www/html/papers/original_dstar_icra94.pdf).**

## Informed RRT*

1. The first part is within the **main** function of informed RRT, where the c_best - best length of the path, is updated when a path is found. 
2. The second part is within the **sample** function. Different sampling functions can be substituted based on the c_best value. 
3. The last part is within the ellipsoid sampling **get_new_point_in_ellipsoid** so that when a path is found, the samples will be cast within an ellipsoid area for faster convergence.

**Reference: [Informed RRT*: Optimal Sampling-based Path Planning Focused via Direct Sampling of an Admissible Ellipsoidal Heuristic](https://arxiv.org/pdf/1404.2334.pdf).**
