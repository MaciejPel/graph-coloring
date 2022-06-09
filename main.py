from urls               import URLS
from graph_request      import request_matrix
from graph_coloring     import *
from tabulate           import tabulate
from tabu               import tabu_coloring
from graph_read         import adjacenecy_matrix_to_adjacency_list

# from graph_read         import read_graph
# from os                 import path, listdir
# from os.path            import isfile, join

# path = path.dirname(path.realpath(__file__)) + "\\tests"
# tests_files = [f for f in listdir(path) if isfile(join(path, f))]

console_clear()
data = []
# Greedy  11  9   90  155 14
# Genetic 7   8   68  124 8

for url in URLS:
    matrix = request_matrix(URLS[url])
    greedy_result = greedy_coloring(matrix)
    tabu_result = tabu_coloring(adjacenecy_matrix_to_adjacency_list(matrix), greedy_result[0], greedy_result[1])
    data.append([url, greedy_result[1], '\n\n\n', tabu_result[1]])
    
print(tabulate(data, headers=["Instance", "Greedy", "Tabu"]))