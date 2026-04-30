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

if __name__ == "__main__":
    print(has_cycle_undirected(undirected_cyclic))
    print(has_cycle_undirected(undirected_acyclic))
