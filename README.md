# Graph coloring with the Tabu Search algorithm

Algorithm and functions made for Combinatorial Optimisation (4th semester). The research focused on metaheuristic methods, their application and differences with the greedy algorithm. The algorithm is supposed to find the best possible solution in 5 minutes.

## Methods

Graph coloring file:

- `greedy_coloring`- find a coloring for a given neighbourhood matrix, greedy method
- `tabu_coloring`- find a coloring for a given adjacency list, focusing on local minimum with a given number of colors to achive
- `tabu_search`- `tabu_coloring` wrapper, forces lower number of colors, continues if there was a positive response

Graph generator file:

- `generate_graph`- generates neighbourhood matrix, prioritizes adjacency over saturation

Graph read file:

- `read_graph`- turns given file path to both adjacency matrix and adjacency list, preferable reading method
- `adjacenecy_list_to_adjacency_matrix`- turns adjacency list into adjacency matrix
- `adjacenecy_matrix_to_adjacency_list`- turns adjacency matrix into adjacency list

Graph request file:

- `request_matrix`- turns given url into adjacency matrix, there are some problems with this method, try using `read_graph` instead

Instances:

- `urls` file- list of example instances found, most of them are available [here](https://mat.gsia.cmu.edu/COLOR/instances.html)
- `tests` folder- test files run during classes
- `benchmarks` folder- files used for measuring relative error between optimum and found solution

## Usage

Any measurment changes should be made in `main.py` file.

## Performance and overall results

Algorithm performed well for small instances and really slow for big ones (e.g. `gc1000` instance). Certainly there could be done some improvements. Overall greedy algorithm works well and any further color reduction is hard make. Nevertheless, the Tabu search method is still able to improve the result- it's mostly 'hit or miss' brute forcing in local minimum, but problem is not trivial so it's necessery.

## Contributing

Pull requests, suggestions and improvements are welcome.
