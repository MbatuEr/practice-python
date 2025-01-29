import heapq
from typing import List

class Element:
    def __init__(self, value, array_index, element_index):
        self.value = value
        self.array_index = array_index
        self.element_index = element_index

    def __lt__(self, other):
        return self.value < other.value
    
class Heapq:
    def __init__(self):
        self.min_heap = []
    
    def merge_sorted_arrays(self, sorted_arrays: List[List[int]]) -> List[int]:
        for i, array in enumerate(sorted_arrays):
            if array:
                heapq.heappush(self.min_heap, Element(sorted_arrays[i][0], i, 0))


        result =[]

        while self.min_heap:
            current = heapq.heappop(self.min_heap)
            result.append(current.value)

            next_element_index = current.element_index + 1
            if next_element_index < len(sorted_arrays[current.array_index]):
                next_value = sorted_arrays[current.array_index][next_element_index]
                heapq.heappush(self.min_heap, Element(next_value, current.array_index, next_element_index))

        return result
     
    def sort_increasing_decreasing_array(self, arr: List[int]) -> List[int]:
        sorted_arrays = self.split_into_sorted_subarrays(arr)
        return self.merge_sorted_arrays(sorted_arrays)
    
    def split_into_sorted_subarrays(self, arr: List[int]) -> List[List[int]]:
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
                increasing = not increasing
        
        return sorted_arrays
    