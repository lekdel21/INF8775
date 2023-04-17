from helper import objective_function, generate_neighbors
import random

def is_tabu(move, tabu_list):
    # Check if a move is tabu
    return move in tabu_list

def tabu_search(solution, weights, subset, k, max_iterations, tabu_tenure):
    best_solution = solution
    best_value = objective_function(solution, weights, subset, k)
    tabu_list = []

    for _ in range(max_iterations):
        neighbors = generate_neighbors(solution)
        best_neighbor = None
        best_neighbor_value = None

        for neighbor in neighbors:
            move = (solution, neighbor)  # Define a move as a tuple of the current solution and the neighbor
            if is_tabu(move, tabu_list):
                continue

            neighbor_value = objective_function(neighbor, weights, subset, k)
            if best_neighbor is None or neighbor_value > best_neighbor_value:
                best_neighbor = neighbor
                best_neighbor_value = neighbor_value

        if best_neighbor_value > best_value:
            best_solution = best_neighbor
            best_value = best_neighbor_value

        solution = best_neighbor
        tabu_list.append((solution, best_neighbor))
        if len(tabu_list) > tabu_tenure:
            tabu_list.pop(0)
    return best_solution

def stochastic_local_search(solution, weights, subset, k, max_iterations):
    best_solution = solution
    best_value = objective_function(solution, weights, subset, k)

    for _ in range(max_iterations):
        i, j = random.sample(range(len(solution)), 2)
        neighbor = solution[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbor_value = objective_function(neighbor, weights, subset, k)

        if neighbor_value > best_value:
            best_solution = neighbor
            best_value = neighbor_value

    return best_solution