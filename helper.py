import random
import math

def manhattan_distance(enclos_a, enclos_b):
    min_distance = float('inf')
    for _, u in enumerate(enclos_a):
        for _, v in enumerate(enclos_b):
            distance = abs(u[0] - v[0]) + abs(u[1] - v[1])
            min_distance = min(min_distance, distance)
    return min_distance

def calculate_score(solution, weights, subset, k):
    # Calculate the objective function (V - U) for the given solution
    U = 0
    V = 0

    for i, enclosure_weights in enumerate(weights):
        for j, weight in enumerate(enclosure_weights):
            U += manhattan_distance(solution[i], solution[j]) * weight

    max_distance = 0
    for u in subset:
        for v in subset:
            distance = manhattan_distance(solution[u-1], solution[v-1])
            max_distance = max(max_distance, distance)

    print(max_distance, k)
    if max_distance <= k:
        V = len(subset) ** 2

    return V - U

def generate_neighbors(solution):
    # Generate neighboring solutions by moving or swapping enclosures
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors