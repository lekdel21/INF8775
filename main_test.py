import sys
import TSP_algorithms as tsp
import time

def main():   

    n = sys.argv[1]
    
    timeGreedy = 0
    distanceGreedy = 0
    timeDynamic = 0
    distacneDynamic = 0
    timeApprox = 0
    distanceApprox = 0

    for i in range(3):

        with open("N" + n + "_" + str(i), 'r') as f:
            lines = f.readlines()
            nCities = int(lines[0])
            coords = [[int(num) for num in line.split()] for line in lines[1:]]

        start = time.time()
        _, distance = tsp.greedy(coords, nCities)
        timeGreedy += (time.time()-start)*1000
        distanceGreedy += distance
        if i == 2:
            print("Greedy (" + str(nCities) + "): ")
            print("\t Time: " + str(timeGreedy/3))
            print("\t Distance: " + str(distanceGreedy/3))

        start = time.time()
        _, distance = tsp.approximative(coords, nCities)
        timeApprox += (time.time()-start)*1000
        distanceApprox += distance
        if i == 2:
            print("Approx: (" + str(nCities) + "): ")
            print("\t Time: " + str(timeApprox/3))
            print("\t Distance: " + str(distanceApprox/3))

        if nCities < 1000:
            start = time.time()
            _, distance = tsp.dynamic(coords, nCities)
            timeDynamic += (time.time()-start)*1000
            distanceDynamic += distance
            if i == 2:
                print("Dynamic: (" + str(nCities) + "): ")
                print("\t Time: " + str(timeDynamic/3))
                print("\t Distance: " + str(distanceDynamic/3))

if __name__ == "__main__":
    main()