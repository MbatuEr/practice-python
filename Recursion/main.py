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
