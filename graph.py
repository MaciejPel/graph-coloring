from collections import defaultdict
from requests import get

URLS = {
    'gc': 'http://www.cs.put.poznan.pl/mmachowiak/instances/gc.txt',
    'gc_500': 'http://www.cs.put.poznan.pl/mmachowiak/instances/gc500.txt',
    'gc_1000': 'http://www.cs.put.poznan.pl/mmachowiak/instances/gc_1000_300013.txt'
}

class Graph:
    def __init__(self, number_of_vertices,  edges) -> None:
        self.number_of_vertices = number_of_vertices
        self.adjacency_matrix = [
            [0 for column in range(number_of_vertices)] 
            for row in range(number_of_vertices)
        ]
        self.connections_dict = defaultdict(list)
    



# test

r = get(URLS['gc'])
print(r.text)

my_graph = Graph(2, [[1,2], [2,1]]);
