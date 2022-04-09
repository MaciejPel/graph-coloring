from random         import choice
from collections    import defaultdict
from os             import system

# PS clear output
def clear():
    system('cls')

# color first vertex, for the rest check connections and assign first available color
def greedy_coloring(matrix):
    colors = list(reversed(range(len(matrix))))
    result = {0: colors[0]}
    for vertex in range(1, len(matrix)):
        temp = colors.copy()
        for edge in range(0, len(matrix[vertex])):
                if matrix[vertex][edge] == 1 and edge in result and result[edge] in temp:
                    temp.remove(result[edge])
        result[vertex] = temp[0]
    return result, len(set(result.values()))

def count_confilicts(adjacency_dict, current_coloring):
    result = defaultdict(list)
    conflicts = 0
    for vertex in range(0, len(adjacency_dict)):
        for edge in adjacency_dict[vertex]:
            if current_coloring[vertex] == current_coloring[edge]:
                conflicts += 1
                if result[vertex]:
                    result[vertex].append(edge)
                else:
                    result[vertex] = [edge]          
    return dict(result), conflicts

def tabu_coloring(matrix, number_of_iterations = 10000):
    colors = list(reversed(range(len(matrix))))
    # colors = ["red", "green", "blue", "cyan", "orange", "black", "white", "yellow", "brown", "pink", "magenta", "grey"]
    tabu_list = []
    result, adjacency_dict = {}, {}
    iterations = 0
    for vertex in range(0, len(matrix)):
        adjacency_dict[vertex] = [(edge) for edge in range(0, len(matrix[vertex])) if matrix[vertex][edge] == 1]
    for vertex in range(0, len(matrix)):
        result[vertex] = choice(colors)
    
    conflicts = count_confilicts(adjacency_dict, result)
    return result

# matrix = [
#     [0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0, 1, 1],
#     [0, 1, 0, 1, 1, 0, 1],
#     [0, 0, 1, 0, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0, 1],
#     [0, 1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 0, 1, 1, 0]
# ]