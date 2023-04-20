from score_calculator import calculate_score
from concurrent.futures import ThreadPoolExecutor
import random

def generate_neighborhood(solution):
    neighborhood = []
    for i, enclosure in enumerate(solution):
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_solution = move_enclosure(solution, i, direction)
            if new_solution is not None and not has_overlap_with_other_enclosures(new_solution, i):
                neighborhood.append(new_solution)
    return neighborhood

def has_overlap_with_other_enclosures(solution, enclosure_index):
    current_enclosure = solution[enclosure_index]
    current_enclosure_set = set(current_enclosure)
    for i, enclosure in enumerate(solution):
        if i != enclosure_index and current_enclosure_set.intersection(enclosure):
            return True
    return False

def move_enclosure(solution, enclosure_index, direction):
    dx, dy = direction
    new_enclosure = []

    for cell in solution[enclosure_index]:
        new_cell = (cell[0] + dx, cell[1] + dy)
        new_enclosure.append(new_cell)

    new_solution = solution.copy()
    new_solution[enclosure_index] = new_enclosure
    return new_solution


def has_overlap(enclosure1, enclosure2):
    for cell1 in enclosure1:
        for cell2 in enclosure2:
            if cell1 == cell2:
                return True
    return False


def is_valid_move(solution):
    for enclosure in solution:
        if not is_contiguous(enclosure):
            return False
    return True

def is_contiguous(enclosure):
    visited = set()
    stack = [enclosure[0]]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)

            for neighbor in get_orthogonal_neighbors(current, enclosure):
                if neighbor not in visited:
                    stack.append(neighbor)

    return len(visited) == len(enclosure)

def get_orthogonal_neighbors(cell, enclosure):
    x, y = cell
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [neighbor for neighbor in neighbors if neighbor in enclosure]

def tabu_search(solution, weights, subset, k, max_iterations, tabu_list_size):
    best_solution = solution
    best_score = calculate_score(solution, weights, subset, k)

    tabu_list = []

    for iteration in range(max_iterations):
        print("Iteration {}".format(iteration))
        neighborhood = generate_neighborhood(solution)
        print("ok0")
        with ThreadPoolExecutor() as executor:
            neighborhood_scores = list(executor.map(lambda neighbor: calculate_score(neighbor, weights, subset, k), neighborhood))
        print("ok1")
        # Sort the neighborhood solutions by their scores in descending order
        sorted_indices = sorted(range(len(neighborhood_scores)), key=lambda i: neighborhood_scores[i], reverse=True)
        print("ok2")
        found_non_tabu_move = False
        num_neighbors_to_explore = 10
        for index in sorted_indices[:num_neighbors_to_explore]:
            print("ok3")
            if (solution, neighborhood[index]) not in tabu_list:
                solution = neighborhood[index]
                tabu_list.append((solution, neighborhood[index]))
                found_non_tabu_move = True
                break

        if not found_non_tabu_move:
            solution = random.choice(neighborhood)

        # Update the best solution if the new solution has a better score
        score = calculate_score(solution, weights, subset, k)
        if score > best_score:
            best_solution = solution
            best_score = score

        # Remove the oldest move from the tabu_list if it exceeds the tabu_list_size
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

    return best_solution
