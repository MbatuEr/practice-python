from collections import defaultdict
from collections import Counter

class HashTables:
    def __init__(self):
        self.map = {}
        self.notes = {}
        self.wordIndex = Counter()

    # Checks if a string has all unique characters.
    def hasAllUniqueCharacters(self, str):
        self.map.clear()
        for char in str:
            if char in self.map:
                return False
            self.map[char] = True

        return True
    
    # Checks if two strings are permutations of each other.
    def arePermutation(self, str1, str2):
        self.map.clear()
        for char in str1:
            self.map[char] = self.map.get(char, 0) + 1
        
        for char in str2:
            if char not in self.map or self.map[char] == 0:
                return False
            self.map[char] -= 1

        return True
    
    # Checks if a string is a permutation of a palindrome.
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
        
    # Checks if two strings size differ by one.
    def isOneAwayChecker(self, str1, str2):
        if abs(len(str1) - len(str2)) >= 2:
            return False
        else:
            return self.isOneAway(str1, str2)
    
    # Checks if two strings are one edit away from each other.
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
    
    # Finds the most frequent word in a string.
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
    
    # Finds the nearest repetition of a word in a string.
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
    
    # Finds the length of the longest contained interval.
    def longestContainedInterval(self, arr):
        self.map.clear()
        max_length = 0
        for num in arr:
            if num not in self.map:
                left = self.map.get(num - 1, 0)
                right = self.map.get(num + 1, 0)
                length = left + right + 1

                self.map[num] = length
                self.map[num - left] = length
                self.map[num + right] = length

                max_length = max(max_length, length)
        
        return length
    
    # Finds the average of top three scores.
    def averageOfTopThreeScores(self, scores):
        top_scores = defaultdict(list)
        max_name = None
        max_average = 0

        for name, score in scores:
            top_scores[name].append(score)

        for name, score_list in top_scores.items():
            if len(score_list) >= 3:
                top_three = sorted(score_list, reverse=True)[:3]
                average = sum(top_three) / 3.0

                if average > max_average:
                    max_average = average
                    max_name = name

        return max_name, max_average
    
    # Finds all string decompositions.
    def allStringDecompositions(self, sentence, words):
        if not words or not sentence:
            return None  

        word_length = len(words[0])  
        word_count = len(words)
        total_length = word_length * word_count  


        self.wordIndex = Counter(words)

        for i in range(len(sentence) - total_length + 1):
            seen_words = Counter()
            j = 0

            while j < word_count:
                current_word = sentence[i + j * word_length : i + (j + 1) * word_length]

                if current_word not in self.wordIndex:
                    break

                seen_words[current_word] += 1
                if seen_words[current_word] > self.wordIndex[current_word]:
                    break

                j += 1

            if j == word_count:
                return i

        return None
    
    # Tests the conjecture for the first billion integers
    def testCollatz(self, n):
        for i in range(1, n+1):
            if not self.collatzSequence(i):
                return False
        
        return True
    
    # Recursive function to compute Collatz sequence.
    def collatzSequence(self, n):
        self.map.clear()
        
        if n == 1:
            return True
        
        if n in self.map:
            return self.map[n] 

        if n % 2 == 0:
            self.map[n] = self.collatzSequence(n // 2)
        else:
            self.map[n] = self.collatzSequence(3 * n + 1)
        
        return self.map[n]