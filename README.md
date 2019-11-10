# Circular Graph Detector
This python script solve the proble find the circular path in graph

### Input
```json
[
    ["(1,1)","(3,1)"], 
    ["(3,1)","(3,3)"], 
    ["(3,3)","(1,3)"], 
    ["(1,3)","(1,1)"]
]
```

### Output
```json
[
    ["(1,3)", "(3,3)", "(3,1)", "(1,1)"]
]
```

### Explanation for graph : find close path
```text
Main logic core of this endpoint is find shape of coordinate, and find all the edge. 
First, we need to parse the input into vertex, in this case, vertex represented by two of point (X,Y). From the input data, we got the edge, but not the adjacency. So we need to know each vertex have adjacency with which another vertex. So we create adjacency list, in there I use dictionary with value set to make sure they join in only one vertex and list adjacency in vertex not redundant.
After we got the adjacency list, we need to do traveling to each edge that connected. To track that path, we use stack. So when we going to another vertex, we push the vertex, if going back, we pop the vertex.
When we traveling, we check the stack of path, if that is not parent (vertex before current vertex) and the point still not yet in stack, we traverse to another vertex. If we check that is not parent and the point is the value of first index in stack, that mean the path is circular, so we need add to new array to save the circular path. In there, I need use temp_variable to save list of set, because set with same value, but different order data will return true, so that can handle redundancy of circular path, and we need another variable to save list of circular path to save the circular path, because list that casting to set will change the order of list, and we need the list to know edge going to where from one vertex to another vertex sequentialy. We use recursive for readable code.  
```