from collections    import defaultdict
from os             import system

# PS clear output
def console_clear():
    system('cls')

# color first vertex, for the rest check connections and assign first available color
def greedy_coloring(matrix):
    colors = list(range(len(matrix)))
    # colors = ['Red', 'Yellow', 'Blue', 'Green']
    result = {0: colors[0]}
    for vertex in range(1, len(matrix)):
        temp = colors.copy()
        for edge in range(0, len(matrix[vertex])):
                if matrix[vertex][edge] == 1 and edge in result and result[edge] in temp:
                    temp.remove(result[edge])
        result[vertex] = temp[0]
    return result, len(set(result.values()))

def count_confilicts(adjacency_dict, current_coloring, perspective):
    result = defaultdict(list)
    conflicts = 0
    for vertex in range(0, len(adjacency_dict)):
        for edge in adjacency_dict[vertex]:
            if current_coloring[vertex] == current_coloring[edge]:
                if vertex != perspective:
                    conflicts += 1
                    if result[vertex]:
                        result[vertex].append(edge)
                    else:
                        result[vertex] = [edge]
    return dict(result), conflicts