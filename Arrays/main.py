from array_utils import Array

if __name__ == "__main__":
    # Dutch National Flag problem.
    obj = Array()
    nums = [3, 5, 2, 1, 7, 3]
    pivot = 3
    obj.DutchNationalFlag(pivot, nums)

    for num in nums:
        print(num, end=' ')
    print("\n----------------------------------------------")

    # Add Binary numbers.
    s1 = "101"
    s2 = "110"

    result_string = obj.AddBinary(s1,s2)
    for i in result_string:
        print(i, end=' ')
    print("\n----------------------------------------------")

    # Multiply two numbers
    num1 = [1, 2, 3]
    num2 = [9, 8, 7]
    multiplied = obj.Multiply(num1, num2)
    print("Result:", multiplied)
    print("----------------------------------------------")

    # Check if end is reachable.
    vec = [2,1,2,0,2,0,1,3,0,1,2,2,0,1]
    final = obj.CanReachEnd(vec)
    print("The end is reachable? ")
    if final:
        print("Yes")
    else:
        print("No")
    print("----------------------------------------------")

    # Remove duplicates
    duplicates = [3,2,1,5,2,3]
    removed = obj.RemoveDuplicates(duplicates)
    print("Removed: ", removed)    
    print("\n----------------------------------------------")

    # Profit from stock.
    stocklist = [310,325,275,295,260,270,290,330,355,350]
    print("Highest profit for one buy and sell: ", obj.ProfitFromStock(stocklist))
    print("----------------------------------------------")

    # Find prime values.
    key_value = 122
    prime_values = obj.FindPrimeValues(key_value)
    print("Prime values smaller than the key value: ", prime_values)
    print("----------------------------------------------")

    # Permute elements.
    original = [3,1,2,4,8,6,5,7]
    order_input = [2,0,1,3,7,5,4,6]
    obj.PermutingElements(original, order_input)
    print("Original array after permutation: ", original)
    print("----------------------------------------------")

    # Next permutation.
    orig = [3,4,0,2,1]
    obj.FindNextPermutation(orig)
    print("Next permutation of the original array: ", orig)
    print("----------------------------------------------")

    # Offline random sampling
    samples = [3,4,10,21,13,38,56,89,22]
    obj.OfflineRandomSampling(6, samples)
    print("Sampled version: ", samples)
    print("----------------------------------------------")

    # Update array with probabilities.
    arr = [3,5,7,11]
    probabilities = [9.0/18.0, 6.0/18.0, 2.0/18.0, 1.0/18.0]
    size = 18
    obj.UpdateArrayWithProbabilities(size, arr, probabilities)
    print("Values multiplied with probabilities: ", arr)
    print("----------------------------------------------")

    # Check if the sudoku board is valid.
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

    is_sudoku_valid = obj.isValidSudoku(board)
    print("Is the sudoku board valid?", is_sudoku_valid)
    print("----------------------------------------------")

    # Spiral order of array.
    spiral_input = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    spiral_output = obj.SpiralOrderOfArray(spiral_input)
    print("Array as in spiral order: ", spiral_output)
    print("----------------------------------------------")

    # Rotating 2D array.
    rotate_input = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    rotated_array = obj.Rotating2DArray(rotate_input)
    print("Rotated array : ")
    for i in range(4):
        print()  # Print a new line
        for j in range(3):
            print(rotated_array[i][j], end=" ")

    print("\n----------------------------------------------")

    # Generate pascal triangle.
    n, row, column = 5, 7, 8
    nth_row = obj.GeneratePascalTriangle(n, row, column)
    print("The " f"{n}th row of the pascal triangle: ", nth_row)
    print("----------------------------------------------")

    # Replace spaces.
    sentence = "Mr John Smith"
    true_length = 13
    replaced = obj.ReplaceSpaces(sentence, true_length)
    print("Replaced sentence: ")
    for i in replaced:
        print(i,end="")
    print("\n----------------------------------------------")

    # String compression.
    compressed = "aabcccccaaa"
    compressed_string = obj.StringCompression(compressed)
    print("The compressed string: ", compressed_string)
    print("----------------------------------------------")

    # Substring check.
    s1 = "waterbottle"
    s2 = "erbottlewat"
    is_substring = obj.isSubString(s1, s2)
    print("Is s2 a substring of s1? ", is_substring)
    print("----------------------------------------------")
    