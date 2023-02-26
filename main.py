import sys
import TSP_algorithms as tsp
import time

def main():   
    
    algorithm = sys.argv[1]
    coordsFile = sys.argv[2]
    showTime = sys.argv[3]
    showPath = sys.argv[4]

    with open(coordsFile, 'r') as f:
        lines = f.readlines()
        nCities = int(lines[0])
        coords = [[int(num) for num in line.split()] for line in lines[1:]]


    start = time.time()

    if algorithm == "glouton":
        path, distance = tsp.greedy(coords, nCities)
        end = time.time()
    
    elif algorithm == "progdyn":
        path, distance = tsp.dynamic(coords, nCities)
        end = time.time()

    elif algorithm == "approx":
        path, distance = tsp.approximative(coords, nCities)
        end = time.time()

    if showPath:
        for i in range(len(path)):
            print(path[i])
    
    if showTime:
        print((end-start)*1000)

    print(distance)
    


if __name__ == "__main__":
    main()