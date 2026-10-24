from itertools import count
import heapq


def greedy_best_first_search(graph, start, goal, heuristic):
    frontier = []
    counter = count()

    heapq.heappush(
        frontier, 
        (heuristic[start], next(counter), start)
    )

    parent = {start:None}
    discovered = {start}
    explored = set()

    while frontier:
        _, _, current = heapq.heappop(frontier)
        explored.add(current)

        if current == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            return path, explored
    
        for neighbor in graph[current]:
            if neighbor not in discovered:
                discovered.add(neighbor)
                parent[neighbor] = current

                heapq.heappush(
                    frontier,
                    (
                        heuristic[neighbor],
                        next(counter),
                        neighbor
                    )
                )
    return None, explored



graph = {
    "S": ["A", "B"],
    "A": ["C"],
    "B": ["D"],
    "C": ["G"],
    "D": ["G"],
    "G": []
}

heuristic = {
    "S": 7,
    "A": 6,
    "B": 4,
    "C": 5,
    "D": 2,
    "G": 0
}

path, explored = greedy_best_first_search(graph, "S", "C", heuristic)
print("Path: ", path)
print("explored: ", explored)

