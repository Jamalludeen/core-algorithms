from collections import deque
from typing import Dict, Hashable, List, Set


def bfs(graph: Dict[Hashable, List[Hashable]], start: Hashable) -> None:
    visited: Set[Hashable] = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

if __name__ == "__main__":
    bfs(graph, 'A')
    print()
