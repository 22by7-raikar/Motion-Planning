**PRM** algorithm. 

Implement 4 different sampling methods - 
**uniform sampling**
**random sampling**
**gaussian sampling** 
**bridge sampling**

Files included:

**PRM.py** Implements a PRM class with the above four different sampling methods

**main.py** provides helper functions that load the map from an image and call the classes and functions from **PRM.py**.

**WPI_map.jpg** is a binary WPI map image with school buildings.

The **main.py** loads the map image **WPI_map.jpg** and calls classes and functions to run planning tasks. 

When the word '**point**' is used, it refers to a simple list [row, col]. When the word '**node**' or '**vertex**' is used, it refers to a node/vertex in a graph. 

## PRM

The two main phases of PRM are **Learning Phase** and **Query Phase**. 

#### Learning Phase

**Learning Phase** coded in the function `sample`, where it samples points in the map according to different strategy, and connects these points to build a graph. 

In this template, the graph library [Networkx](https://networkx.org/documentation/stable/) is used to store the result graph. 

There are four different sampling methods to be implemented - `uniform_sample`, `random_sample`, `gaussian_sample` and `bridge_sample`. Please refer to the lectures and make sure you understand the ideas behind these sampling methods before coding. 

After sampling, connect these sampling points are connectee to their k nearest neighbors. To find their neighbors, K-D tree is used. 

[example](https://stackoverflow.com/questions/13796782/networkx-random-geometric-graph-implementation-using-k-d-trees) of how to use scipy K-D tree structure. 

All the sampled points and their connection with neighbors are used as nodes and edges to build a Networkx graph.

#### Query Phase

**Query Phase** is in the function `search`, where it search for a path in the constructed graph given a start and goal point.

As start and goal points are not connected to the graph, you will first need to add the start and goal node, find their nearest neighbors in the graph and connect them to these two nodes. Practically, as some of the graphs don't have a good connectivity, we will not only connect the start and goal node to their nearest node, but all the nodes within a certain distance, in order to increase the chance of finding a path.

Having connected start and goal node in the graph, we could use Dijkstra algorithm or any other algorithms we learn before to search for a valid path. This part is already done by using the Dijkstra function Networkx provided.

Finally, as PRM is a multi-query planning algorithms, one could call `search` with other start and goal point. So the previous start and goal nodes and their edges need to be removed in the end of each query phase. This part is also implemented already.
