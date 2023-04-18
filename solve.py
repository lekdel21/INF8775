from search import tabu_search, stochastic_local_search
import random


def generate_initial_solution(n):
    # Generate an initial random solution
    return [(-1 + 2 * random.random(), -1 + 2 * random.random()) for _ in range(n)]

def solve_zoo_enclosure_problem(n, weights, subset, k, max_tabu_iterations, tabu_tenure, max_stochastic_iterations):
    initial_solution = generate_initial_solution(n)
    tabu_solution = tabu_search(initial_solution, weights, subset, k, max_tabu_iterations, tabu_tenure)
    final_solution = stochastic_local_search(tabu_solution, weights, subset, k, max_stochastic_iterations)
    return final_solution
