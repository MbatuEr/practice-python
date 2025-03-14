from array_utils import Array

if __name__ == "__main__":
    # Dutch National Flag problem.
    obj = Array()
    nums = [3, 5, 2, 1, 7, 3]
    pivot = 3
    obj.dutch_national_flag(pivot, nums)

    for num in nums:
        print(num, end=' ')
    print()
    print("-" * 60)

    # Add Binary numbers.
    s1 = "101"
    s2 = "110"

    result_string = obj.add_binary(s1,s2)
    for i in result_string:
        print(i, end=' ')
    print()
    print("-" * 60)

    # Multiply two numbers
    num1 = [1, 2, 3]
    num2 = [9, 8, 7]
    multiplied = obj.multiply(num1, num2)
    print("Result:", multiplied)
    print("-" * 60)

    # Check if end is reachable.
    vec = [2,1,2,0,2,0,1,3,0,1,2,2,0,1]
    final = obj.can_reach_end(vec)
    print("The end is reachable? ")
    if final:
        print("Yes")
    else:
        print("No")
    print("-" * 60)

    # Remove duplicates
    duplicates = [3,2,1,5,2,3]
    removed = obj.remove_duplicates(duplicates)
    print("Removed: ", removed)    
    print("-" * 60)

    # Profit from stock.
    stocklist = [310,325,275,295,260,270,290,330,355,350]
    print("Highest profit for one buy and sell: ", obj.profit_from_stock(stocklist))
    print("-" * 60)

    # Find prime values.
    key_value = 122
    prime_values = obj.find_prime_values(key_value)
    print("Prime values smaller than the key value: ", prime_values)
    print("-" * 60)

    # Permute elements.
    original = [3,1,2,4,8,6,5,7]
    order_input = [2,0,1,3,7,5,4,6]
    obj.permuting_elements(original, order_input)
    print("Original array after permutation: ", original)
    print("-" * 60)

    # Next permutation.
    orig = [3,4,0,2,1]
    obj.find_next_permutation(orig)
    print("Next permutation of the original array: ", orig)
    print("-" * 60)

    # Offline random sampling
    samples = [3,4,10,21,13,38,56,89,22]
    obj.offline_sandom_sampling(6, samples)
    print("Sampled version: ", samples)
    print("-" * 60)

    # Update array with probabilities.
    arr = [3,5,7,11]
    probabilities = [9.0/18.0, 6.0/18.0, 2.0/18.0, 1.0/18.0]
    size = 18
    obj.update_array_with_probabilities(size, arr, probabilities)
    print("Values multiplied with probabilities: ", arr)
    print("-" * 60)

    # Validation of sudoku board.
    board = [
        [0, 3, 5, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    is_sudoku_valid = obj.is_valid_sudoku(board)
    print("Is the sudoku board valid?", is_sudoku_valid)
    print("-" * 60)

    # Spiral order of array.
    spiral_input = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    spiral_output = obj.spiral_order_of_array(spiral_input)
    print("Array as in spiral order: ", spiral_output)
    print("-" * 60)

    # Rotating 2D array.
    rotate_input = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    rotated_array = obj.rotate_matrix(rotate_input)
    print("Rotated array : ")
    for i in range(4):
        print()  # Print a new line
        for j in range(3):
            print(rotated_array[i][j], end=" ")
    print()
    print("-" * 60)

    # Generate pascal triangle.
    n, row, column = 5, 8, 8
    nth_row = obj.generate_pascal_triangle(n, row, column)
    print("The " f"{n}th row of the pascal triangle: ", nth_row)
    print("-" * 60)

    # Replace spaces.
    sentence = "Mr John Smith"
    replaced = obj.replace_spaces(sentence)
    print("Replaced sentence: ")
    for i in replaced:
        print(i,end="")
    print()
    print("-" * 60)

    # String compression.
    compressed = "aabcccccaaa"
    compressed_string = obj.string_compression(compressed)
    print("The compressed string: ", compressed_string)
    print("-" * 60)

    # Substring check.
    s1 = "waterbottle"
    s2 = "erbottlewat"
    is_substring = obj.is_rotation(s1, s2)
    print("Is s2 a rotation of s1? ", is_substring)
    print("-" * 60)
    
    # Triplet sum
    input_nums = [0, -1, 2, -3, 1]
    nums_samples = obj.triplet_sum(input_nums)
    print(nums_samples)
    print("-" * 60)

    # Largest container
    heights = [2, 7, 8, 3, 7, 6]
    container = obj.largest_container(heights)
    print("Largest containers area:", container)
    print("-" * 60)