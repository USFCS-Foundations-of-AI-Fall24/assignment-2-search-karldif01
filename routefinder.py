import math

from Graph import Graph, Node, Edge
from queue import PriorityQueue

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    states_generated = 1  # including start stete

    while not search_queue.empty():
        current_state = search_queue.get()

        if goal_test(current_state):
            path = []
            while current_state:
                path.append(current_state.location)
                current_state = current_state.prev_state
            return list(reversed(path)), states_generated

        if use_closed_list:
            if current_state.location in closed_list:
                if closed_list[current_state.location] <= current_state.f:
                    continue
            closed_list[current_state.location] = current_state.f

        for edge in current_state.mars_graph.get_edges(current_state.location):
            new_g = current_state.g + 1  # assuming step cost of 1
            new_state = map_state(
                location=edge.dest,
                mars_graph=current_state.mars_graph,
                prev_state=current_state,
                g=new_g,
                h=heuristic_fn(map_state(location=edge.dest))
            )
            new_state.f = new_state.g + new_state.h
            states_generated += 1  # Count each new state generated

            if use_closed_list and new_state.location in closed_list:
                if closed_list[new_state.location] <= new_state.f:
                    continue

            search_queue.put(new_state)


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    x, y = map(int, state.location.split(','))
    return math.sqrt((x - 1) ** 2 + (y - 1) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    mars_graph = Graph()

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) != 2:
                continue

            current_node = parts[0].strip()
            connected_nodes = parts[1].strip().split()

            if current_node not in mars_graph.g:
                mars_graph.add_node(current_node)

            for connected_node in connected_nodes:
                if connected_node not in mars_graph.g:
                    mars_graph.add_node(connected_node)

                # Only add the edge if it doesn't already exist
                if not mars_graph.get_edge(current_node, connected_node):
                    mars_graph.add_edge(Edge(current_node, connected_node))

    return mars_graph



def main():
    filename = 'MarsMap.txt'
    mars_graph = read_mars_graph(filename)
    print("Mars Graph Structure:")
    print(mars_graph)

    # Assuming the rover starts at position 8,8
    start_location = "8,8"
    start_state = map_state(location=start_location, mars_graph=mars_graph, g=0, h=sld(map_state(location=start_location)))

    # A* with SLD heuristic
    a_star_path, a_star_states = a_star(start_state, sld, lambda state: state.is_goal())

    # Uniform Cost Search (A* with h1 heuristic)
    ucs_path, ucs_states = a_star(start_state, h1, lambda state: state.is_goal())

    # Print results
    print("\nA* Search Results:")

    print("Path found:", " -> ".join(a_star_path))

    print("States generated:", a_star_states)



    print("\nUniform Cost Search Results:")

    print("Path found:", " -> ".join(ucs_path))

    print("States generated:", ucs_states)


if __name__ == "__main__":
    main()


