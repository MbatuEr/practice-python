import sys, random
from typing import List


class Array:
    @staticmethod
    def dutch_national_flag(pivot: int, nums: List[int]) -> List[int]:
        low, mid, high = 0,0, len(nums) - 1

        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == pivot:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                mid += 1
                high -= 1
        
        return nums
    
    @staticmethod
    def add_binary(s1: str, s2: str) -> str:
        i, j, carry = len(s1) - 1,len(s2) - 1, 0
        result = []

        while i>= 0 or j>= 0 or carry > 0:
            sum = carry

            if i >= 0:
                sum += int(s1[i])
                i -= 1
            if j >= 0:
                sum += int(s2[j])
                j -= 1
            
            result.append(str(sum % 2))
            carry = sum // 2
        
        return ''.join(reversed(result))

    @staticmethod
    def multiply(v1: List[int], v2: List[int]) -> List[int]:
        n, m = len(v1), len(v2)
        sign = -1 if v1[0] < 0 ^ v2[0] < 0 else 1
        multiplied = [0] * (n + m)
        v1[0], v2[0] = abs(v1[0]), abs(v2[0])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                sum = v1[i] * v2[j] + multiplied[i + j + 1]
                multiplied[i + j + 1] = sum % 10
                multiplied[i + j] += sum // 10
        
        while len(multiplied) > 1 and multiplied[0] == 0:
            multiplied.pop(0)
        
        multiplied[0] *= sign
        return multiplied

    @staticmethod
    def can_reach_end(nums: List[int]) -> bool:
        i, counter, furthest_reach = 0, 0, 0
        last_index = len(nums) - 1
    
        while i <= furthest_reach < last_index:
            temp = furthest_reach
            furthest_reach = max(furthest_reach, nums[i] + i)
            if temp != furthest_reach:
                counter += 1
            i += 1
        
        if furthest_reach >= last_index:
            print(f"The min step to reach the end is: {counter}")
        
        return furthest_reach >= last_index

    @staticmethod
    def remove_duplicates(nums: List[int]) -> List[int]:
        return list(dict.fromkeys(nums))

    @staticmethod
    def profit_from_stock(stocklist):
        lowest_price, highest_profit = sys.maxsize, 0

        for price in stocklist:
            lowest_price = min(lowest_price,price)
            highest_profit = max(highest_profit, price - lowest_price)

        return highest_profit
    
    @staticmethod
    def find_prime_values(key_value: int) -> List[int]:
        result = []

        for i in range(key_value - 1, 2, -1):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1, 1):
                if i % j == 0:
                    is_prime = False
                    break   
            if is_prime:
                result.append(i)
        
        result.append(2)
        return result
    
    @staticmethod
    def permuting_elements(nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(0, len(nums1)):
            nums1[i], nums1[nums2[i]] = nums1[nums2[i]], nums1[i]
            temp = nums2[i] 
            nums2[temp], nums2[i] = nums2[i], nums2[temp]

    @staticmethod
    def find_next_permutation(nums: List[int]) -> List[int]:
        s = len(nums) - 2

        while s >= 0 and nums[s] > nums[s + 1]:
            s -= 1 
        
        if s == -1:
            print("The original is the last permutation.")
        
        for i in range(len(nums) - 1, s, -1):
            if nums[s] > nums[i]:
                nums[s], nums[i] = nums[i], nums[s]
                break

        nums[s+1:] = reversed(nums[s + 1:]) 

    @staticmethod
    def offline_sandom_sampling(key: int, nums: List[int]) -> List[int]:
        random.shuffle(nums)
        nums[:] = nums[:key]
        
    def update_array_with_probabilities(self, size: int, input_array: List[int], probabilities: List[float]) ->List[int]:
        updated_array, counts = [], []
        counts = [round(prob*size) for prob in probabilities]
    
        for i, count in enumerate(counts):
            updated_array.extend([input_array[i]] * count)

        input_array[:] = updated_array 

    @staticmethod
    def is_valid_sudoku(board: List[List[int]]) -> bool:
        row = len(board)
        column = len(board[0])

        for i in range(0, row - 1):
            row_set = set()
            column_set = set()
            for j in range(0, column - 1, 1):    
                if board[i][j] in row_set or board[j][i] in column_set:
                    return False
                if board[i][j] != 0:
                    row_set.add(board[i][j])
                if board[j][i] != 0:
                    column_set.add(board[j][i])
    
        return True
    
    @staticmethod
    def spiral_order_of_array(matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        column = len(matrix[0])
        spiral_array = []

        left, right, top, bottom = 0, column - 1, 0, row - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                spiral_array.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                spiral_array.append(matrix[i][right])
            right -= 1

            for i in range(right, left - 1, -1):
                spiral_array.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                spiral_array.append(matrix[i][left])
            left += 1
        
        return spiral_array

    @staticmethod
    def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*matrix[::-1])]
    
    @staticmethod
    def generate_pascal_triangle(n: int, row: int, column: int) -> List[int]:
        if row == 0 or column == 0:
            return 1
        
        pascal_triangle = [[0 for _ in range(row)] for _ in range(column)]
        pascal_triangle[0][column - 1] = 1
        result = []

        for i in range(row - 1):
            for j in range(column - 1):
                pascal_triangle[i + 1][j] = pascal_triangle[i][j] + pascal_triangle[i][j + 1]
        
        for i in range(row):
            if pascal_triangle[n][i] != 0:
                result.append(pascal_triangle[n][i]) 
        
        return result
    
    @staticmethod
    def replace_spaces(s: str) -> str:
        return s.replace(' ', '%20')
    
    @staticmethod
    def string_compression(s: str) ->str:
        count = 1
        compressed = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                compressed.append(f"{s[i - 1]}{count}")
                count = 1
        
        compressed.append(f"{s[-1]}{count}")
        return ''.join(compressed)
    
    @staticmethod
    def is_rotation(s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in (s1 + s1)