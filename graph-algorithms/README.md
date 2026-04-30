# Graph Algorithms

A collection of small, self-contained graph and tree algorithm implementations
in Python. Every file is runnable directly (`python <file>.py`) and prints a
quick demo against an example graph defined in the same file.

## Modules

| File | What it covers |
| --- | --- |
| `dfs.py` | Recursive and iterative depth-first traversal of a graph. |
| `bfs.py` | Breadth-first traversal and shortest path by edge count. |
| `tree_traversal.py` | Binary search tree with in/pre/post/level-order traversal, search, height, and node count. |
| `dfs_leetcode_problem.py` | LeetCode 104 — maximum depth of a binary tree (recursive and iterative). |
| `cycle_detection.py` | Cycle detection for both undirected and directed graphs. |
| `topological_sort.py` | Topological ordering of a DAG using Kahn's algorithm. |
| `connected_components.py` | Counts and lists connected components in an undirected graph. |
| `dijkstra.py` | Single-source shortest paths with weights, plus path reconstruction. |

## Graph representation

Graphs are represented as plain `dict` adjacency lists:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    ...
}
```

Weighted graphs use tuples `(neighbor, weight)`:

```python
weighted = {
    'A': [('B', 1), ('C', 4)],
    ...
}
```
