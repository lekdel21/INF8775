import random
from score_calculator import calculate_score
from tabu_search import move_enclosure, has_overlap_with_other_enclosures, is_valid_move
from generate_solution import generate_initiale_solution as generate_initial_solution
from in_out_file import read_input_file
import time
# Helper functions

def evaluate_population(population, weights, subset, k):
    return [calculate_score(individual, weights, subset, k) for individual in population]

def local_search(individual, weights, enclos_bonus, k, max_iterations):
    best_individual = individual
    best_score = calculate_score(individual, weights, enclos_bonus, k)
    
    for _ in range(max_iterations):
        for i, enclosure in enumerate(individual):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_individual = move_enclosure(individual, i, (dx, dy))
                new_score = calculate_score(new_individual, weights, enclos_bonus, k)
                
                if new_score < best_score:
                    best_individual = new_individual
                    best_score = new_score

    return best_individual


def selection(population, fitnesses, selection_size):
    selected_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)[:selection_size]
    return [population[i] for i in selected_indices]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual):
    mutated_individual = individual.copy()
    mutation_idx = random.randint(0, len(individual) - 1)
    dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])

    mutated_enclosure = move_enclosure(mutated_individual, mutation_idx, dx, dy)
    if not has_overlap_with_other_enclosures(mutated_enclosure, mutation_idx) and is_valid_move(mutated_enclosure):
        mutated_individual[mutation_idx] = mutated_enclosure

    return mutated_individual

def genetic_algorithm(enclos_sizes, weights, subset, k, population_size=50, generations=100, local_search_iterations=10):
    # Create the initial population
    population = [generate_initial_solution(enclos_sizes, enclos_weights) for _ in range(population_size)]
    # Evaluate initial population
    fitnesses = evaluate_population(population, weights, subset, k)

    for generation in range(generations):
        print("Generation", generation)

        # Apply local search to the population
        for i, individual in enumerate(population):
            improved_individual = local_search(individual, weights, subset, k, local_search_iterations)
            if is_valid_move(improved_individual):
                population[i] = improved_individual
                fitnesses[i] = calculate_score(improved_individual, weights, subset, k)

        # Selection
        mating_pool = selection(population, fitnesses, population_size)

        # Crossover and mutation
        offspring = []
        for _ in range(population_size // 2):
            parent1 = random.choice(mating_pool)
            parent2 = random.choice(mating_pool)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1)
            child2 = mutation(child2)
            offspring.extend([child1, child2])

        # Evaluate offspring
        offspring_fitnesses = evaluate_population(offspring, weights, subset, k)

        # Replacement
        population = offspring
        fitnesses = offspring_fitnesses

    # Return the best individual found
    best_index = fitnesses.index(max(fitnesses))
    return population[best_index]

# Example usage

input_file_path = "n20_m15_V-74779.txt"
n, m, k, enclos_bonus, enclos_sizes, enclos_weights = read_input_file(input_file_path)
start = time.time()
best_solution = genetic_algorithm(enclos_sizes, enclos_weights, enclos_bonus, k, 
                                  population_size=10, generations=10, local_search_iterations=10)


print("time to execute : {} seconds".format(time.time() - start))
score = calculate_score(best_solution, enclos_weights, enclos_bonus, k)
print("better score : {}".format(score))
