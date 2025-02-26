from graphs import GraphNode, Graphs

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


