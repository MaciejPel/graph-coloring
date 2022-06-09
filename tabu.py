from graph_coloring import greedy_coloring, count_confilicts
from graph_read import adjacenecy_list_to_adjacency_matrix, adjacenecy_matrix_to_adjacency_list
from copy import deepcopy

test_subject = [
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [0, 1, 0, 1, 1, 0, 1],
  [0, 0, 1, 0, 1, 0, 0],
  [0, 0, 1, 1, 0, 0, 1],
  [0, 1, 0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 0],
]


def tabu_coloring(adjacency_list, initial_coloring, initial_number_of_colors):
  colors = list(range(initial_number_of_colors))
  # colors = ['Red', 'Yellow', 'Blue', 'Green']
  current_coloring = initial_coloring
  save_result = deepcopy(initial_coloring)
  visit_queue = []
  tabu_list = []
  for k in sorted(adjacency_list, key=lambda k: len(adjacency_list[k]), reverse=True):
    visit_queue.append(k)

  for i in visit_queue:
    current_conflicts = {}
    tabu_list.append(initial_coloring[i])
    for j in colors:
      if j not in tabu_list:
        current_coloring[i] = j
        conflicts = count_confilicts(adjacency_list, current_coloring, i)
        current_conflicts[j] = conflicts
      candidates = sorted(current_conflicts.items(), key=lambda x: x[1][1])
    for color, conflict in candidates:
      tabu_list.append(color)
      current_coloring[i] = color
      win = False
      for k, v in conflict[0].items():
        for h in colors:
          if h not in tabu_list:
            # print(current_coloring, "INITIAL", tabu_list)
            color_check = current_coloring[k]
            current_coloring[k] = h
            conflicts_deeper = count_confilicts(adjacency_list, current_coloring, i)
            if conflict[1] > 0 and k in conflicts_deeper[0]:
              # print("BAD", conflicts_deeper[1], len(set(current_coloring.values())))
              current_coloring[k] = color_check
            elif conflicts_deeper[1]==0 and len(set(current_coloring.values()))<=initial_number_of_colors:
              win = True
              save_result = deepcopy(current_coloring)
              # print("PERFECT", conflicts_deeper[1], len(set(current_coloring.values())))
              break
            else:
              win = True
              # print("GOOD", conflicts_deeper[1], len(set(current_coloring.values())))
              break
      if win == False:
        tabu_list.remove(color)
      else: 
        break
  if count_confilicts(adjacency_list, current_coloring, 1)[1] > 0:
    current_coloring = save_result
  return current_coloring, len(set(current_coloring.values()))

# greedy_result = greedy_coloring(test_subject)
# print(greedy_result)
# print(tabu_coloring(adjacenecy_matrix_to_adjacency_list(test_subject), greedy_result[0], greedy_result[1]))