from itertools import combinations
from helper import calculate_score
from read_input_file import read_input_file

def read_solution_from_file(file_path):
    solution = []
    with open(file_path, 'r') as file:
        for line in file:
            coordinates = line.strip().split()
            enclos = [(float(coordinates[i]), float(coordinates[i+1])) for i in range(0, len(coordinates), 2)]
            solution.append(enclos)
    return solution

input_file_path = "n20_m15_V-74779.txt"
n, m, k, enclos_bonus, enclos_sizes, enclos_weights = read_input_file(input_file_path)

sol_file_path = "sol_n20_m15_V-74779.txt"
initial_solution = read_solution_from_file(sol_file_path)
score = calculate_score(initial_solution, enclos_weights, enclos_bonus, k)

print(score)
# score = calculate_score()