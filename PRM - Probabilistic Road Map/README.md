## **PRM**

Implemented 4 different sampling methods:

**1. Uniform**

**2. Random**
   
**3. Gaussian**
  
**4. Bridge**


Files included:

**PRM.py** Implements a PRM class with the above four different sampling methods

**main.py** provides helper functions that load the map from an image and call the classes and functions from **PRM.py**.

**WPI_map.jpg** is a binary WPI map image with school buildings.

The **main.py** loads the map image **WPI_map.jpg** and calls classes and functions to run planning tasks. 

## PRM

The two main phases of PRM are the **Learning Phase** and **Query Phase**. 

### Learning Phase

It is coded in the function `sample`, where samples point in the map according to a different strategy, and connects these points to build a graph. 

In this template, the graph library [Networkx](https://networkx.org/documentation/stable/) is used to store the resulting graph. 

After sampling, these sampling points are connected to their k nearest neighbors. To find their neighbors, a [K-D tree](https://stackoverflow.com/questions/13796782/networkx-random-geometric-graph-implementation-using-k-d-trees) is used. 

All the sampled points and their connection with neighbors are used as nodes and edges to build a NetworkX graph.

### Query Phase

This was in the function search, where it searched for a path in the constructed graph given a start and goal point.

**Step 1:** The start and goal points are not connected to the graph. Add the start and goal nodes

**Step 2:** Find their nearest neighbors in the graph, and connect them to these two nodes.

**Step 3:** Some of the graphs don't have good connectivity. So, not only the start and goal nodes but all nodes within a certain distance were connected to increase the chances of finding a path.

**Step 4:** The Dijkstra algorithm was used to search for a valid path. The Dijkstra function provided by Networkx made it convenient to do so.

Finally, as PRM is a multi-query planning algorithm, one could call a search with other start and goal points. 

Therefore, the previous start and goal nodes and their edges needed to be removed at the end of each query phase. This part was also implemented.
