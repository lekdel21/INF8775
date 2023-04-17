from helper import transpose, attraction

def tabu_search(initial_sol, weights, iterations, list_size):
    current_sol = initial_sol
    best_sol = current_sol
    taboo_list = []
    for _ in range(iterations):
        candidate_sol = transpose(current_sol)
        if candidate_sol not in taboo_list:
            if attraction(candidate_sol, weights) < attraction(current_sol, weights):
                current_sol = candidate_sol
                taboo_list.append(current_sol)
                if len(taboo_list) > list_size:
                    taboo_list.pop(0)
                if attraction(candidate_sol, weights) < attraction(best_sol, weights):
                    best_sol = candidate_sol
    return best_sol



def local_search(initial_sol, weights, iterations):
    current_sol = initial_sol
    for _ in range(iterations):
        candidate_sol = transpose(current_sol)
        if attraction(candidate_sol, weights) < attraction(current_sol, weights):
            current_sol = candidate_sol
    return current_sol