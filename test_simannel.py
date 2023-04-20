from score_calculator import calculate_score
from in_out_file import read_input_file, write_solution_to_file
import time


# from tabu_search import tabu_search
from simulated_anneal import simulated_annealing

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
start = time.time()
best_solution = simulated_annealing(initial_solution, enclos_weights, enclos_bonus, k, 
                                    max_iterations=100, 
                                    initial_temperature=200, 
                                    cooling_rate=0.3)
write_solution_to_file(best_solution, "bettersol_n200_m150_V-68542542.txt")
print("time to execute : {} seconds".format(time.time() - start))
score = calculate_score(best_solution, enclos_weights, enclos_bonus, k)
print("better score : {}".format(score))