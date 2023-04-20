import heapq
import random
from score_calculator import calculate_score

def generate_random_neighborhood(solution, neighborhood_size):
    neighborhood = set()
    while len(neighborhood) < neighborhood_size:
        i = random.randint(0, len(solution) - 1)
        direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        new_solution = move_enclosure(solution, i, direction)
        if new_solution is not None and not has_overlap_with_other_enclosures(new_solution, i):
            neighborhood.add(tuple(tuple(enclosure) for enclosure in new_solution))
    
    return [list(enclosure) for enclosure in neighborhood]

def has_overlap_with_other_enclosures(solution, enclosure_index):
    for i, enclosure in enumerate(solution):
        if i != enclosure_index and has_overlap(solution[i], solution[enclosure_index]):
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

# New implementation based on QAP solution

def generate_random_neighborhood(solution, neighborhood_size):
    neighborhood = []
    while len(neighborhood) < neighborhood_size:
        i = random.randint(0, len(solution) - 1)
        direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        new_solution = move_enclosure(solution, i, direction)
        if new_solution is not None and not has_overlap_with_other_enclosures(new_solution, i):
            # Convert inner lists to tuples and then convert the entire list to a tuple
            tuple_solution = tuple(tuple(enclosure) for enclosure in new_solution)
            if tuple_solution not in neighborhood:
                neighborhood.append(tuple_solution)
    # Convert back to list of lists before returning
    return [list(enclosure) for enclosure in neighborhood]

def tabu_search_v2(solution, weights, subset, k, max_iterations, tabu_list_size, neighborhood_size, sample_size):
    best_solution = solution
    best_score = calculate_score(solution, weights, subset, k)
    tabu_list = []

    for iteration in range(max_iterations):
        print("Iteration {}".format(iteration))
        
        # Generate a smaller neighborhood
        neighborhood = generate_random_neighborhood(solution, neighborhood_size)

        # Sample 'sample_size' neighbors from the neighborhood
        sampled_neighbors = random.sample(neighborhood, min(sample_size, len(neighborhood)))
        
        # Calculate scores for the sampled neighbors only
        neighborhood_scores = [calculate_score(neighbor, weights, subset, k) for neighbor in sampled_neighbors]

        # Sort the sampled neighbors by their scores in descending order
        sorted_indices = sorted(range(len(neighborhood_scores)), key=lambda i: neighborhood_scores[i], reverse=True)

        found_non_tabu_move = False
        for index in sorted_indices:
            if (solution, sampled_neighbors[index]) not in tabu_list:
                solution = sampled_neighbors[index]
                tabu_list.append((solution, sampled_neighbors[index]))
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