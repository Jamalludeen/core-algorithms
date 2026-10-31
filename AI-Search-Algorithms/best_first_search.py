
from itertools import count
import heapq


def reconstruct_path(parent, goal):
    """
    Reconstruct the path from the start node to the goal.
    """
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def greedy_best_first_search(graph, start, goal, heuristic):
    """
    Greedy Best-First Search.

    Evaluation function:
        f(n) = h(n)

    Returns:
        path: Path from start to goal, or None.
        explored: Nodes that were expanded.
        statistics: Search statistics.
    """

    # --------------------------------------------------
    # 1. Validate inputs
    # --------------------------------------------------

    if start not in graph:
        raise ValueError(f"Start node '{start}' is not in the graph.")

    if goal not in graph:
        raise ValueError(f"Goal node '{goal}' is not in the graph.")

    for node, neighbors in graph.items():
        if node not in heuristic:
            raise ValueError(f"Missing heuristic for node '{node}'.")

        for neighbor in neighbors:
            if neighbor not in graph:
                raise ValueError(
                    f"Neighbor '{neighbor}' is not defined in the graph."
                )

            if neighbor not in heuristic:
                raise ValueError(
                    f"Missing heuristic for neighbor '{neighbor}'."
                )

    # --------------------------------------------------
    # 2. Initialize search structures
    # --------------------------------------------------

    frontier = []

    # Prevents heap entries from being compared by node value
    # when heuristic values are equal.
    counter = count()

    # Stores the predecessor of each discovered node.
    parent = {start: None}

    # Nodes that have been discovered.
    discovered = {start}

    # Nodes that have been expanded.
    explored = set()

    # Search statistics.
    statistics = {
        "nodes_discovered": 1,
        "nodes_expanded": 0,
        "nodes_generated": 1,
        "max_frontier_size": 1
    }

    # Add the starting node to the priority queue.
    heapq.heappush(
        frontier,
        (heuristic[start], next(counter), start)
    )

    # --------------------------------------------------
    # 3. Main search loop
    # --------------------------------------------------

    while frontier:

        # Select the node with the lowest heuristic value.
        _, _, current = heapq.heappop(frontier)

        # Skip nodes already expanded.
        if current in explored:
            continue

        # Mark current node as expanded.
        explored.add(current)
        statistics["nodes_expanded"] += 1

        # --------------------------------------------------
        # 4. Goal test
        # --------------------------------------------------

        if current == goal:
            path = reconstruct_path(parent, goal)

            return path, explored, statistics

        # --------------------------------------------------
        # 5. Expand neighbors
        # --------------------------------------------------

        for neighbor in graph[current]:

            # Ignore previously discovered nodes.
            if neighbor in discovered:
                continue

            # Record discovery and parent.
            discovered.add(neighbor)
            parent[neighbor] = current

            statistics["nodes_discovered"] += 1
            statistics["nodes_generated"] += 1

            # Insert neighbor into priority queue.
            heapq.heappush(
                frontier,
                (
                    heuristic[neighbor],
                    next(counter),
                    neighbor
                )
            )

        # Track maximum frontier size.
        statistics["max_frontier_size"] = max(
            statistics["max_frontier_size"],
            len(frontier)
        )

    # --------------------------------------------------
    # 6. Goal was not reachable
    # --------------------------------------------------

    return None, explored, statistics


# ======================================================
# Example graph
# ======================================================

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


# ======================================================
# Run search
# ======================================================

path, explored, statistics = greedy_best_first_search(
    graph=graph,
    start="S",
    goal="C",
    heuristic=heuristic
)

