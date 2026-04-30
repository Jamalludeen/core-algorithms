from collections import deque
from typing import Dict, Hashable, List


def topological_sort(graph: Dict[Hashable, List[Hashable]]) -> List[Hashable]:
    in_degree: Dict[Hashable, int] = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node, deg in in_degree.items() if deg == 0])
    order: List[Hashable] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(graph):
        raise ValueError("graph has a cycle, topological sort not possible")
    return order


dag = {
    'shirt': ['tie', 'belt'],
    'tie': ['jacket'],
    'belt': ['jacket'],
    'jacket': [],
    'pants': ['belt', 'shoes'],
    'shoes': [],
}

if __name__ == "__main__":
    print(topological_sort(dag))
