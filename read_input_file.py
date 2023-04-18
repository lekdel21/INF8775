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

# input_file_path = "n20_m15_V-74779.txt"
# n, m, k, enclos_bonus, enclos_sizes, enclos_weights = read_input_file(input_file_path)

# print("n =", n)
# print("m =", m)
# print("k =", k)
# print("Enclos avec bonus :", enclos_bonus)
# print("Tailles des enclos :", enclos_sizes)
# print("Poids des enclos :", enclos_weights)