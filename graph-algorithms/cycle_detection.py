from typing import Dict, Hashable, List, Optional, Set


def has_cycle_undirected(graph: Dict[Hashable, List[Hashable]]) -> bool:
    visited: Set[Hashable] = set()

    def dfs(node: Hashable, parent: Optional[Hashable]) -> bool:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


def has_cycle_directed(graph: Dict[Hashable, List[Hashable]]) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2
    color: Dict[Hashable, int] = {node: WHITE for node in graph}

    def dfs(node: Hashable) -> bool:
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True
    return False


undirected_cyclic = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
}

undirected_acyclic = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
}

directed_cyclic = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
}

directed_acyclic = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': [],
}

if __name__ == "__main__":
    print(has_cycle_undirected(undirected_cyclic))
    print(has_cycle_undirected(undirected_acyclic))
    print(has_cycle_directed(directed_cyclic))
    print(has_cycle_directed(directed_acyclic))
