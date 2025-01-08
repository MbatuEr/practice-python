from hash_tables import HashTables

if __name__ == "__main__":

    # check for unique characters
    obj = HashTables()
    input_string = "asdfghjkli"
    if obj.hasAllUniqueCharacters(input_string):
        print("All characters are unique.")
    else:
        print("Not all characters are unique.")
    print("------------------------------------------------------")

    # check for permutations
    perm1 = "aaasdfghjkli"
    perm2 = "iaalkjsdfhga"

    if obj.arePermutation(perm1, perm2):
        print("The strings are permutations of each other.")
    else:
        print("The strings are not permutations of each other.")
    print("------------------------------------------------------")

    # check for palindrome permutation
    palperm = "taco cat"
    print("Is palindrome permutation:", obj.isPalindromePermutation(palperm))
    print("------------------------------------------------------")    

    # check for one away
    str1 = "pale"
    str2 = "bale"
    print("Is one away:", obj.isOneAwayChecker(str1, str2))
    print("------------------------------------------------------")    

    # check for most frequent word
    str3 = "hello world"
    freqword = obj.mostFrequentWord(str3)
    print("Most frequent word is ", freqword)
    print("------------------------------------------------------")    
