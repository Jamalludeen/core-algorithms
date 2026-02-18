# Graph Algorithms: Graphs, DFS, BFS

This folder contains notes and implementations for core graph concepts and traversals. This README is a compact reference to understand graphs, depth-first search (DFS), and breadth-first search (BFS).

## Graph Basics

### What is a Graph?

A graph is a set of nodes (also called vertices) connected by edges.

Common use cases:

- social networks
- road maps
- dependency graphs
- recommendation systems

### Types of Graphs

- **Directed graph (digraph):** edges have direction (u -> v).
- **Undirected graph:** edges are bidirectional (u -- v).
- **Weighted graph:** edges have weights or costs.
- **Unweighted graph:** all edges have equal cost.
- **Cyclic graph:** has a cycle (a path that returns to a node).
- **Acyclic graph:** no cycles. A directed acyclic graph is a DAG.
- **Connected graph (undirected):** every node is reachable from any other.
- **Tree:** a connected, acyclic, undirected graph with n-1 edges.

### Graph Representations

- **Adjacency list:** for each node, store its neighbors. Efficient for sparse graphs.
- **Adjacency matrix:** N x N matrix; matrix[u][v] indicates if an edge exists. Efficient for dense graphs.
- **Edge list:** store pairs (u, v) or (u, v, w).

Typical time/space tradeoffs:

- adjacency list: O(V + E) space
- adjacency matrix: O(V^2) space

### Basic Graph Terms

- **Degree (undirected):** number of edges incident to a node.
- **In-degree / out-degree (directed):** incoming/outgoing edges.
- **Path:** sequence of nodes connected by edges.
- **Shortest path:** minimum number of edges (unweighted) or minimum weight (weighted).

## DFS (Depth-First Search)

DFS explores as far as possible along each branch before backtracking.

### Intuition

- Think of DFS like exploring a maze by always going forward until you hit a wall, then backtrack.

### Core Behavior

- Use a stack (explicit) or recursion (implicit call stack).
- Mark nodes as visited to avoid infinite loops on cycles.

### Pseudocode (Recursive)

```
DFS(u):
  mark u visited
  for each v in neighbors(u):
    if v not visited:
      DFS(v)
```

### Complexity

- Time: O(V + E) on adjacency list
- Space: O(V) for visited + recursion/stack

### Common Uses

- detect cycles
- topological sort (DAG)
- connected components
- path existence
- maze and puzzle solving

### DFS on Disconnected Graphs

Run DFS from every unvisited node to cover all components.

## BFS (Breadth-First Search)

BFS explores neighbors level by level from a start node.

### Intuition

- Think of BFS like waves expanding outward from the start.

### Core Behavior

- Use a queue.
- Mark nodes as visited when enqueued.

### Pseudocode (Queue)

```
BFS(start):
  queue = [start]
  mark start visited
  while queue not empty:
    u = queue.pop(0)
    for each v in neighbors(u):
      if v not visited:
        mark v visited
        queue.push(v)
```

### Complexity

- Time: O(V + E) on adjacency list
- Space: O(V) for visited + queue

### Common Uses

- shortest path in unweighted graphs
- level order traversal in trees
- bipartite checking

## DFS vs BFS (Quick Contrast)

- DFS: deep first, stack/recursion, good for structure and connectivity
- BFS: level by level, queue, good for shortest paths in unweighted graphs

## Practical Tips

- Always track visited nodes for graphs with cycles.
- For weighted shortest paths, use Dijkstra or Bellman-Ford instead of BFS.
- For huge graphs, iterative DFS avoids recursion depth issues.

## Related Files

- dfs implementation: dfs.py
- dfs practice: dfs_leetcode_problem.py
- tree traversal basics: tree_traversal.py
