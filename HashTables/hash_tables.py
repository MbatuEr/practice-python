from collections import defaultdict, Counter
from itertools import zip_longest

class HashTables:
    @staticmethod
    def has_all_unique_characters(s: str) -> bool:
        return len(set(s)) == len(s)

    @staticmethod
    def are_permutations(s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)

    @staticmethod
    def is_palindrome_permutation(s: str) -> bool:
        s = s.replace(" ", "")
        char_counts = Counter(s)
        return sum(count % 2 for count in char_counts.values()) <= 1

    @staticmethod
    def is_one_away(s1: str, s2: str) -> bool:
        if abs(len(s1) - len(s2)) > 1:
            return False
        
        diffs = sum(c1 != c2 for c1, c2 in zip_longest(s1, s2, fillvalue=""))
        return diffs <= 1
    
    @staticmethod
    def most_frequent_word(s: str) -> dict:
        char_counts = Counter(s)
        return max(char_counts.items(), key=lambda x: x[1])
    
    @staticmethod
    def nearest_repetition(words: list) -> dict:
        word_positions = {}
        min_distance = float('inf')
        nearest_word = ""

        for i, word in enumerate(words):
            if word in word_positions:
                distance = i - word_positions[word]
                if distance < min_distance:
                    min_distance, nearest_word = distance, word
            word_positions[word] = i
        
        return {nearest_word: min_distance if min_distance != float('inf') else -1}
    
    @staticmethod
    def find_shortest_sequential_subarray(paragraph: list, keywords: set) -> tuple:
        keyword_count = defaultdict(int)
        matched_keywords = 0
        start = 0
        min_length = float('inf')
        result = (-1, -1)

        for end, word in enumerate(paragraph):
            if word in keywords:
                keyword_count[word] += 1
                if keyword_count[word] == 1:
                    matched_keywords += 1
            
            while matched_keywords == len(keywords):
                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    result = (start, end)
                
                if paragraph[start] in keywords:
                    keyword_count[paragraph[start]] -= 1
                    if keyword_count[paragraph[start]] == 0:
                        matched_keywords -= 1
                start += 1
        
        return result
    
    @staticmethod
    def longest_subarray_with_distinct_entries(arr: list) -> tuple:
        seen = {}
        start = 0
        best_range = (0, 0)

        for end, num in enumerate(arr):
            if num in seen and seen[num] >= start:
                start = seen[num] + 1
            seen[num] = end
            if end - start > best_range[1] - best_range[0]:
                best_range = (start, end)
        
        return best_range
    
    @staticmethod
    def longest_contained_interval(arr: list) -> int:
        elements = set(arr)
        max_length = 0

        for num in arr:
            if num - 1 not in elements:
                current_length = 1
                while num + 1 in elements:
                    num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        
        return max_length
    
    @staticmethod
    def average_of_top_three_scores(scores: list) -> tuple:
        top_scores = defaultdict(list)
        max_avg = 0
        max_name = None

        for name, score in scores:
            top_scores[name].append(score)

        for name, score_list in top_scores.items():
            if len(score_list) >= 3:
                avg = sum(sorted(score_list, reverse=True)[:3]) / 3.0
                if avg > max_avg:
                    max_avg, max_name = avg, name
        
        return max_name, max_avg
    
    @staticmethod
    def all_string_decompositions(sentence: str, words: list) -> list:
        if not words or not sentence:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []
        
        for i in range(len(sentence) - total_len + 1):
            seen = Counter()
            j = 0
            while j < len(words):
                word = sentence[i + j * word_len: i + (j + 1) * word_len]
                if word not in word_count or seen[word] >= word_count[word]:
                    break
                seen[word] += 1
                j += 1
            if j == len(words):
                result.append(i)
        
        return result
    
    def test_collatz(self, n: int) -> bool:
        return all(self.collatz_sequence(i) for i in range(1, n + 1))

    @staticmethod
    def collatz_sequence(n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = n // 2 if n % 2 == 0 else 3 * n + 1
        return True