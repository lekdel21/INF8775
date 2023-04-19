
def transform(solution, n):
    new_solution = [[] for _ in range(n)]
    for y, row in enumerate(solution):
        for x, value in enumerate(row):
            if value is not None:
                new_solution[value].append((x, y))
    return new_solution
