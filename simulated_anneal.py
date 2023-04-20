import random
import math
from score_calculator import calculate_score

def simulated_annealing(solution, weights, subset, k, max_iterations, initial_temperature, cooling_rate):
    current_solution = solution
    current_score = calculate_score(current_solution, weights, subset, k)
    best_solution = current_solution
    best_score = current_score
    temperature = initial_temperature

    for iteration in range(max_iterations):
        # print("Iteration {}".format(iteration))
        new_solution = generate_random_neighbor(current_solution)
        new_score = calculate_score(new_solution, weights, subset, k)
        
        delta_score = new_score - current_score
        
        # Accept the new solution if it has better score or with a probability that depends on the temperature
        if delta_score > 0 or random.random() < math.exp(delta_score / temperature):
            current_solution = new_solution
            current_score = new_score

            if current_score > best_score:
                best_solution = current_solution
                best_score = current_score

        # Update the temperature using the cooling rate
        temperature *= cooling_rate

    return best_solution

def generate_random_neighbor(solution):
    new_solution = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution