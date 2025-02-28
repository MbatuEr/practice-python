from graphs import GraphNode, Graphs, MergingCommunities

if __name__ == "__main__":
    graph = Graphs()
    
    # Graph deep copy
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node1.neighbors.append(node2)
    node2.neighbors.append(node1)

    cloned_graph = graph.graph_deep_copy(node1)
    print("Cloned node:", cloned_graph.val)  
    print("Cloned node's neighbor:", cloned_graph.neighbors[0].val)  
    print("Are nodes neighbor to each other?", cloned_graph.neighbors[0].neighbors[0] is cloned_graph) 
    print("-" * 60)
    
    # Count islands
    input_matrix = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1]
    ]
    number_of_islands = graph.count_island(input_matrix)
    print("The number of islands:", number_of_islands)
    print("-" * 60)

    # Matrix infection
    infected_matrix = [         # 2: infected, 1: non-infected 0: immune
        [1, 2, 1, 0, 1], 
        [1, 0, 0, 1, 1], 
        [1, 2, 0, 0, 2]
    ]
    level_of_infection = graph.matrix_infection(infected_matrix)
    print("The level of infection is:", level_of_infection)
    print("-" * 60)

    # Bipartite graph
    bipartite_graph = [[1, 4], [0, 2], [1], [4] , [0, 3]]
    validation = graph.bipartite_graph_validation(bipartite_graph)
    if validation:
        print("The graph is bipartite.")
    else:
        print("The graph is not bipartite.")
    print("-" * 60)

    # Longest increasing path
    increasing_path = [
        [1, 5, 8],
        [3, 4, 4],
        [7, 9, 2]
    ]

    longest_path = graph.longest_increasing_path(increasing_path)
    print("Length of the longest path:", longest_path)
    print("-" * 60)

    # Shortest Transformation
    start = "hit"
    end = "cog"
    dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]
    shortest_path_length = graph.shortest_transformation_sequence(start, end, dictionary)
    print("Shortest transformation sequence is:", shortest_path_length)
    print("-" * 60)

    # Merging communities
    n = 5
    com = MergingCommunities(n)
    if com.connect(0, 1):
        print("Node 0 and node 1 are connected.")
    if com.connect(1, 2):
        print("Node 1 and node 2 are connected.")
    print("Community size of the node 3:", com.get_community_size(3))
    print("Community size of the node 0:", com.get_community_size(0))
    if com.connect(3, 4):
        print("Node 3 and node 4 are connected.")
    print("Community size of the node 4:", com.get_community_size(4))
    print("-" * 60)

    # Connecting dots (Kruskal's Algorithm)
    dots = [[1, 1], [2, 6], [3, 2], [4, 3], [7, 1]]
    mst = graph.connect_the_dots(dots)
    print("The weight of the MST:", mst)
    print("-" * 60)

    # Prerequisites (Kahn's Algorithm)
    pre = 6
    prereq = [[0, 1], [0, 2], [3, 2], [1, 4], [2, 4], [4, 5]]
    if graph.prerequisites(pre, prereq):
        print("The graph does not contain a cycle.")
    else:
        print("The graph contains a cycle.")
    print("-" * 60)

    # Shortest path (Dijkstra's Algorithm)
    start, number_of_nodes = 0, 6
    edges_dijkstra = [
        [0, 1, 5], [0, 2, 3], [1, 2, 1], 
        [1, 3, 4], [2, 3, 4], [2, 4, 5]
    ]
    
    shortest_dijkstra = graph.dijkstra_s_algorithm(number_of_nodes, edges_dijkstra, start)
    print("The shortest path:", shortest_dijkstra)
    print("-" * 60)

    # Shortest path (Bellman-Ford Algorithm)
    edges_bellman = [
        [0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2],
        [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]
    ]
    num_vertices = 5
    source = 0

    shortest_bellman = graph.bellman_ford(num_vertices, edges_bellman, source)
    print("Shortest distances from source:", shortest_bellman)
    print("-" * 60)

    # Floyd-Warshall Algorithm
    INF = float("inf")
    graph_fw = [
        [0, 3, INF, 5],
        [2, 0, INF, 4],
        [INF, 1, 0, INF],
        [INF, INF, 2, 0]
    ]

    shortest_fw = graph.floyd_warshall(graph_fw)
    print("Shortest distance between all vertices:")
    for row in shortest_fw:
        print(row)
    print("-" * 60)