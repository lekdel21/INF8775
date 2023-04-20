from in_out_file import read_input_file, write_solution_to_file
import math
import numpy as np
from score_calculator import calculate_score
from enclosures_manipulation import get_enclosure_coords, add_to_grid

def generate_initiale_solution(enclos_sizes, enclos_weights, subset):
    n = len(enclos_sizes)
    size = math.ceil(math.sqrt(n))
    solution = [[] for _ in range(n)]
    boxes_left = [[] for _ in range(3)] # a list of the spaces left, either under 15, 10 or 5
    enclos_number = 0
    for j in range(size):
        i=0
        while i < size:
            if enclos_number >= n:
                break
            boxes_left, enclos = check_for_spaces(enclos_sizes[enclos_number], boxes_left)
            if enclos!=-1:
                solution[enclos_number] = add_to_grid(enclos_sizes[enclos_number], solution[enclos][0], solution[enclos][-1])
            else:
                solution[enclos_number] = get_enclosure_coords(enclos_sizes[enclos_number], (i*5, j*4))
                boxes_left = add_to_boxes_left(enclos_number, enclos_sizes[enclos_number], boxes_left, 20)
                i += 1  
            enclos_number += 1  
    return solution

def add_to_boxes_left(enclos_number, size, boxes_left, n):
    if size > 15: 
        return boxes_left
    for i in range(3, 0, -1):
        if(n - size >= i * 5):
            boxes_left[i-1].append(enclos_number)
            return boxes_left
    return boxes_left


def check_for_spaces(size, boxes_left):
    for i in range(1, 4):
        if len(boxes_left[i-1]) > 0 and size <= i * 5:
            enclos = boxes_left[i-1].pop(-1)
            return boxes_left, enclos
    return boxes_left, -1

