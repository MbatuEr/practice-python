class HashTables:
    def __init__(self):
        self.uniqchar = {}
        self.charcount = {}

    # check if a string has all unique characters
    def hasAllUniqueCharacters(self, str):
        self.uniqchar.clear()
        for char in str:
            if char in self.uniqchar:
                return False
            self.uniqchar[char] = True

        return True
    
    # check if two strings are permutations of each other
    def arePermutation(self, str1, str2):
        self.charcount.clear()
        for char in str1:
            self.charcount[char] = self.charcount.get(char, 0) + 1
        
        for char in str2:
            if char not in self.charcount or self.charcount[char] == 0:
                return False
            self.charcount[char] -= 1

        return True
    
    # check if a string is a permutation of a palindrome
    def isPalindromePermutation(self, str):
        self.charcount.clear()
        odd_count = 0

        for char in str:
            if char == ' ':
                continue

            self.charcount[char] = self.charcount.get(char, 0) + 1

            if self.charcount[char] % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1

        return odd_count <= 1
        
    # check if two strings size differ by one
    def isOneAwayChecker(self, str1, str2):
        if abs(len(str1) - len(str2)) >= 2:
            return False
        else:
            return self.isOneAway(str1, str2)
    
    # check if two strings are one edit away from each other
    def isOneAway(self, str1, str2):
        diff_count = 0
        self.charcount.clear()

        shorter = str1 if len(str1) <= len(str2) else str2
        longer =  str2 if len(str1) <= len(str2) else str1

        for char in shorter:
            self.charcount[char] = self.charcount.get(char, 0) + 1
        
        for char in longer:
            if char not in self.charcount or self.charcount[char] == 0:
                diff_count += 1
            else:
                self.charcount[char] -= 1

        return diff_count <= 1
    
    # find the most frequent word in a string
    def mostFrequentWord(self, str):
        self.charcount.clear()
        max_count = 0
        most_freq_char = ''
        for char in str:
            self.charcount[char] = self.charcount.get(char, 0) + 1
        
        for char, count in self.charcount.items():
            if count > max_count:
                max_count = count
                most_freq_char = char
        
        return {most_freq_char : max_count}
    