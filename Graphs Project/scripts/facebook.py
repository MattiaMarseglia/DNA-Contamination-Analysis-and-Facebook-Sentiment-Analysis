from itertools import permutations

from max_flow_graph import MaxFlowGraph
from search_algorithms import find_a_path, after_max_flow
from graph import Graph


def facebook_enmy(V, E):
    """this function facebook_enmy(V, E) takes in input:
    ● a Python set V of voters, and
    ● a Python dictionary E whose keys are Python tuples representing pairs of
    voters that have a friendship relationship on Facebook, and whose values
    represent the enmity level that Facebook assigned to the corresponding pair,
    and returns two Python sets, D and R, corresponding to voters for Democrats and
    Republicans, respectively."""

    democratic = []  # set for democrats.
    republican = []  # set for republican.
    graph, vertex_weight_dict = construct_simple_graph(V, E)  # this function construct a graph.
    vertex_moved_dict = {}  # contains an association between the solution index and the element moved.
    solution_dict = {}  # contains an association between the solution index and its associated cut.
    single_execution_cut = 0  # this variable is used in the next cycle to keep emory the of the current execution
    # this cycle in every execution take a decision best locally and throw the space of solution reordered evert time the vertex in the best way
    for index in range(len(graph.vertices())):
        ordered_vertex_weight_dict = sorted(vertex_weight_dict.items(), key=lambda x: x[1], reverse=True)  # update every time vertex by them weight
        most_move_valuable_vertex = ordered_vertex_weight_dict[0]  # is the element with the highest weight on its edge
        single_execution_cut = single_execution_cut + most_move_valuable_vertex[1]  # update execution cut by the weight of the vertex extract
        vertex_moved_dict[index] = most_move_valuable_vertex[0]  # update "vertex_moved_dict" by the vertex extract
        vertex_weight_dict.pop(most_move_valuable_vertex[0])  # remove from the "vertex_weight_dict" the vertex extract for next iteration
        # this cycle update weight of node connected by an edge to the extract node if they are yet in the vertex_weight_dict
        for incident_edge in graph.incident_edges(most_move_valuable_vertex[0]):
            opposite_node = incident_edge.opposite(most_move_valuable_vertex[0])
            if opposite_node in vertex_weight_dict:
                vertex_weight_dict[opposite_node] = vertex_weight_dict[opposite_node] - 2 * incident_edge.element()
        solution_dict[index] = single_execution_cut  # update "solution_dict" by the cut obtained in this iteration
    best_configuration = 0  # this variable store at the end of the previous cycle the best cut obtained
    best_configuration_index = 0  # this variable store at the end of the previous cycle the index of the best configuration cut obtained
    # this cycle calculates the index in the previous cycle were is obtained the best cut of the best cut
    for single_solution in solution_dict:
        if solution_dict[single_solution] > best_configuration:
            best_configuration = solution_dict[single_solution]
            best_configuration_index = single_solution
    # this cycle composes republican and democratic sets throw the knowledge of "best_configuration_index"
    for index in range(len(vertex_moved_dict)):
        if index <= best_configuration_index:
            republican.append(vertex_moved_dict[index].element())
        else:
            democratic.append(vertex_moved_dict[index].element())
    return democratic, republican


def construct_simple_graph(vertex_list, edge_list):
    """this function costruct a simple graph starting from sets of vertices and of edges.
    It returns the graph build and a dictionary containing the vertex and its weight in terms of edges."""
    graph = Graph()  # it initializes a graph from the class Graph.
    vertices_dict = {}  # vertices dict were save vertices for graph.
    vertex_weight_dict = {}  # dict that conserve vertices and its weight in terms of edge.
    # this for each cycle complete a dict that associates to vertex item a real vertex of the graph "graph".
    for vertex in vertex_list:
        vertices_dict[vertex] = graph.insert_vertex(vertex)
    # this for each cycle insert edges takes from the "edge_list" in the graph "graph".
    for edge in edge_list:
        graph.insert_edge(vertices_dict[edge[0]], vertices_dict[edge[1]], edge_list[edge])
    # this for each cycle complete a dict "vertex_weight_dict" that associates to vertex item its weight.
    for vertex in vertices_dict:
        vertex_weight = 0
        for incident_edge in graph.incident_edges(vertices_dict[vertex]):
            vertex_weight += incident_edge.element()
        vertex_weight_dict[vertices_dict[vertex]] = vertex_weight
    return graph, vertex_weight_dict


def facebook_friend(V, E):
    """this function facebook_friend(V, E) that takes in input:
    ● a Python dictionary V whose keys represent voters, and values are Python
    tuples with the first entry being the likelihood for Democrats and the second
    being the likelihood for Republicans;
    ● a Python dictionary E whose keys represent pairs of voters that have a
    friendness relationship on Facebook, and whose values represent the
    friendship level that Facebook assigned to the corresponding pair,
    and returns two Python sets, D and R, corresponding to voters for Democrats and
    Republicans, respectively."""
    democratic = []  # set for democrats.
    republican = []  # set for republican.
    graph, all_vertex, super_source, super_target = costruct_graph_for_max_flow(V, E)  # this function construct a graph for max flow algorithm.
    discovered = {}  # this dict is used by find a path function to construct a path.
    path = []  # empty path by default.
    bottleneck = find_a_path(graph, path, super_source, super_target, discovered)  # this function construct a path from the target to the source if exist and return its bottleneck.
    # this cycle construct updates residual graph for every path that is found.
    while len(path) > 1:
        residual_graph(graph, path, bottleneck)  # construct residual graph throws the path found.
        bottleneck = find_a_path(graph, path, super_source, super_target, discovered)  # this function construct a path from the target to the source if exist and return its bottleneck.
    democrats_node = {}  # is a dict to insert democrats node (reachable from super source).
    after_max_flow(graph, super_source, democrats_node)  # this function is a simple BFS in the final residual graph.
    # this cycle complete democratic set scrolling "democrats_node" dict.
    for democrat in democrats_node:
        if democrat != super_source:
            democratic.append(democrat.element())
    # this cycle complete republican set scrolling "graph.vertices()" dict controlling if are not in "democratic" set.
    for elem in graph.vertices():
        if elem.element() not in democratic and elem != super_source and elem != super_target:
            republican.append(elem.element())
    return democratic, republican


def costruct_graph_for_max_flow(V, E):
    """this function create a graph for max flow from two dictionary, one for vertices and the second for edges, it
    inserts also a super source and a super target to use max flow algorithm, return the graph, vertex dict, super source
     and the super target."""
    g = MaxFlowGraph(True)
    all_vertex = {}  # dict were insert all graph vertex.
    super_source = g.insert_vertex("SuperSource")  # insert_super_source.
    super_target = g.insert_vertex("SuperTarget")  # insert_super_target.
    # this for each cycle complete a dict that associates to vertex item a real vertex of the graph "graph"
    # and insert an edge from the super source to the vertex if the likelihood for democrat in more than 0
    # and an edge from the vertx to the super_target if the likelihood for republican is more than 0.
    for vertex in V:
        all_vertex[vertex] = g.insert_vertex(vertex)
        if V[vertex][0] > 0:
            g.insert_edge(super_source, all_vertex[vertex], V[vertex][0])
        if V[vertex][1] > 0:
            g.insert_edge(all_vertex[vertex], super_target, V[vertex][1])
    # this for each cycle insert two edges in the opposite verse if its value is more than 0 in the graph "graph" between
    # vertices that represent them friendness.
    for edge in E:
        if E[edge] > 0:
            g.insert_edge(all_vertex[edge[0]], all_vertex[edge[1]], E[edge])
            g.insert_edge(all_vertex[edge[1]], all_vertex[edge[0]], E[edge])
    return g, all_vertex, super_source, super_target


def residual_graph(graph, path, bottleneck):
    """this function update as residual graph a graph passed as param, with a path and its bottleneck"""
    # this cycle decrement of bottleneck the value of every edge contained in the path, and increase of bottleneck the
    # opposite edges of path, furthermore remove edges that have values equal to zero to obtain a more compact structure.
    for edge in path:
        start_edge = edge.endpoints()[0]
        end_edge = edge.endpoints()[1]
        revert_edge = graph.get_edge(end_edge, start_edge)
        if edge.element() == bottleneck:
            if revert_edge is None:
                graph.insert_edge(end_edge, start_edge, bottleneck)
            else:
                graph.insert_edge(end_edge, start_edge, revert_edge.element() + bottleneck)
            graph.remove_edge(start_edge, end_edge)
        else:
            graph.insert_edge(start_edge, end_edge, edge.element() - bottleneck)
            if revert_edge is None:
                graph.insert_edge(end_edge, start_edge, bottleneck)
            else:
                graph.insert_edge(end_edge, start_edge, revert_edge.element() + bottleneck)
