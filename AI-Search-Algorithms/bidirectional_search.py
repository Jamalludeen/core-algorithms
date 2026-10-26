from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    forward = deque([start])
    backward = deque([goal])

    parent_forward = {start: None}
    parent_backward = {goal: None}

    while forward and backward:
        for _ in range(len(forward)):
            current = forward.popleft()

            for neighbor in graph[current]:
                if neighbor not in parent_forward:
                    parent_forward[neighbor] = current
                    forward.append(neighbor)

                if neighbor in parent_backward:
                    metting = neighbor
                    return build_path(
                        metting,
                        parent_backward,
                        parent_backward
                    )
                
        for _ in range(len(backward)):
            current = backward.popleft()

            for neighbor in graph[current]:
                if neighbor not in parent_backward:
                    parent_backward[neighbor] = current
                    backward.append(neighbor)

                if neighbor in parent_forward:
                    meeting = neighbor
                    return build_path(
                        meeting,
                        parent_forward,
                        parent_backward
                    )

    # The searches did not connect
    return None


def build_path(meeting, parent_forward, parent_backward):
    # Reconstruct the start-to-meeting section
    left = []
    node = meeting

    while node is not None:
        left.append(node)
        node = parent_forward[node]

    left.reverse()

    # Reconstruct the meeting-to-goal section
    right = []
    node = parent_backward[meeting]

    while node is not None:
        right.append(node)
        node = parent_backward[node]

    return left + right


graph = {
    "S": ["A"],
    "A": ["S", "B", "C"],
    "B": ["A", "D"],
    "C": ["A", "G"],
    "D": ["B", "G"],
    "G": ["C", "D"]
}

path = bidirectional_search(graph, "S", "G")
print("Path:", path)
