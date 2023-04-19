def read_input_file(file_path):
    with open(file_path, 'r') as file:
        # Read first line
        n, m, k = map(int, file.readline().split())

        # Read second line
        enclos_bonus = list(map(int, file.readline().split()))

        # Read n lines for enclos sizes
        enclos_sizes = [int(file.readline()) for _ in range(n)]

        # Read n lines for enclos weights
        enclos_weights = [list(map(int, file.readline().split())) for _ in range(n)]

    return n, m, k, enclos_bonus, enclos_sizes, enclos_weights

def write_solution_to_file(solution, file_path):
    with open(file_path, 'w') as file:
        for enclos in solution:
            coordinates = ' '.join(f"{x} {y}" for x, y in enclos)
            file.write(coordinates + '\n')