import sys
from generate_solution import generate_initiale_solution
from in_out_file import read_input_file, write_solution_to_file
from score_calculator import calculate_score

def solve(fileName, iterations, show_solution):
    n, m, k, subset, enclos_sizes, enclos_weights = read_input_file(fileName)

    solution = generate_initiale_solution(enclos_sizes, enclos_weights, subset)

    score = calculate_score(solution, enclos_weights, subset, k)
    if(show_solution):
        print(solution)
    print(score)

    output_file_path = "sol_"+fileName
    write_solution_to_file(solution, output_file_path)


def main():   
    fileName = sys.argv[1]
    show_solution = False 
    if len(sys.argv) == 3: 
        show_solution = sys.argv[2]
    
    solve(fileName, 100, show_solution)
    

if __name__ == "__main__":
    main()
