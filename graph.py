from collections import defaultdict
from requests import get

URLS = {
    'gc': 'http://www.cs.put.poznan.pl/mmachowiak/instances/gc.txt',
    'gc_500': 'http://www.cs.put.poznan.pl/mmachowiak/instances/gc500.txt',
    'gc_1000': 'http://www.cs.put.poznan.pl/mmachowiak/instances/gc_1000_300013.txt'
}

class Graph:
    def __init__(self) -> None:
        self.number_of_vertices = 0
        self.adjacency_matrix = []
        self.connections_dict = defaultdict(list)
    
    def request_matrix(self, url):
        response = get(url).text.split('\r\n')
        if ' '  in response[0]:
            g.number_of_vertices = len(response)
            for i in range(0, len(response)):
                if response[i] in ['']:
                    pass
                else:
                    row = [int(j) for j in response[i].split(' ')]
                    row_index_numeric_connection = [(x + 1) for x in range(0, len(row)) if row[x] == 1]
                    self.adjacency_matrix.append(row)
                    self.connections_dict[i + 1] = row_index_numeric_connection
        else:
            for i in range(0, len(response)):
                if response[i] in ['']:
                    pass
                elif i == 0:
                    self.number_of_vertices = int(response[0])
                    self.adjacency_matrix = [[0 for column in range(self.number_of_vertices)] for row in range(self.number_of_vertices)]
                else:
                    vertice, destination_vertice = int(response[i].split(' ')[0]), int(response[i].split(' ')[1])
                    self.adjacency_matrix[vertice - 1][destination_vertice - 1], self.adjacency_matrix[destination_vertice - 1][vertice - 1] = 1
                    if self.connections_dict[vertice]:
                        self.connections_dict[vertice].append(destination_vertice)
                        self.connections_dict[destination_vertice].append(vertice)
                    else:
                        self.connections_dict[vertice], self.connections_dict[destination_vertice] = [destination_vertice], [vertice]


                

                
g = Graph()
g.request_matrix(URLS['gc_500'])
print(g.number_of_vertices, '\n', dict(g.connections_dict), '\n', g.adjacency_matrix)
