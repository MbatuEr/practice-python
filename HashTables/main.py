from hash_tables import HashTables

if __name__ == "__main__":

    obj = HashTables()
    # Unique characters
    input_string = "asdfghjkli"
    print("All characters are unique." if obj.has_all_unique_characters(input_string) else "Not all characters are unique.")
    print("-" * 60)

    # Permutations
    perm1, perm2 = "aaasdfghjkli", "iaalkjsdfhga"
    print("The strings are permutations of each other." if obj.are_permutations(perm1, perm2) else "The strings are not permutations of each other.")
    print("-" * 60)

    # Palindrome permutation
    print(f"Is palindrome permutation: {obj.is_palindrome_permutation('taco cat')}")
    print("-" * 60)

    # One edit away checker
    print(f"Is one away: {obj.is_one_away('pale', 'bale')}")
    print("-" * 60)

    # Most frequent character
    str3 = "hello world"
    char, freq = obj.most_frequent_word(str3)
    print(f"Most frequent character is '{char}' with frequency {freq}")
    print("-" * 60)

    # Nearest repetition
    words = ["apple", "banana", "apple", "orange", "banana", "grape"]
    print(f"Nearest repetition: {obj.nearest_repetition(words)}")
    print("-" * 60)

    # Shortest sequential subarray
    text = ["Given", "permutation", "string,", "write", "a", "palindrome", "to", "check", "if", "it", "is", "a", 
            "palindrome", "of", "a", "permutation", "A", "check", "is", "a", "word", "or", "phrase", "that", "is", 
            "the", "same", "forwards", "and", "backwards.", "A", "palindrome", "is", "just", "rearrangement", "of", 
            "permutation", "The", "palindrome", "does", "not", "need", "to", "be", "limited", "to", "permutation", "just", "does"]
    
    keywords = ["palindrome", "permutation"]
    start, end = obj.find_shortest_sequential_subarray(text, keywords)
    print(f"Shortest subarray: {' '.join(text[start:end + 1])}" if start != -1 else "No subarray contains all the keywords.")
    print("-" * 60)

    # Longest subarray with distinct entries
    arr = ["f", "s", "s", "e", "t", "w", "e", "n", "a", "e"]
    start, end = obj.longest_subarray_with_distinct_entries(arr)
    print(f"The longest subarray with distinct entries: {' '.join(arr[start:end + 1])}")
    print("-" * 60)

    # Longest contained interval
    input_array = [3, -2, 7, 9, 8, 1, 6, 0, -1, 5, 4]
    print(f"Length of the longest contained interval: {obj.longest_contained_interval(input_array)}")
    print("-" * 60)

    # Average of top three scores
    scores = [
        ("John", 60), ("Jane", 90), ("John", 35), ("Jane", 20),
        ("Jane", 50), ("Jack", 80), ("Jack", 95),
        ("Aby", 100), ("Aby", 95), ("Aby", 80)
    ]
    name, avg = obj.average_of_top_three_scores(scores)
    print(f"{name} {avg:.2f}" if name else "No individual has at least three scores.")
    print("-" * 60)

    # String decompositions
    sentence, words = "amanaplanacandl", ["nac", "ana", "pla"]
    starting_indices = obj.all_string_decompositions(sentence, words)

    if starting_indices:
        substring_length = sum(map(len, words))
        for index in starting_indices:
            print(f"All string decompositions: {sentence[index:index + substring_length]}")
    else:
        print("No valid decomposition found.")
    print("-" * 60)

    # Collatz conjecture
    n = 100
    print(f"Collatz conjecture holds for all numbers up to {n}: {obj.test_collatz(n)}")
    print("-" * 60)

    # Sudoku validation
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 2, 8, 0, 3, 0, 2, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    is_valid = obj.sudoku_board_validation(sudoku_board)
    if is_valid:
        print("Sudoku board is valid")
    else:
        print("Sudoku board is not valid")
    print("-" * 60)

    # Zero striping
    striping_matrix = [
        [1, 2, 3, 4, 5],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 0]
    ]

    obj.zero_striping(striping_matrix)
    for i in range(len(striping_matrix)):
        print(striping_matrix[i])
    print("-" * 60)