from collections import defaultdict
from collections import deque
import heapq
import random

class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):     # To print team members in a readable format.
        return f"({self.name}, {self.age})" 
    
class Team:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __lt__(self, other):    # Define less-than operator for sorting.
        return self.height < other.height

    def __repr__(self):     # To print team members in a readable format.
        return f"({self.name}, {self.height})"

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
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            
            (left, right) = (mid + 1, right) if arr[mid] <= target <= arr[right] else (left, mid - 1)
            (right, left) = (mid - 1, left) if arr[left] <= target <= arr[mid] else (right, mid + 1)

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

    def sorting_students_by_age(self, students):
        """Sorts string and integer pairs by comparing integers."""
        students.sort(key=lambda student: student.age)

    def team_photo(self, team1, team2):
        """Sorts two unsorted vectors into two different arrays."""
        def print_lines(front_line, back_line):
            """Prints the sorted arrays."""
            print("Front Line:", front_line)
            print("Back Line:", back_line)
        
        team1.sort()
        team2.sort()

        front_line = []
        back_line = []

        team1_idx, team2_idx = 0, 0

        while team1_idx < len(team1) and team2_idx < len(team2) and len(front_line) < len(team1):
            if team1[team1_idx] < team2[team2_idx]:
                front_line.append(team1[team1_idx])
                team1_idx += 1
            else:
                front_line.append(team2[team2_idx])
                team2_idx += 1
        
        while team1_idx < len(team1) and team2_idx < len(team2) and len(back_line) < len(team1):
            if team1[team1_idx] < team2[team2_idx]:
                back_line.append(team1[team1_idx])
                team1_idx += 1
            else:
                back_line.append(team2[team2_idx])
                team2_idx += 1

        back_line.extend(team1[team1_idx:])
        back_line.extend(team2[team2_idx:])

        print_lines(front_line, back_line)

    def print_values(self):
        """Prints the values in the data."""
        print(" ".join(map(str, self.data)))

    def quick_sort(self, low = 0, high = None):
        """Function to perform Quick Sort."""
        if high is None:
            high = len(self.data) - 1
        
        if low >= high:
            return 
        
        pivot_index = random.randint(low, high)
        pivot = self.data[pivot_index]

        i,j = low, high
        while i <= j:
            while i <= high and self.data[i] < pivot:
                i += 1
            while j >= low and self.data[j] > pivot:
                j -= 1
            
            if i <= j:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i += 1
                j -= 1
        
        self.quick_sort(low, j)
        self.quick_sort(i, high)

    def bucket_sort(self, arr):
        """Function to perform Bucket Sort."""
        if len(arr) <= 1:
            return

        n = len(arr)
        buckets = defaultdict(list)

        for num in arr:
            bucket_index = int(n * num)
            buckets[bucket_index].append(num)

        sorted_arr = []
        for key in sorted(buckets):
            sorted_arr.extend(buckets[key])
        
        arr[:] = sorted_arr
    
    def radix_sort(self, arr):
        """Radix Sort implementation."""
        def counting_sort(arr, exp):
            """Counting sort for a specific digit represented by given value."""
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for num in arr:
                count[(num // exp) % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                digit = (arr[i] // exp) % 10
                output[count[digit] - 1] = arr[i]
                count[digit] -= 1
            
            arr[:] = output

        if not arr:
            return
        
        max_val = max(arr)
        exp = 1

        while max_val // exp > 0:
            counting_sort(arr, exp)
            exp *= 10