class HashTables:
    def __init__(self):
        self.map = {}

    # Check if a string has all unique characters.
    def hasAllUniqueCharacters(self, str):
        self.map.clear()
        for char in str:
            if char in self.map:
                return False
            self.map[char] = True

        return True
    
    # Check if two strings are permutations of each other.
    def arePermutation(self, str1, str2):
        self.map.clear()
        for char in str1:
            self.map[char] = self.map.get(char, 0) + 1
        
        for char in str2:
            if char not in self.map or self.map[char] == 0:
                return False
            self.map[char] -= 1

        return True
    
    # Check if a string is a permutation of a palindrome.
    def isPalindromePermutation(self, str):
        self.map.clear()
        odd_count = 0

        for char in str:
            if char == ' ':
                continue

            self.map[char] = self.map.get(char, 0) + 1

            if self.map[char] % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1

        return odd_count <= 1
        
    # Check if two strings size differ by one.
    def isOneAwayChecker(self, str1, str2):
        if abs(len(str1) - len(str2)) >= 2:
            return False
        else:
            return self.isOneAway(str1, str2)
    
    # Check if two strings are one edit away from each other.
    def isOneAway(self, str1, str2):
        diff_count = 0
        self.map.clear()

        shorter = str1 if len(str1) <= len(str2) else str2
        longer =  str2 if len(str1) <= len(str2) else str1

        for char in shorter:
            self.map[char] = self.map.get(char, 0) + 1
        
        for char in longer:
            if char not in self.map or self.map[char] == 0:
                diff_count += 1
            else:
                self.map[char] -= 1

        return diff_count <= 1
    
    # Find the most frequent word in a string.
    def mostFrequentWord(self, str):
        self.map.clear()
        max_count = 0
        most_freq_char = ''
        for char in str:
            self.map[char] = self.map.get(char, 0) + 1
        
        for char, count in self.map.items():
            if count > max_count:
                max_count = count
                most_freq_char = char
        
        return {most_freq_char : max_count}
    
    # Find the nearest repetition of a word in a string.
    def nearestRepetition(self, str):
        min_dist = float('inf')
        nearest_word = ""
        self.map.clear()
    
        for i, word in enumerate(str):
            if word in self.map:
                distance = i - self.map[word]

                if distance < min_dist:
                    min_dist = distance
                    nearest_word = word
    
            self.map[word] = i
            
        
        return {nearest_word: min_dist if min_dist != float('inf') else -1}
    
    # Finds the shortest subarray that contains all the keywords in a paragraph.
    def findShortestSequentialSubarray(self, paragraph, keywords):
        matched_keywords = 0
        self.map.clear()
        result = (-1,-1)
        min_length = float('inf')
        start = 0

        for end, word in enumerate(paragraph):
            if word in keywords:
                self.map[word] = self.map.get(word, 0) + 1
                if self.map[word] == 1:
                    matched_keywords +=  1
            
            while matched_keywords == len(keywords):
                window_length = end - start + 1
                if window_length < min_length:
                    min_length = window_length
                    result = (start, end)

                start_word = paragraph[start]
                if start_word in keywords:
                    self.map[start_word] -= 1
                    if self.map[start_word] == 0:
                        matched_keywords -= 1
                    
                start += 1

        return result
    
    # Finds the longest subarray with distinct entries.
    def longestSubarrayWithDistinctEntries(self, arr):
        start = 0
        self.map.clear()
        result = (-1, -1)
        for end in range(len(arr)):
            if arr[end] not in self.map:
                self.map[arr[end]] = 1
            else:
                while arr[end] in self.map:
                    del self.map[arr[start]]
                    start += 1
                self.map[arr[end]] = 1

            if(end -start > result[1]- result[0]):
                result = (start, end)
        
        return result
            