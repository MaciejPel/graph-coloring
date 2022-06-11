from requests		import get
from collections	import defaultdict

# grabbing data by GET request
# add local reading from the file when problems occur
def request_matrix(url):

	adjacency_matrix, connections_dict = [], defaultdict(list)
	response = get(url).text.split('\n')

    # adjacency matrix data input case
	if ' '  in response[0]:
		for i in range(0, len(response)):
			if response[i] in ['', '\r']:
				pass
			else:
				row = [int(j) for j in response[i].split(' ')]
				row_index_numeric_connection = [(x) for x in range(0, len(row)) if row[x] == 1]
				adjacency_matrix.append(row)
				connections_dict[i] = row_index_numeric_connection
	# numeric values data input case
	else:
		for i in range(0, len(response)):
			if response[i] in ['', '\r']:
				pass
			elif i == 0:
				adjacency_matrix = [[0 for column in range(int(response[0]))] for row in range(int(response[0]))]
			else:
				vertice, destination_vertice = int(response[i].split(' ')[0]), int(response[i].split(' ')[1])
				adjacency_matrix[vertice - 1][destination_vertice - 1], adjacency_matrix[destination_vertice - 1][vertice - 1] = 1, 1
				if connections_dict[vertice]:
					if destination_vertice not in connections_dict[vertice]:
						connections_dict[vertice].append(destination_vertice)
				elif connections_dict[destination_vertice]:
					if vertice not in connections_dict[destination_vertice]:
						connections_dict[destination_vertice].append(vertice)
				else:
					connections_dict[vertice], connections_dict[destination_vertice] = [destination_vertice], [vertice]
    # pretty print dictionary with connections
    # for i in sorted(dict(connections_dict)):
        # print(i, sorted(dict(connections_dict)[i]))
	return adjacency_matrix