from typing import Dict, Hashable, List, Optional, Set


def dfs_recursive(
    graph: Dict[Hashable, List[Hashable]],
    node: Hashable,
    visited: Optional[Set[Hashable]] = None,
) -> None:
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, node=neighbor, visited=visited)


def dfs_iterative(
    graph: Dict[Hashable, List[Hashable]],
    start: Hashable,
) -> None:
    visited: Set[Hashable] = set()
    stack: List[Hashable] = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

if __name__ == "__main__":
    print("recursive:", end=" ")
    dfs_recursive(graph, 'A')
    print()

    print("iterative:", end=" ")
    dfs_iterative(graph, 'A')
    print()
