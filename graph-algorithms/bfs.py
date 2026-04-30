from collections import deque
from typing import Dict, Hashable, List, Optional, Set


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


def shortest_path_bfs(
    graph: Dict[Hashable, List[Hashable]],
    start: Hashable,
    goal: Hashable,
) -> Optional[List[Hashable]]:
    if start == goal:
        return [start]

    visited: Set[Hashable] = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            new_path = path + [neighbor]
            if neighbor == goal:
                return new_path
            visited.add(neighbor)
            queue.append((neighbor, new_path))
    return None


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
    print(shortest_path_bfs(graph, 'A', 'F'))
