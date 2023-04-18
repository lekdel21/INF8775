import sys
from solve import solve

def main():   
    fileName = sys.argv[1]
    show_matrix = sys.argv[2]
    
    solve(fileName, max_tabu_iterations=1000, tabu_tenure=10, max_stochastic_iterations=1000, show_matrix)
    

if __name__ == "__main__":
    main()
