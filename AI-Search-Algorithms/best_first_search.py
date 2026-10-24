from itertools import count
import heapq

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