from typing import List 
from collections import Counter
import heapq
import math

class Element:
    def __init__(self, value, array_index, element_index):
        self.value = value
        self.array_index = array_index
        self.element_index = element_index
    
    def __lt__(self, other):
        return self.value < other.value

class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distance_to_earth(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __repr__(self):
        return f"Star({self.x}, {self.y}, {self.z})"

class Pair:
    def __init__(self, str, freq):
        self.str = str
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str > other.str
        return self.freq < other.freq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"

class Heapq:
    def __init__(self):
        self.min_heap = []
    
    def merge_sorted_arrays(self, sorted_arrays: List[List[int]]) -> List[int]:
        for i, arr in enumerate(sorted_arrays):
            if arr:
                heapq.heappush(self.min_heap, Element(sorted_arrays[i][0], i, 0))
        
        result = []
        while self.min_heap:
            current = heapq.heappop(self.min_heap)
            result.append(current.value)

            next_element_index = current.element_index + 1
            if next_element_index < len(sorted_arrays[current.array_index]):
                next_value = sorted_arrays[current.array_index][next_element_index]
                heapq.heappush(self.min_heap, Element(next_value, current.array_index, next_element_index))
            
        return result

    def sort_increasing_decreasing_array(self, arr: List[int]) -> List[int]:
        def split_into_sorted_subarrays(arr: List[int]) -> List[List[int]]:
            sorted_arrays = []
            increasing = True
            start = 0

            for i in range(1, len(arr) + 1):
                if i == len(arr) or (arr[i] > arr[i - 1]) != increasing:
                    segment = arr[start:i]
                    if not increasing:
                        segment.reverse()

                    sorted_arrays.append(segment)
                    start = i
                    increasing != increasing
            
            return sorted_arrays
        sorted_arrays = split_into_sorted_subarrays(arr)
        return self.merge_sorted_arrays(sorted_arrays)
    
    def sort_almost_sorted_array(self, arr: List[int], k: int) -> List[int]:
        result = []

        for num in arr[:k + 1]:
            heapq.heappush(self.min_heap, num)
        
        for num in arr[k + 1:]:
            result.append(heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, num)
        
        while self.min_heap:
            result.append(heapq.heappop(self.min_heap))
        
        return result
    
    @staticmethod
    def find_k_closest_stars(stars: List[List[Star]], k: int) -> List[Star]:
        if k <= 0 : 
            return []
        return heapq.nsmallest(k, stars, key=lambda star: star.distance_to_earth())
    
    @staticmethod
    def online_median(sequence: List[int]) -> List[float]:
        max_heap = []  # Store negative values for max behavior
        min_heap = []  
        result = []

        for x in sequence:
            heapq.heappush(min_heap, -heapq.heappushpop(max_heap, x))
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            median = (-max_heap[0] + min_heap[0]) / 2 if len(max_heap) == len(min_heap) else -max_heap[0]
            result.append(-median)

        return result
    
    @staticmethod
    def find_k_largest_elements(arr: List[int], k: int) -> List[int]:
        if k  <= 0: return []
        return heapq.nlargest(k, arr)

    def most_frequent_strings(self, strs: List[str], k: int) -> List[str]:
        freqs = Counter(strs)

        for str, freq in freqs.items():
            heapq.heappush(self.min_heap, Pair(str, freq))
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)
        
        res = [heapq.heappop(self.min_heap).str for _ in range(k)]
        return res
    
    @staticmethod
    def combine_sorted_linked_lists(lists: list[ListNode]) -> ListNode:
        ListNode.__lt__ = lambda self, other : self.val < other.val
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        dummy = ListNode(-1)
        curr = dummy
        while heap:
            smallest_node = heapq.heappop(heap)
            curr.next = smallest_node
            curr = curr.next
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)
        
        return dummy.next
    
    @staticmethod
    def create_linked_list(lst):
        if not lst:
            return None
        
        head = ListNode(lst[0])
        curr = head
        for val in lst[1:]:
            curr.next = ListNode(val)
            curr = curr.next
            
        return head