import random

def transpose(sol):
    sol_copy = [list(enclosure) for enclosure in sol]
    i = random.randrange(len(sol))
    j = random.randrange(len(sol))
    while i == j:
        j = random.randrange(len(sol))
    x_shift = random.choice([-1, 0, 1])
    y_shift = random.choice([-1, 0, 1])
    while x_shift == 0 and y_shift == 0:
        x_shift = random.choice([-1, 0, 1])
        y_shift = random.choice([-1, 0, 1])
    for idx, (x, y) in enumerate(sol_copy[j]):
        sol_copy[j][idx] = (x + x_shift, y + y_shift)
    return sol_copy


def attraction(sol, weights):
    score = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            if i != j:
                min_distance = float('inf')
                for x1, y1 in sol[i]:
                    for x2, y2 in sol[j]:
                        min_distance = min(min_distance, abs(x1 - x2) + abs(y1 - y2))
                score += weights[i][j] * min_distance
    return score

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n, m, k = map(int, lines[0].split())
        theme = list(map(int, lines[1].split()))
        enclosures = [int(x) for x in lines[2:2 + n]]
        weights = [list(map(int, x.split())) for x in lines[2 + n:]]
    return n, m, k, theme, enclosures, weights


def format_solution(final_sol):
    formatted_solution = ""
    for enclosure in final_sol:
        for coord in enclosure:
            formatted_solution += f"{coord[0]} {coord[1]} "
        formatted_solution = formatted_solution.strip()
        formatted_solution += "\n"
    return formatted_solution

def load_data(input_file_path):
    with open(input_file_path, "r") as file:
        lines = file.readlines()

        n, m, k = map(int, lines[0].strip().split())
        theme = list(map(int, lines[1].strip().split()))

        enclosures = []
        for line in lines[2:n+2]:
            enclosures.append(int(line.strip()))

        weights = []
        for line in lines[n+2:]:
            weights.append(list(map(int, line.strip().split())))

    return enclosures, weights, theme, k



