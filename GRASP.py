import random
from score_calculator import calculate_score
from generate_solution import generate_initiale_solution 
from in_out_file import read_input_file
import time
import math
import sys
import numpy as np

def random_placement(enclosure_sizes, grid_size=20):
    enclosures = []

    for size in enclosure_sizes:
        while True:
            # Choose a random starting point
            start_row, start_col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)

            # Generate random positions for the enclosure
            positions = [(start_row, start_col)]
            for _ in range(size - 1):
                # Choose a random direction (up, down, left, right)
                direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

                # Add the new position
                new_row, new_col = positions[-1][0] + direction[0], positions[-1][1] + direction[1]
                if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                    positions.append((new_row, new_col))

            # Check if this enclosure overlaps with existing enclosures or goes outside the grid
            valid_placement = True
            for pos in positions:
                if not (0 <= pos[0] < grid_size and 0 <= pos[1] < grid_size):
                    valid_placement = False
                    break
                for enc in enclosures:
                    if pos in enc:
                        valid_placement = False
                        break
                if not valid_placement:
                    break

            # If the placement is valid, add the new enclosure and break the loop
            if valid_placement:
                enclosures.append(positions)
                break

    return enclosures


# Helper functions
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def total_attractiveness(enclosures, weights):
    U = 0
    for u in range(len(enclosures)):
        for v in range(u + 1, len(enclosures)):
            min_distance = sys.maxsize
            for p1 in enclosures[u]:
                for p2 in enclosures[v]:
                    min_distance = min(min_distance, manhattan_distance(p1, p2))
            U += min_distance * weights[u][v]
    return U

def is_valid_move(enclosures, enclosure_sizes, new_positions):
    # Check if new_positions are valid (not overlapping with other enclosures or out of the grid)
    for i, new_pos in enumerate(new_positions):
        for j, enc in enumerate(enclosures):
            if i != j:
                for pos in new_pos:
                    if pos in enc:
                        return False
    return True

# Greedy local search with random restart
def greedy_local_search(weights, enclosure_sizes, enclos_bonus, k, n_restarts=100):
    best_enclosures = None
    best_score = sys.maxsize
    
    for _ in range(n_restarts):
        # Initialization
        enclosures = random_placement(enclosure_sizes)
        
        while True:
            improved = False
            
            # Local search
            for i, enc in enumerate(enclosures):
                for j, enc2 in enumerate(enclosures):
                    if i != j:
                        # Swap two enclosures
                        new_positions = enclosures.copy()
                        new_positions[i] = enc2
                        new_positions[j] = enc
                        
                        if is_valid_move(new_positions, enclosure_sizes, enclos_bonus):
                            new_score = total_attractiveness(new_positions, weights)
                            if new_score < best_score:
                                best_score = new_score
                                best_enclosures = new_positions
                                enclosures = new_positions
                                improved = True
                                break
                            
            # Terminate local search when no improvement is found
            if not improved:
                break
    
    # Add the bonus for the subset S
    max_distance = 0
    for i, enc1 in enumerate(enclos_bonus):
        for j, enc2 in enumerate(enclos_bonus):
            if i != j:
                min_distance = sys.maxsize
                for p1 in enclosures[enc1]:
                    for p2 in enclosures[enc2]:
                        min_distance = min(min_distance, manhattan_distance(p1, p2))
                max_distance = max(max_distance, min_distance)
    
    if max_distance <= k:
        best_score -= len(enclos_bonus) ** 2
    
    return best_enclosures, best_score

def calculate_zoo_attraction(enclosures, enclos_weights, enclos_bonus, k):
    # Calculate the total distance-based cost U
    U = 0
    for i, enc1 in enumerate(enclosures):
        for j, enc2 in enumerate(enclosures):
            if i != j:
                min_distance = min(abs(x1 - x2) + abs(y1 - y2) for (x1, y1) in enc1 for (x2, y2) in enc2)
                U += min_distance * enclos_weights[i][j]

    # Calculate the bonus attraction V
    V = 0
    max_distance = 0
    for i in enclos_bonus:
        for j in enclos_bonus:
            if i != j:
                min_distance = min(abs(x1 - x2) + abs(y1 - y2) for (x1, y1) in enclosures[i] for (x2, y2) in enclosures[j])
                max_distance = max(max_distance, min_distance)
    if max_distance <= k:
        V = len(enclos_bonus) ** 2

    # Calculate the total attraction
    total_attraction = V - U
    return total_attraction

# Set the problem parameters
input_file_path = "n200_m150_V-68542542.txt"
n, m, k, enclos_bonus, enclos_sizes, enclos_weights = read_input_file(input_file_path)

# Solve the problem
num_iterations = 10
best_solution = None
best_attraction = float('-inf')
start = time.time()
for it in range(num_iterations):
    print("Iteration {}".format(it))
    initial_solution = random_placement(enclos_sizes)
    # You can implement and call a local search algorithm to improve the initial_solution here
    current_attraction = calculate_zoo_attraction(initial_solution, enclos_weights, enclos_bonus, k)
    
    if current_attraction > best_attraction:
        best_solution = initial_solution
        best_attraction = current_attraction
print("time to execute : {} seconds".format(time.time() - start))
score = calculate_score(best_solution, enclos_weights, enclos_bonus, k)
print("better score : {}".format(score))
