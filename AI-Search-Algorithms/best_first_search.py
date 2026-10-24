from itertools import count
import heapq


def greedy_best_first_search(graph, start, goal, heuristic):
    frontier = [] # list of nodes that have been discovered but have not yet been explored. It acts as the algorithm's waiting list.
    counter = count() # Creates the tie-breaking sequence used when adding nodes to the priority queue.

    # [(7, 0, "S")]
    heapq.heappush(
        frontier, 
        (heuristic[start], next(counter), start)
    )

    
    parent = {start:None} # {"S": None}
    discovered = {start} # Keeps track of nodes already discovered or added to the frontier.
    explored = set() # Stores nodes that have been removed from the frontier and processed.

    while frontier:
        _, _, current = heapq.heappop(frontier)
        explored.add(current)

        if current == goal: # Checks whether the selected node is the goal.
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            return path, explored
    
        for neighbor in graph[current]: # explore the neighbors of the current node
            if neighbor not in discovered: # if the neighor has not been discovered yet
                discovered.add(neighbor) # add to discovered list
                parent[neighbor] = current # track its parent

                heapq.heappush( # push it to the heap
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

