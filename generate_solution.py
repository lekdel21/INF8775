import random
from read_input_file import read_input_file


def generate_contiguous_enclosure(size, used_coordinates):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x_offset, y_offset = random.randint(-1000, 1000), random.randint(-1000, 1000)
    
    enclos = [(x_offset, y_offset)]
    fringe = [(x_offset, y_offset)]
    used_coordinates.add((x_offset, y_offset))

    while len(enclos) < size:
        x, y = fringe.pop(0)
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in used_coordinates:
                enclos.append((nx, ny))
                used_coordinates.add((nx, ny))
                fringe.append((nx, ny))
                break

        if not fringe:
            raise RuntimeError("Failed to generate a contiguous enclosure")

    return enclos

def generate_random_solution(enclos_sizes):
    used_coordinates = set()
    solution = []

    for size in enclos_sizes:
        enclos = generate_contiguous_enclosure(size, used_coordinates)
        solution.append(enclos)

    return solution

def write_solution_to_file(solution, file_path):
    with open(file_path, 'w') as file:
        for enclos in solution:
            coordinates = ' '.join(f"({x},{y})" for x, y in enclos)
            file.write(coordinates + '\n')

# Read input file
input_file_path = "n20_m15_V-74779.txt"
n, m, k, enclos_bonus, enclos_sizes, enclos_weights = read_input_file(input_file_path)

# Generate random solution
random_solution = generate_random_solution(enclos_sizes)

# Write solution to a file
output_file_path = "sol_n20_m15_V-74779.txt"
write_solution_to_file(random_solution, output_file_path)



