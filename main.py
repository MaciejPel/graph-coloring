from urls               import URLS
from graph_request      import request_matrix
from graph_read         import read_graph
from graph_generator    import generate_graph
from graph_coloring     import *
from os                 import path, listdir
from os.path            import isfile, join

path = path.dirname(path.realpath(__file__)) + "\\tests"
tests_files = [f for f in listdir(path) if isfile(join(path, f))]

clear()

for test in tests_files:
    matrix = read_graph(path + "\\" + test)[0]
    res = greedy_coloring(matrix)
    test = test.replace('.txt', '')

    # tab fix for better visualization
    if len(test)>7:
        print(test, end='\t\t')
    else:
        print(test, end='\t\t\t')
    print(res[1])

for url in URLS:
    matrix = request_matrix(URLS[url])
    res = greedy_coloring(matrix)

    # tab fix for better visualization
    if len(url)>7:
        print(url, end='\t\t')
    else:
        print(url, end='\t\t\t')
    print(res[1])

for i in range(100, 1000, 100):
    for j in range(3, 9):
        print(i, '\t', j/10,'\t', int(i*j/10) ,'\t', greedy_coloring(generate_graph(i, j/10))[1])