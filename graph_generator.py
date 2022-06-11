from random import randrange
from graph_read import adjacenecy_matrix_to_adjacency_list
from graph_coloring import count_confilicts, greedy_coloring, tabu_search

# graph generator from 2nd semester
# todo: create more advanced graph generator
def generate_graph(number_of_vertices, saturation):
    max_number_of_edges = number_of_vertices * (number_of_vertices - 1) / 2
    number_of_required_edges = max_number_of_edges * saturation
    matrix = [[0 for column in range(number_of_vertices)] for row in range(number_of_vertices)]
    number_of_required_edges = number_of_required_edges - number_of_vertices
    for i in range(0, number_of_vertices):
        add_edge(matrix, i, (i + 1) % number_of_vertices)
    for _ in range(0, int(number_of_required_edges / 4)):
        while True:
            x1 = randrange(0, number_of_vertices)
            x2 = randrange(0, number_of_vertices)
            y1 = randrange(0, number_of_vertices)
            y2 = randrange(0, number_of_vertices)
            if x1 == y1 or x2 == y2:
                continue
            if x1 == y2 or x2 == y1:
                continue
            if x1 == x2 or y1 == y2:
                continue
            if (matrix[x1][y1] or matrix[x1][y2] or matrix[x2][y1] or matrix[x2][y2]):
                continue
            break
        add_edge(matrix, x1, y1)
        add_edge(matrix, x1, y2)
        add_edge(matrix, x2, y1)
        add_edge(matrix, x2, y2)
    return matrix

def add_edge(matrix, x, y):
    matrix[x][y] = 1
    matrix[y][x] = 1
    return matrix