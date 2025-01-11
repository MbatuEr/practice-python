from hash_tables import HashTables

if __name__ == "__main__":

    # Unique characters.
    obj = HashTables()
    input_string = "asdfghjkli"
    if obj.hasAllUniqueCharacters(input_string):
        print("All characters are unique.")
    else:
        print("Not all characters are unique.")
    print("------------------------------------------------------")

    # Permutation.
    perm1 = "aaasdfghjkli"
    perm2 = "iaalkjsdfhga"

    if obj.arePermutation(perm1, perm2):
        print("The strings are permutations of each other.")
    else:
        print("The strings are not permutations of each other.")
    print("------------------------------------------------------")

    # Palindrome permutation.
    palperm = "taco cat"
    print("Is palindrome permutation:", obj.isPalindromePermutation(palperm))
    print("------------------------------------------------------")    

    # One edit away checker.
    str1 = "pale"
    str2 = "bale"
    print("Is one away:", obj.isOneAwayChecker(str1, str2))
    print("------------------------------------------------------")    

    # Most frequent word.
    str3 = "hello world"
    freqword = obj.mostFrequentWord(str3)
    print("Most frequent word is ", freqword)
    print("------------------------------------------------------")    

    # Nearest repetition.
    vec = (["apple", "banana", "apple", "orange", "banana", "grape"])
    nearest_repetition = obj.nearestRepetition(vec)
    print("Nearest repetetion is: ", nearest_repetition)
    print("------------------------------------------------------")  

    # Shortest subarray.
    text = (["Given", "permutation", "string,", "write", "a", "palindrome", "to", "check", "if", "it", "is", "a", 
        "palindrome", "of", "a", "permutation", "A", "check", "is", "a", "word", "or", 
        "phrase", "that", "is", "the", "same", "forwards", "and", "backwards.", "A", "palindrome", 
        "is", "just", "rearrangement", "of", "permutation", "The", "palindrome", "does", "not", 
        "need", "to", "be", "limited", "to", "permutation", "just", "does"])
    
    
    keywords = ["palindrome", "permutation"]

    subarray = obj.findShortestSequentialSubarray(text, keywords)
    
    if subarray[0] != -1:
        print("Shortest subarray:", " ".join(text[subarray[0]:subarray[1] + 1]))
    else:
        print("No subarray contains all the keywords.")
    print("------------------------------------------------------")  

    # Longest Subarray.
    arr = (["f", "s", "s", "e", "t", "w", "e", "n", "a", "e"])
    longest_subarray = obj.longestSubarrayWithDistinctEntries(arr)
 
    print("The longest subarray with distinct entries: ", " ".join(arr[longest_subarray[0]: longest_subarray[1] + 1]))
    print("------------------------------------------------------")  

    # Longest Contained Interval.
    input_array = [3, -2, 7, 9, 8, 1, 6, 0, -1, 5, 4]
    length = obj.longestContainedInterval(input_array)
    print("Length of the longest interval: ", length)
    print("------------------------------------------------------")  

    # Average of top three scores.
    scores = [
        ("John", 60), ("Jane", 90), ("John", 35), ("Jane", 20),
        ("Jane", 50), ("Jack", 80), ("Jack", 95),
        ("Aby", 100), ("Aby", 95), ("Aby", 80)
    ]

    name, avg = obj.averageOfTopThreeScores(scores)

    if name:
        print(f"{name} {avg:.2f}")
    else:
        print("No individual has at least three scores.")
    print("------------------------------------------------------")

    # String decompositions.
    sentence = "amanaplanacandl"
    words = ["nac", "ana", "pla"]

    starting_index = obj.allStringDecompositions(sentence, words)
    
    if starting_index is not None:
        print(f"Input: {sentence}")
        print("All string decompositions: ", end="")
    
        for i in range(starting_index, starting_index + len(words) * len(words[0])):
            print(sentence[i], end="")
        print()
    else:
        print("No valid decomposition found.")
    print("------------------------------------------------------")

    # Collatz conjecture.
    n = 1000000
    result = obj.testCollatz(n)
    print("Collatz conjecture holds for all numbers up to 1000000:", result)
    print("------------------------------------------------------")
