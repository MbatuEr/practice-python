from collections import defaultdict
import heapq
from collections import deque

class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Sorting:
    def __init__(self, data = None):
        self.data = data if data is not None else []
        
    def merge_sorted_arrays(self, A, m, B, n):
        """Merges two array in sorted order."""
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            A[k] = A[i] if A[i] > B[j] else B[j]
            k, i, j = k - 1, i - (A[i] > B[j]), j - (A[i] <= B[j])

        A[:j + 1] = B[:j + 1] 

    def vector_hash(self, vec):
        """Generates a hash for a vector of integers."""
        hash_val = 0
        for num in vec:
            hash_val ^= hash(num) + 0x9e3779b9 + (hash_val << 6) + (hash_val >> 2)
        return hash_val
    
    def group_anagrams(self, strs):
        """Groups anagrams together in-place and reverses the list."""
        anagram_groups = defaultdict(list)

        for word in strs:
            freq = tuple(sorted(word))
            anagram_groups[freq].append(word)
        
        strs[:] = [anagram for group in anagram_groups.values() for anagram in group]

    def find_in_rotated_array(self, arr, target):
        """Checks a given input whether it's in the array or not."""
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (right + left) // 2
            if arr[mid] == target: return mid
    
            if arr[left] < arr[mid]:
                if arr[left] <= target and target <= arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:             
                if arr[mid] <= target and target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
    
    def find_element(self, x):
        """Finds the index of x in an unbounded sorted list."""
        
        def element_at(index):
            """Returns element at index or inf if out of bounds."""
            return self.data[index] if 0 <= index < len(self.data) else float('inf')

        index = 1
        while element_at(index) != float('inf') and element_at(index) < x:
            index *= 2

        left, right = index // 2, index

        while left <= right:
            mid = (left + right) // 2
            element = element_at(mid)

            if element == x:
                return mid
            elif element == float('inf') or element > x:
                right = mid - 1
            else:
                left = mid + 1

        return -1
        
    def split_into_chunks(self, data, chunk_size):
        """Splits the data into chunks and sorts each chunk."""
        return [sorted(data[i:i + chunk_size]) for i in range(0, len(data), chunk_size)]

    def merge_chunks(self, chunks):
        """Merges the sorted chunks using a min-heap."""
        min_heap = []
        result = []

        for i, chunk in enumerate(chunks):
            if chunk:
                heapq.heappush(min_heap, (chunk[0], i, 0))
            
        while min_heap:
            smallest_string, chunk_index, element_index = heapq.heappop(min_heap)
            result.append(smallest_string)

            if element_index + 1 < len(chunks[chunk_index]):
                next_element = chunks[chunk_index][element_index + 1]
                heapq.heappush(min_heap, (next_element, chunk_index, element_index + 1))
        
        return result

    def max_concurrent_events(self, events):
        """Determines the max number of events that take place concurrently."""
        events.sort(key = lambda event: event.end)

        max_concurrent = 0
        active = deque()

        for event in events:
            while active and active[0].end <= event.start:
                active.popleft()

            active.append(event)
            max_concurrent = max(max_concurrent, len(active))
        
        return max_concurrent
    
    def compute_union(self, intervals):
        """Computes the union of intervals."""
        intervals.sort(key = lambda event: (event.start, event.end))

        result = []
        current = intervals[0]

        for next_event in intervals[1:]:
            if current.end >= next_event.start:
                current.end = max(current.end, next_event.end)
            else:
                result.append(current)
                current = next_event
        
        result.append(current)
        return result