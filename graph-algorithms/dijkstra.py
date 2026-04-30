import heapq
from typing import Dict, Hashable, List, Optional, Tuple


def dijkstra(
    graph: Dict[Hashable, List[Tuple[Hashable, float]]],
    start: Hashable,
) -> Tuple[Dict[Hashable, float], Dict[Hashable, Optional[Hashable]]]:
    distances: Dict[Hashable, float] = {node: float('inf') for node in graph}
    predecessors: Dict[Hashable, Optional[Hashable]] = {node: None for node in graph}
    distances[start] = 0

    heap: List[Tuple[float, Hashable]] = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))
    return distances, predecessors


def reconstruct_path(
    predecessors: Dict[Hashable, Optional[Hashable]],
    start: Hashable,
    goal: Hashable,
) -> Optional[List[Hashable]]:
    if goal not in predecessors:
        return None
    path: List[Hashable] = []
    node: Optional[Hashable] = goal
    while node is not None:
        path.append(node)
        if node == start:
            return list(reversed(path))
        node = predecessors[node]
    return None


weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

if __name__ == "__main__":
    distances, predecessors = dijkstra(weighted_graph, 'A')
    print(distances)
    print(reconstruct_path(predecessors, 'A', 'D'))
