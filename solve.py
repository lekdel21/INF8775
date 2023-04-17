from search import tabu_search, local_search
from helper import format_solution, load_data
import random

def generate_random_solution(enclosures, weights):
    # Calculate the total number of cells
    total_cells = sum(enclosures)

    # Generate random coordinates for all cells
    coordinates = [(random.randint(-total_cells, total_cells), random.randint(-total_cells, total_cells)) for _ in range(total_cells)]

    # Assign coordinates to enclosures
    initial_solution = []
    coord_index = 0
    for size in enclosures:
        enclosure = []
        for _ in range(size):
            enclosure.append(coordinates[coord_index])
            coord_index += 1
        initial_solution.append(enclosure)

    return initial_solution

def solve(input_file_path, taboo_iterations, taboo_list_size, local_iterations):
    # Load the input data
    enclosures, weights, theme, k = load_data(input_file_path)
    
    # Initialize the solution randomly
    initial_solution = generate_random_solution(enclosures, weights)
    
    #Tabu Search
    tabu_solution, tabu_cost = tabu_search(initial_solution, enclosures, weights, theme, k, taboo_iterations, taboo_list_size)
    
    #Local Search
    final_solution, final_cost = local_search(tabu_solution, enclosures, weights, theme, k, local_iterations)
    
    formatted_solution = format_solution(final_solution)
    
    return formatted_solution