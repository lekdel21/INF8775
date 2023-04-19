from score_calculator import calculate_score
import math
import numpy as np

def local_search(solution, weights, subset, k, enclos_sizes, iterations):
    current_score = calculate_score(solution, weights, subset, k)
    while iterations > 0:
        iterations -= 1
        i, j = np.random.choice(len(solution), size=2, replace=False)
        neighbor_solution = swap_enclosures(solution, i, j, enclos_sizes)
        neighbor_score = calculate_score(neighbor_solution, weights, subset, k)
        if neighbor_score > current_score:
            solution = neighbor_solution
            current_score = neighbor_score
            print(current_score)
    return solution

def initial_swap(solution, weights, subset, k, enclos_sizes, old_score):
    for j in range(len(weights)):
        for i in range(j+1, len(weights)):
            solution, old_score = swap_enclosure(solution, i, j, weights, subset, k, enclos_sizes, old_score)
    return solution
            
def swap_enclosure(solution, i, j, weights, subset, k, sizes, old_score):
    new_solution = solution.copy()
    new_solution[i] = get_enclosure_coords(sizes[i], solution[j][0])
    new_solution[j] = get_enclosure_coords(sizes[j], solution[i][0])
    new_score = calculate_score(new_solution, weights, subset, k)
    if(old_score > new_score):
        return solution, old_score
    else: 
        return new_solution, new_score
        

def swap_enclosures(solution, i, j, sizes):
    new_solution = solution.copy()
    new_solution[i] = get_enclosure_coords(sizes[i], solution[j][0])
    new_solution[j] = get_enclosure_coords(sizes[j], solution[i][0])
    return new_solution


def get_enclosure_coords(size, start_point):
    enclosure_coords = []
    x, y = start_point
    dx_max = 5
    dy_max = 4
    count = 0
    for j in range(dy_max):
        for i in range(dx_max):
            count += 1
            if (count) > size: 
                break
            enclosure_coords.append((x+i,y+j))

    return enclosure_coords