
# color first vertex, for the rest check connections and assign first available color
def greedy_coloring(matrix, colors):
    result = {0: colors[0]}
    for row in range(1, len(matrix)):
        temp = colors
        for element in range(0, len(matrix[row])):
                if matrix[row][element] == 1 and element in result and result[element] in temp:
                    temp.remove(result[element])
        result[row] = temp[0]
    return result, len(set(result.values()))

def tabu_coloring(matrix, colors):
    # todo: Tabu Search
    pass