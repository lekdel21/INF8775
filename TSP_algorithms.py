import math
import heapq

def createGraph(coords, nCities):
    
    graph = [[0] * nCities for i in range(nCities)]
    
    for i in range(nCities):
        for j in range(i + 1, nCities):
            
            distance = round(math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2))
            graph[i][j] = distance
            graph[j][i] = distance
    
    return graph


def greedy(coords, nCities):
    
    graph = createGraph(coords, nCities)

    startCity = 0
    visited_set = set([startCity])
    path = [startCity]

    for i in range(nCities - 1):
        
        closestNeighbor = None
        smallestDist = float('inf')
        
        for j in range(nCities):
            
            if j not in visited_set and graph[path[-1]][j] < smallestDist:
                closestNeighbor = j
                smallestDist = graph[path[-1]][j]

        visited_set.add(closestNeighbor)
        path.append(closestNeighbor)

    distance = sum(graph[path[i]][path[(i+1)%nCities]] for i in range(nCities))

    return path, distance



def dynamic(coords, nCities):

    graph = createGraph(coords, nCities)

    dynamicTable = [[None] * nCities for i in range(2**nCities)]
    for i in range(nCities):
        dynamicTable[2**i][i] = 0
    
    for k in range(1, 2**nCities):
        for i in range(nCities):
            
            if k & (1 << i):
                continue

            for j in range(nCities):
                
                if k & (1 << j):
                    subproblem = k | (1 << i)
                    
                    if dynamicTable[subproblem][i] is None or dynamicTable[subproblem][i] > dynamicTable[k][j] + graph[j][i]:
                        dynamicTable[subproblem][i] = dynamicTable[k][j] + graph[j][i]

    path = [0]
    k = 2**nCities - 2
    distance = 0
    
    for i in range(nCities - 1):
        
        nextCity = None
        samllestDist = float('inf')

        for j in range(nCities):
            
            if j == path[-1] or not k & (1 << j):
                continue

            distJ = dynamicTable[k][j] + graph[j][path[-1]]
            
            if distJ < samllestDist:
                nextCity = j
                samllestDist = distJ

        path.append(nextCity)
        k &= ~(1 << nextCity)
        distance += graph[path[-2]][path[-1]]

    path.append(0)
    distance += graph[path[-2]][path[-1]]

    return path, distance




def approximative(coords, nCities):
    graph = createGraph(coords, nCities)
    
    visited_set = set([0])
    path = [0]

    priorityQueue = []
    for i in range(1, nCities):
        heapq.heappush(priorityQueue, (graph[0][i], i))
    
    while priorityQueue:
        _, i = heapq.heappop(priorityQueue)
        
        if i in visited_set:
            continue
        
        visited_set.add(i)
        path.append(i)

        if len(path) == nCities:
            break

        for j in range(nCities):
            if j not in visited_set:
                heapq.heappush(priorityQueue, (graph[i][j], j))
    
    path.append(0)

    distance = sum(graph[path[i]][path[(i+1)%nCities]] for i in range(nCities))
    
    return path, distance