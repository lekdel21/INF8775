import sys
from generate_solution import generate_initiale_solution
from in_out_file import read_input_file, write_solution_to_file
from score_calculator import calculate_score
from swap import local_search

def solve(fileName, iterations, show_matrix):
    n, m, k, subset, enclos_sizes, enclos_weights = read_input_file(fileName)

    solution = generate_initiale_solution(enclos_sizes, enclos_weights)

    score = calculate_score(solution, enclos_weights, subset, k)
    print(score)

    solution = local_search(solution, enclos_weights, subset, k, enclos_sizes, 1000)

    output_file_path = "sol_"+filename
    write_solution_to_file(solution, output_file_path)


def main():   
    fileName = sys.argv[1]
    show_matrix = "" 
    if len(sys.argv) == 3: 
        show_matrix = sys.argv[2]
    
    solve(fileName, 100, show_matrix)
    

if __name__ == "__main__":
    main()
