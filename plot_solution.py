import matplotlib.pyplot as plt
import numpy as np

def plot_enclosures(solution):
    # Find the bounding box of the enclosures
    min_x = min(coord[0] for enclos in solution for coord in enclos)
    max_x = max(coord[0] for enclos in solution for coord in enclos)
    min_y = min(coord[1] for enclos in solution for coord in enclos)
    max_y = max(coord[1] for enclos in solution for coord in enclos)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Create an empty grid
    grid = np.full((height, width), -1, dtype=int)

    # Assign colors to the grid cells
    colors = plt.cm.rainbow(np.linspace(0, 1, len(solution)))

    for i, enclos in enumerate(solution):
        for x, y in enclos:
            grid[y - min_y, x - min_x] = i

    # Display the grid
    plt.imshow(grid, cmap='rainbow', aspect='equal', origin='lower', vmin=-1, vmax=len(solution) - 1)

    # Set the grid
    plt.gca().set_xticks(np.arange(-0.5, width - 0.5, 1))
    plt.gca().set_yticks(np.arange(-0.5, height - 0.5, 1))
    plt.gca().set_xticklabels(np.arange(min_x, max_x + 1, 1))
    plt.gca().set_yticklabels(np.arange(min_y, max_y + 1, 1))
    plt.gca().xaxis.tick_bottom()
    plt.gca().yaxis.tick_left()
    plt.gca().xaxis.set_ticks_position('none')
    plt.gca().yaxis.set_ticks_position('none')

    plt.grid(True, which='both', color='black', linewidth=1)

    plt.show()

def read_solution_file(file_path):
    solution = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            coordinates = [tuple(map(int, coord.strip("()").split(","))) for coord in line.split()]
            solution.append(coordinates)
    return solution

# Read solution from a file
solution = read_solution_file("sol_n20_m15_V-74779.txt")

# Plot the enclosures
plot_enclosures(solution)