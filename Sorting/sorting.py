from collections import defaultdict
from typing import List
import heapq, random

class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):     # To print students in a readable format
        return f"({self.name}, {self.age})" 
    
class Team:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __lt__(self, other):    # Less-than operator for sorting
        return self.height < other.height

    def __repr__(self):     # To print team members in a readable format
        return f"({self.name}, {self.height})"

class Sorting:
    def __init__(self, data = None):
        self.data = data if data is not None else []
        self.memo = {}
    
    @staticmethod
    def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            A[k] = A[i] if A[i] > B[j] else B[j]
            k, i, j = k - 1, i - (A[i] > B[j]), j - (A[i] <= B[j])

        A[:j + 1] = B[:j + 1] 
    
    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            freq = tuple(sorted(word))
            anagram_groups[freq].append(word)
        
        strs[:] = [anagram for group in anagram_groups.values() for anagram in group]

    @staticmethod
    def find_in_rotated_array(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            
            if arr[left] <= arr[mid]:
                (left, right) = (mid + 1, right) if arr[mid] < target <= arr[right] else (left, mid - 1)
            else:
                (right, left) = (mid - 1, left) if arr[left] <= target < arr[mid] else (right, mid + 1)

        return -1 
    
    def find_element(self, x: int) -> int:
        def element_at(index: int) -> int:
            return self.data[index] if 0 <= index < len(self.data) else float('inf')

        index = 1
        val = element_at(index)
        while val != float('inf') and val < x:
            index *= 2
            val = element_at(index)         # Store value to avoid redundant calls

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
    
    @staticmethod
    def split_into_chunks(data: List[str], chunk_size: int) -> List[List[str]]:
        return [sorted(data[i:i + chunk_size]) for i in range(0, len(data), chunk_size)]

    @staticmethod
    def merge_chunks(chunks: List[List[str]]) -> List[str]:
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

    @staticmethod
    def max_concurrent_events(events: Event) -> int:
        events.sort(key = lambda event: event.start)
        min_heap = []
        max_concurrent = 0

        for event in events:
            while min_heap and min_heap[0] <= event.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, event.end)
            max_concurrent = max(max_concurrent, len(min_heap))

        return max_concurrent
    
    @staticmethod
    def compute_union(intervals: List[Event]) -> List[Event]:
        if not intervals:
            return []
        
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

    @staticmethod
    def sorting_students_by_age(students: List[Student]) -> None:
        students.sort(key=lambda student: student.age)

    @staticmethod
    def team_photo(team1: List[Team], team2: List[Team]) -> None:
        def print_lines(front_line: List[Team], back_line: List[Team]) -> None:
            print("Front Line:", front_line)
            print("Back Line:", back_line)
        
        team1.sort()
        team2.sort()
        front_line, back_line = [], []
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

    def print_values(self) -> None:
        print(" ".join(map(str, self.data)))

    def quick_sort(self, low = 0, high = None) -> None:
        if high is None:
            high = len(self.data) - 1
        
        if low >= high:
            return 
        
        pivot_index = random.randint(low, high)
        pivot = self.data[pivot_index]

        i,j = low, high
        while True:
            while self.data[i] < pivot:
                i += 1
            while self.data[j] > pivot:
                j -= 1
            
            if i >= j:
                break       # Stop when pointers cross
            
            self.data[i], self.data[j] = self.data[j], self.data[i]  
            i += 1
            j -= 1
        
        self.quick_sort(low, j)
        self.quick_sort(j + 1, high)
    
    @staticmethod
    def bucket_sort(arr: List[float]) -> None:
        if len(arr) <= 1:
            return

        n = len(arr)
        buckets = defaultdict(list)

        for num in arr:
            bucket_index = int(n * num)
            buckets[bucket_index].append(num)

        sorted_arr = []
        for key in sorted(buckets):
            sorted_arr.extend(sorted(buckets[key]))
        
        arr[:] = sorted_arr
    
    @staticmethod
    def radix_sort(arr: List[int]) -> None:
        def counting_sort(arr: List[int], exp: int) -> None:
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

    def kth_largest_integer(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, k)
    
    def quick_select(self, nums: List[int], left: int, right: int, k: int) -> int:
        n = len(nums)
        if left >= right:
            return nums[left]
        
        random_index = random.randint(left, right)
        nums[random_index], nums[right] = nums[right], nums[random_index]
        pivot_index = self.partition(nums, left, right)

        if pivot_index < n - k:
            return self.quick_select(nums, pivot_index + 1, right, k)
        elif  pivot_index > n - k:
            return self.quick_select(nums, left, pivot_index - 1, k)
        else:
            return nums[pivot_index]
    
    @staticmethod
    def partition(nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        lo = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1
        
        nums[lo], nums[right] = nums[right], nums[lo]
        return lo
