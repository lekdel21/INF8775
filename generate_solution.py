from in_out_file import read_input_file, write_solution_to_file
import math
import numpy as np
from score_calculator import calculate_score
from swap import get_enclosure_coords, initial_swap, local_search

def generate_initiale_solution(enclos_sizes, enclos_weights):
    n = len(enclos_sizes)
    size = math.ceil(math.sqrt(n))
    solution = [[]] * n
    enclos_number = 0
    for j in range(size):
        for i in range(size):
            if(enclos_number >= n): 
                break
            else:
                solution[enclos_number] = get_enclosure_coords(enclos_sizes[enclos_number], (i*5, j*4))
            enclos_number += 1   
    return solution

