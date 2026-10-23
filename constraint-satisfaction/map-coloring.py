variables = ["A", "B", "C"]

domains = {
    "A": ["Red", "Green", "Blue"],
    "B": ["Red", "Green", "Blue"],
    "C": ["Red", "Green", "Blue"],
}

# Each pair represents variables that must differ.
constraints = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
]


def is_consistent(variable, value, assignment):
    for left, right in constraints:
        if variable == left and right in assignment:
            if assignment[right] == value:
                return False

        if variable == right and left in assignment:
            if assignment[left] == value:
                return False

    return True


def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment.copy()

    # Select the next unassigned variable.
    variable = next(
        v for v in variables if v not in assignment
    )

    for value in domains[variable]:
        if is_consistent(variable, value, assignment):
            assignment[variable] = value

            result = backtrack(assignment)

            if result is not None:
                return result

            # Undo the choice if it leads to a dead end.
            del assignment[variable]

    return None


solution = backtrack({})
print(solution)