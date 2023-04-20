from score_calculator import calculate_score
from in_out_file import read_input_file, write_solution_to_file
# from tabu_search import tabu_search
from tabu_search2 import tabu_search_v2
def read_solution_from_file(file_path):
    solution = []
    with open(file_path, 'r') as file:
        for line in file:
            coordinates = line.strip().split()
            enclos = [(float(coordinates[i]), float(coordinates[i+1])) for i in range(0, len(coordinates), 2)]
            solution.append(enclos)
    return solution

input_file_path = "n200_m150_V-68542542.txt"
n, m, k, enclos_bonus, enclos_sizes, enclos_weights = read_input_file(input_file_path)

sol_file_path = "sol_n200_m150_V-68542542.txt"
initial_solution = read_solution_from_file(sol_file_path)
score = calculate_score(initial_solution, enclos_weights, enclos_bonus, k)
print("initial score : {}".format(score))

best_solution = tabu_search_v2(initial_solution, enclos_weights, enclos_bonus, k, 10, 100, neighborhood_size=10, sample_size=10)
write_solution_to_file(best_solution, "bettersol_n200_m150_V-68542542.txt")
score = calculate_score(best_solution, enclos_weights, enclos_bonus, k)
print("better score : {}".format(score))