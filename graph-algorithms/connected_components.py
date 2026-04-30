from typing import Dict, Hashable, List, Set


def connected_components(graph: Dict[Hashable, List[Hashable]]) -> List[List[Hashable]]:
    visited: Set[Hashable] = set()
    components: List[List[Hashable]] = []

    def dfs(node: Hashable, bucket: List[Hashable]) -> None:
        visited.add(node)
        bucket.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, bucket)

    for node in graph:
        if node not in visited:
            bucket: List[Hashable] = []
            dfs(node, bucket)
            components.append(bucket)
    return components


graph = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D', 'E'],
    'D': ['C'],
    'E': ['C'],
    'F': [],
}

if __name__ == "__main__":
    comps = connected_components(graph)
    print(f"count: {len(comps)}")
    for c in comps:
        print(c)
