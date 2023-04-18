import random
from read_input_file import read_input_file
from helper import calculate_score
from swap import swap_initial

def extract_free_cardinal_point(x, y, used_coordinates, directions):
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in used_coordinates:
            return (nx, ny)
    return None

def generate_contiguous_enclosure(size, used_coordinates, ):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x_offset, y_offset = 0, 0
    if len(used_coordinates) != 0: 
        max_x = max(used_coordinates, key=lambda coord: coord[0])[0]
        max_y = max(used_coordinates, key=lambda coord: coord[1])[1]
        x_offset, y_offset = max_x + 1, max_y + 1
        
    
    enclos = [(x_offset, y_offset)]
    fringe = [(x_offset, y_offset)]
    used_coordinates.add((x_offset, y_offset))

    while len(enclos) < size:
        x, y = fringe.pop(0)
        random.shuffle(directions)
        found = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in used_coordinates:
                enclos.append((nx, ny))
                used_coordinates.add((nx, ny))
                fringe.append((nx, ny))
                found = True
                break

        if not found:
            x, y = enclos[0]
            cardinal_point = extract_free_cardinal_point(x, y, used_coordinates, directions)
            if cardinal_point is not None:
                enclos.append(cardinal_point)
                used_coordinates.add(cardinal_point)
                fringe.append(cardinal_point)
                found = True
            if not found:
                raise RuntimeError("Failed to generate a contiguous enclosure")

    return enclos


def generate_random_solution(enclos_sizes, enclos_bonus):
    used_coordinates = set()
    solution = [[]] * len(enclos_sizes)
    print(solution)

    for enclos_number in enclos_bonus:
        size = enclos_sizes[enclos_number]
        enclos = generate_contiguous_enclosure(size, used_coordinates)
        solution[enclos_number] = enclos

    for i, size in enumerate(enclos_sizes):
        is_bonus = False
        for enclos_number in enclos_bonus:
            if i == enclos_number:
                is_bonus = True
                break
        if(not is_bonus):
            enclos = generate_contiguous_enclosure(size, used_coordinates)
            solution[i] = enclos
        

    return solution

def write_solution_to_file(solution, file_path):
    with open(file_path, 'w') as file:
        for enclos in solution:
            coordinates = ' '.join(f"{x} {y}" for x, y in enclos)
            file.write(coordinates + '\n')

# Read input file
input_file_path = "n20_m15_V-74779.txt"
n, m, k, enclos_bonus, enclos_sizes, enclos_weights = read_input_file(input_file_path)

print(enclos_sizes)

# Generate random solution
random_solution = generate_random_solution(enclos_sizes, enclos_bonus)
score = calculate_score(random_solution, enclos_weights, enclos_bonus, k)
print(score)

initial_solution = swap_initial(random_solution)
score = calculate_score(initial_solution, enclos_weights, enclos_bonus, k)
print(score)

# Write solution to a file
output_file_path = "sol_n20_m15_V-74779.txt"
write_solution_to_file(initial_solution, output_file_path)



