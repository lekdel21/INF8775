# The goal here is to eliminate every space between
# every enclosure.
# solution is a list of enclosures which are a list of coordinates

def swap_initial(solution):
    directions = [(0, -1), (-1, 0)]
    count = len(solution)
    is_optimized = [False] * count
    while count > 0:
        for i, enclosure in enumerate(solution):
            furthest_point = enclosure[-1]
            x, y = enclosure[0]
            for dx, dy in directions:
                x_new, y_new = x + dx, y + dy
                if x_new > 0 and y_new > 0 and not is_coord_already_used((x_new, y_new), solution):
                    enclosure.pop(-1)
                    enclosure.insert(0, (x_new, y_new))
                    x, y = x_new, y_new
                    break
                elif (dx, dy) == (-1, 0) and not is_optimized[i]:
                    count -= 1
                    is_optimized[i] = True
    return solution
                  
    
def is_coord_already_used(coord, solution):
    for enclosure in solution:
        for point in enclosure:
            if coord == point:
                return True
    return False
