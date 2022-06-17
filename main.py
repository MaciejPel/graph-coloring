from graph_coloring		import greedy_coloring, tabu_search
from graph_read			import read_graph
from os					import path, listdir
from os.path			import isfile, join
from time 				import sleep
from multiprocessing	import Process
from sys 				import argv

# Results
# X 	Greedy		11	9	90	155		14
# O 	Genetic? 	7	8	68	124		8
# O 	Tabu ?min 	7	8	65	116		6
# X 	Tabu 5min 	7	8	81	152		6
# X 	Tabu Xmin 	7	8	77	149		6

path = path.dirname(path.realpath(__file__)) + "/tests/"
test_files = [f for f in listdir(path) if isfile(join(path, f))]

if __name__ == "__main__":
	if len(argv) > 1:
		matrix = read_graph(path + argv[1])
		greedy_result = greedy_coloring(matrix[0])
		tabu_result = Process(target = tabu_search, args = (matrix[1], greedy_result[0], greedy_result[1]))
		tabu_result.start()
		sleep(5 * 60)
		tabu_result.terminate()
		tabu_result.join()
	else:
		required_tests = ['queen6.txt', 'miles250.txt', 'gc500.txt', 'gc1000.txt', 'le450_5a.txt']
		processes = []
		greedy_results = {}
		threads_number = 2

		for test in required_tests:
			matrix = read_graph(path + test)
			greedy_result = greedy_coloring(matrix[0])
			greedy_results.setdefault(test, [matrix[0], matrix[1], greedy_result[0], greedy_result[1]])

		for name, result in greedy_results.items():
			for i in range(2):
				p = Process(target = tabu_search, args = (result[1], result[2], result[3]))
				p.start()
				processes.append(p)

		sleep(5 * 60)

		for p in processes:
			p.terminate()
			p.join()
		
