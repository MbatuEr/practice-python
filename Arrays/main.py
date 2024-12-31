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

    # Update array with probabilities
    arr = [3,5,7,11]
    probabilities = [9.0/18.0, 6.0/18.0, 2.0/18.0, 1.0/18.0]
    size = 18
    obj.UpdateArrayWithProbabilities(size, arr, probabilities)
    print("Values multiplied with probabilities: ", arr)
    print("----------------------------------------------")