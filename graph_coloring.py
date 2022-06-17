from collections	import defaultdict, deque
from copy 			import deepcopy
from os				import system
from random         import randrange

# PS clear output
def console_clear():
	system('cls')

# color first vertex, for the rest check connections and assign first available color
def greedy_coloring(matrix):
	colors = list(range(len(matrix)))
	result = {0: colors[0]}
	for vertex in range(1, len(matrix)):
		temp = colors.copy()
		for edge in range(0, len(matrix[vertex])):
			if matrix[vertex][edge] == 1 and edge in result and result[edge] in temp:
				temp.remove(result[edge])
		result[vertex] = temp[0]
	return result, len(set(result.values()))

def count_confilicts(adjacency_dict, current_coloring, exclude_in_return = -1):
	result = defaultdict(list)
	conflicts = 0
	for vertex, edges in adjacency_dict.items():
		for edge in edges:
			if current_coloring[vertex] == current_coloring[edge] and edge not in result and vertex != exclude_in_return:
				conflicts += 1
				if vertex in result:
					result[vertex].append(edge)
				else:
					result[vertex] = [edge]
	return dict(result), conflicts

def tabu_coloring(adjacency_list, number_of_colors, previous_solution, is_first_solution, tabu_size = 7, reps = 40, max_iterations = 10000):
	colors = list(range(number_of_colors))
	iterations = 0
	tabu_list = deque()
	aspiration_dict = {}

	solution = deepcopy(previous_solution)
	if not is_first_solution:
		for i in range(len(adjacency_list)):
			if solution[i] >= number_of_colors:
				solution[i] = colors[randrange(0, len(colors))]

	while iterations < max_iterations:
		candidates = set()
		conflict_count = 0
    
		for vertice, edges in adjacency_list.items():
			for edge in edges:
				if solution[vertice] == solution[edge]:
					candidates.add(vertice)
					candidates.add(edge)
					conflict_count += 1

		candidates = list(candidates)
    
		if conflict_count == 0:
      		# Found a valid coloring.
			break

		new_solution = None
		for _ in range(reps):
			vertice = candidates[randrange(0, len(candidates))]
			new_color = colors[randrange(0, len(colors))]
			if solution[vertice] == new_color:
				new_color = colors[-1]

			new_solution = deepcopy(solution)
			new_solution[vertice] = new_color
			new_conflicts = 0
        
			for vertice, edges in adjacency_list.items():
				for edge in edges:
					if vertice is not None and edge is not None and new_solution[vertice] == new_solution[edge]:
						new_conflicts += 1
			
			if new_conflicts < conflict_count:
				if new_conflicts <= aspiration_dict.setdefault(conflict_count, conflict_count - 1):
					aspiration_dict[conflict_count] = new_conflicts - 1
					if (vertice, new_color) in tabu_list:
						tabu_list.remove((vertice, new_color))
						break
				else:
					if (vertice, new_color) in tabu_list:
						continue
				break

		tabu_list.append((vertice, solution[vertice]))
		if len(tabu_list) > tabu_size:
			tabu_list.popleft()

		solution = deepcopy(new_solution)
		iterations += 1

	if conflict_count != 0:
		print("No coloring found with {} colors.".format(number_of_colors))
		return False, previous_solution
	else:
		print("Found coloring:", len(set(solution.values())))
		return True, solution

def tabu_search(adjacency_list, greedy_result_dict, greedy_result_number):
	first_coloring = True
	result = greedy_result_dict
	for v in range(greedy_result_number, 1, -1):
		status, result = tabu_coloring(adjacency_list, v, result, first_coloring)
		if not status:
			break
		first_coloring = False

	return result, len(set(result.values()))