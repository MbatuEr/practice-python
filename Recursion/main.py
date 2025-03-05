from recursion import Recursion

if __name__ == "__main__":
    rec = Recursion()

    # Find all permutations
    perm = [2, 3, 5]
    all_candidates = rec.find_all_permutations(perm)
    print("Permutations:", all_candidates)
    print("-" * 60)

    # Find all subsets
    input_values = [0, 1, 2]
    all_subsets = rec.find_all_subsets(input_values)
    print("All possible subsets are:", all_subsets)
    print("-" * 60)

    # N-queens problem
    s = 4
    number_of_design = rec.n_queens(s)
    print("The number of design:", number_of_design)
    print("-" * 60)

    # Phone keypad combinations
    digits = "69"
    combination_of_digits = rec.phone_keypad_combinations(digits)
    print(combination_of_digits)
    print("-" * 60)

    # Tower of Hanoi problem
    nums_of_rings = 3
    rec.compute_tower_of_hanoi(nums_of_rings, "A", "C", "B")
    print("-" * 60)

    # Generate subsets
    n, k = 5, 2
    subsets = rec.generate_all_subsets_of_size_k(n, k)
    print(subsets)
    print("-" * 60)

    # Generate parantheses
    num_of_parantheses = 3
    parantheses = rec.generate_parantheses(num_of_parantheses)
    print(parantheses)
    print("-" * 60)

    # Palindrome checker
    input_string = "0204451881"
    palindromes = rec.palindrome_decompositions(input_string)
    for i in range(len(palindromes)):
        print(palindromes[i])
    print("-" * 60)

    # Generating binary trees
    num_nodes = 3
    trees = rec.generate_all_binary_trees(num_nodes)
    print(f"Distinct binary trees with 3 nodes (total {len(trees)}):")
    for i, tree in enumerate(trees):
        print(f"\nTree {i+1}:")
        rec.print_tree_level_order(tree)
    print("-" * 60)

    # Solve sudoku
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if rec.solve_sudoku(sudoku_board):
        print("Solved Sudoku:")
        rec.print_sudoku(sudoku_board)
    else:
        print("No solution found.")
    print("-" * 60)

    # Gray code
    g_code = 3
    gray_code_calc = rec.gray_code(g_code)
    print(f"Gray code sequence for n = {g_code}:")
    print(" ".join(map(str, gray_code_calc)))
    print("-" * 60)

    # Tree diameter
    # Number of nodes (A, B, C, D, E, and two unnamed nodes)
    d = 7
    adj = [[] for _ in range(d)]  

    adj[0].append((1, 14))  # A -> B
    adj[1].append((0, 14))  # B -> A
    adj[1].append((2, 7))   # B -> C
    adj[2].append((1, 7))   # C -> B
    adj[2].append((3, 4))   # C -> D
    adj[3].append((2, 4))   # D -> C
    adj[3].append((4, 6))   # D -> E
    adj[4].append((3, 6))   # E -> D

    diameter = rec.tree_diameter(adj)
    print(f"The diameter of the tree is: {diameter}")
    print("-" * 60)