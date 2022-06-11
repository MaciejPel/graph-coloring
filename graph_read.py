from collections import defaultdict

def read_graph(path):
	adjacency_matrix, adjacency_list = [], defaultdict(list)

	def strip_split_int(line):
		line = line.strip().split(' ')
		line = [int(element) for element in line]
		return line

	with open(path) as f:
		content = f.readlines()
		if content[0].strip().count(' '):
			for line in content:
				adjacency_matrix.append(strip_split_int(line))
			adjacency_list = adjacenecy_matrix_to_adjacency_list(adjacency_matrix)
		else:
			for line in content:
				line = strip_split_int(line)
				if len(line) == 1:
					continue
				line = [element - 1 for element in line]
				if line[1] not in adjacency_list[line[0]]:
					adjacency_list[line[0]].append(line[1])
				if line[0] not in adjacency_list[line[1]]:
					adjacency_list[line[1]].append(line[0])
			# for elem_list in adjacency_list:
			# 	adjacency_list[elem_list].sort()
			adjacency_matrix = adjacenecy_list_to_adjacency_matrix(adjacency_list, int(content[0].strip()))

	return adjacency_matrix, adjacency_list

def adjacenecy_list_to_adjacency_matrix(dictionary, number_of_vertices):
	adjacency_matrix = [[0 for column in range(number_of_vertices)] for row in range(number_of_vertices)]
	for key in sorted(dictionary):
		for element in dictionary[key]:
			if element:
				adjacency_matrix[key][element] = 1
				adjacency_matrix[element][key] = 1

	return adjacency_matrix

def adjacenecy_matrix_to_adjacency_list(matrix):
	adjacency_list = defaultdict(list)
	for row in range(0, len(matrix)):
		for element in range(0, len(matrix[row])):
			if matrix[row][element] == 1:
				adjacency_list[row].append(element)
			# if row not in adjacency_list:
			# 	adjacency_list[row].append(None)

	return dict(adjacency_list)
