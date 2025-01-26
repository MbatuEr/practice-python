import sys
import random

class Array:
    # Sorts a vector around a pivot.
    def dutch_national_flag(self, pivot, nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == pivot:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
    
    # Adds two binary numbers represented as strings
    def add_binary(self, s1, s2):
        result = []
        carry = 0
        i, j = len(s1) - 1, len(s2) - 1

        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            if i >= 0:
                total += int(s1[i])
                i -= 1
            if j >= 0:
                total += int(s2[j])
                j -= 1
            
            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))

    # Multiplies two large integers represented as vectors of their digits.
    def multiply(self, v1, v2):
        n = len(v1)
        m = len(v2)
        sign = -1 if (v1[0] < 0) ^ (v2[0] < 0) else 1
        v1[0], v2[0] = abs(v1[0]), abs(v2[0])

        result = [0] * (n + m)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = v1[i] * v2[j]
                sum = product + result[i + j + 1]  
                result[i + j + 1] = sum % 10       
                result[i + j] += sum // 10         

        while len(result) > 1 and result[0] == 0:
            result.pop(0)

        result[0] *= sign
        return result

    # Checks if it is possible to reach the last index of the array by jumping.
    def can_reach_end(self, vec):
        furthest_reach, counter, i = 0,0,0
        last_index = len(vec) - 1
        
        while i <= furthest_reach and furthest_reach < last_index:
            temp = furthest_reach
            furthest_reach = max(furthest_reach, vec[i] + i)
            if temp != furthest_reach:
                counter += 1
            i += 1
        
        if furthest_reach >= last_index:
            print("The minimum number of steps to reach the end : ", counter)
        
        return furthest_reach >= last_index

    # Removes duplicate elements from a vector.
    def remove_duplicates(self, vec):
        removed = []
        seen = set()
        for i in vec:
            if i not in seen:
                seen.add(i)
                removed.append(i)

        return removed
        # unique_elements = list(dict.fromkeys(vec))  # that'll do the same
        # return unique_elements 

    # Calculates the maximum profit that can be obtained by buying and selling a stock once.
    def profit_from_stock(self, stocklist):
        lowest_price = sys.maxsize
        max_profit = 0
        for price in stocklist:
            temp = price - lowest_price
            if price < lowest_price:
                lowest_price = price
            max_profit = max(max_profit, temp)
        
        return max_profit
    
    # Finds all prime numbers less than a given key value.
    def find_prime_values(self, key_value):
        primes = []
        for i in range(key_value - 1, 2, -1):  
            is_prime = True
            for j in range(2, int(i**0.5) + 1, 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        primes.append(2)  
        return primes
    
    # Rearranges one vector based on the permutation order.
    def permuting_elements(self, vec1, vec2):
        i = 0
        while i < len(vec1):
            vec1[i], vec1[vec2[i]] = vec1[vec2[i]], vec1[i]
            temp = vec2[i]
            vec2[i], vec2[temp] = vec2[temp], vec2[i]
            i += 1

    # Computes the next lexicographical permutation of the input vector.
    def find_next_permutation(self, vec):
        s = len(vec) - 2
        while s >= 0 and vec[s] >= vec[s + 1]:
            s -= 1

        if s == -1:
            print("Original is the last permutation.")
            return
        
        for i in range(len(vec) - 1, s, -1):
            if vec[i] > vec[s]:
                vec[i], vec[s] = vec[s], vec[i]
                break

        vec[s + 1:] = reversed(vec[s + 1:])

    # Randomly selects a subset of a specified size from the input vector.
    def offline_sandom_sampling(self, key, vec):
        random.shuffle(vec)
        vec[:] = vec[:key]
        
    # Updates an array's elements based on their associated probabilities.
    def update_array_with_probabilities(self, size, input_array, probabilities):
        updated_array, counts = [], []
        counts = [round(prob * size) for prob in probabilities]
        i = 0
        for i, count in enumerate(counts):
            updated_array.extend([input_array[i]] * count)
        
        input_array[:] = updated_array  
    
    # Checks if the sudoku board is valid.
    def is_valid_sudoku(self,board):
        row = len(board)
        column = len(board[0])
        for i in range(row):
            row_set = set()
            column_set = set()
            for j in range(column):
                if board[i][j] in row_set or board[j][i] in column_set:
                    return False
                if board[i][j] != 0:
                    row_set.add(board[i][j])
                if board[j][i] != 0:
                    column_set.add(board[j][i])
        
        return True

    # Returns the elements of a 2D array in spiral order as a 1D vector.
    def spiral_order_of_array(self, vec):
        row = len(vec)
        if row == 0:
            return []
        column = len(vec[0])
        arr = []
        top, bottom, left, right = 0, row - 1, 0, column - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                arr.append(vec[top][i])
            top += 1
            for i in range(top, bottom + 1):
                arr.append(vec[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    arr.append(vec[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    arr.append(vec[i][left])
                left += 1
        return arr
    
    # Rotates a 2D array 90 degrees clockwise.
    def rotating_2d_array(self, vec):
        row = len(vec)
        column = len(vec[0])
        rotated = [[0] * row for i in range(column)]

        for i in range(row):
            for j in range(column):
                rotated[j][row - i - 1] = vec[i][j]
        
        return rotated
    
    # Generates a specific row of Pascal's Triangle.
    def generate_pascal_triangle(self, n, row, column):
        if column == 0 or row == 0:
            return 1
        pascal_triangle = [[0 for _ in range(column)] for _ in range(row)]
        pascal_triangle[0][row - 1] = 1
        result = [0] * column
        
        for i in range(row - 1):
            for j in range(column - 1):
                pascal_triangle[i+1][j] = pascal_triangle[i][j] + pascal_triangle[i][j+1]
        
        for i in range(column):
            result[i] = pascal_triangle[n+1][i]
        k = 0
        while k < len(result):
            if result[k] == 0:
                    result.pop(k)
            k += 1
        
        return result
    
    # Replaces spaces in a string with '%20'.
    def replace_spaces(self, str, true_length):
        space_count = 0
        for i in range(true_length):
            if str[i] == ' ':
                space_count += 1
        
        index = true_length + space_count * 2
        str = list(str)
        str += [''] * space_count * 2
        for i in range(true_length - 1, -1, -1):
            if str[i] == ' ':
                str[index - 1] = '0'
                str[index - 2] = '2'
                str[index - 3] = '%'
                index -= 3
            else:
                str[index - 1] = str[i]
                index -= 1
        return str

    # Compresses a string using the counts of repeated characters.
    def string_compression(self, str):
        compressed = []
        count = 1
        for i in range(len(str)):
            if i + 1 < len(str) and str[i] == str[i+1]:
                count += 1
            else:
                compressed.append(str[i])
                compressed.append(count) 
                count = 1

        return compressed if len(compressed) < len(str) else str 
    
    # Checks if one string is a rotation of another string.
    def is_sub_string(self, str1, str2):
        if len(str1) != len(str2):
            return False
        return str2 in str1 + str1