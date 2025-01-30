import heapq
from typing import List
import math

class Element:
    def __init__(self, value, array_index, element_index):
        self.value = value
        self.array_index = array_index
        self.element_index = element_index

    def __lt__(self, other):
        return self.value < other.value

class Star:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def distance_to_earth(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def __repr__(self):
        return f"Star({self.x}, {self.y}, {self.z})"

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
                    increasing = not increasing

            return sorted_arrays
        sorted_arrays = split_into_sorted_subarrays(arr)
        return self.merge_sorted_arrays(sorted_arrays)
    
    def sort_k_sorted_array(self, arr, k):
        result = []

        for num in arr[:k+1]:
            heapq.heappush(self.min_heap, num)
        
        for num in arr[k+1:]:
            result.append(heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, num)
        
        while self.min_heap:
            result.append(heapq.heappop(self.min_heap))

        return result
    
    def find_k_closest_stars(self, stars: List[Star], k: int) -> List[Star]:
        if k <= 0 : return []

        return heapq.nsmallest(k, stars, key=lambda star: star.distance_to_earth())

