from timeit             import default_timer as timer
from urls               import URLS
from graph_request      import request_matrix
from graph_generator    import generate_graph
from graph_coloring     import greedy_coloring

# random reversed numbers, to avoid confusion when comparing with result dict
COLORS = list(reversed(range(0, 1500)))

for url in URLS:
    matrix = request_matrix(URLS[url])
    start = timer()
    res = greedy_coloring(matrix, COLORS)
    endtime = timer() - start

    # tab fix for better visualization
    if len(url)>7:
        print(url, end='\t')
    else:
        print(url, end='\t\t')
    print(res[1], end='\t')
    print(endtime)


