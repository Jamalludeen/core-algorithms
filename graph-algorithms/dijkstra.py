import heapq
from typing import Dict, Hashable, List, Tuple


def dijkstra(
    graph: Dict[Hashable, List[Tuple[Hashable, float]]],
    start: Hashable,
) -> Dict[Hashable, float]:
    distances: Dict[Hashable, float] = {node: float('inf') for node in graph}
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
                heapq.heappush(heap, (new_dist, neighbor))
    return distances


weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

if __name__ == "__main__":
    print(dijkstra(weighted_graph, 'A'))
