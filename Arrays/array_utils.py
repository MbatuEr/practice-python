import sys
import random

class Array:
    def dutch_national_flag(self, pivot, nums):
        """Sorts a vector around a pivot."""
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
    
    def add_binary(self, s1, s2):
        """Adds two binary numbers represented as strings"""
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

    def multiply(self, v1, v2):
        """Multiplies two large integers represented as vectors of their digits."""
        n, m = len(v1), len(v2)
        sign = -1 if v1[0] < 0 ^ v2[0] < 0 else 1
        multiplied = [0] * (n + m)
        v1[0], v2[0] = abs(v1[0]), abs(v2[0])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = v1[i] * v2[j]
                sum = product + multiplied[i + j + 1]
                multiplied[i + j + 1] = sum % 10
                multiplied[i + j] += sum // 10
        
        while len(multiplied) > 1 and multiplied[0] == 0:
            multiplied.pop(0)
        
        multiplied[0] *= sign
        return multiplied

    def can_reach_end(self, vec):
        """Checks if it is possible to reach the last index of the array by jumping."""
        i, counter, furthest_reach = 0, 0, 0
        last_index = len(vec) - 1
    
        while i <= furthest_reach and furthest_reach < last_index:
            temp = furthest_reach
            furthest_reach = max(furthest_reach, vec[i] + i)
            if temp != furthest_reach:
                counter += 1
            i += 1
        
        if furthest_reach >= last_index:
            print(f"The min step to reach the end is: {counter}")
        
        return furthest_reach >= last_index

    def remove_duplicates(self, vec):
        """Removes duplicate elements from a vector."""
        seen = set()
        removed = []
        for num in vec:
            if num not in seen:
                seen.add(num)
                removed.append(num)
        
        return removed
        # that'll do the same.
        # unique_elements = list(dict.fromkeys(vec))
        # return unique_elements

    def profit_from_stock(self, stocklist):
        """Calculates the maximum profit that can be obtained by buying and selling a stock once."""
        lowest_price = sys.maxsize
        highest_profit = 0

        for price in stocklist:
            lowest_price = min(lowest_price,price)
            highest_profit = max(highest_profit, price - lowest_price)

        return highest_profit
    
    def find_prime_values(self, key_value):
        """Finds all prime numbers less than a given key value."""
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
        
    def permuting_elements(self, vec1, vec2):
        """Rearranges one vector based on the permutation order."""
        for i in range(0, len(vec1)):
            vec1[i], vec1[vec2[i]] = vec1[vec2[i]], vec1[i]
            temp = vec2[i] 
            vec2[temp], vec2[i] = vec2[i], vec2[temp]

    def find_next_permutation(self, vec):
        """Computes the next lexicographical permutation of the input vector."""
        s = len(vec) - 2

        while s >= 0 and vec[s] > vec[s + 1]:
            s -= 1 
        
        if s == -1:
            print("The original is the last permutation.")
        
        for i in range(len(vec) - 1, s, -1):
            if vec[s] > vec[i]:
                vec[s], vec[i] = vec[i], vec[s]
                break

        vec[s+1:] = reversed(vec[s + 1:]) 

    def offline_sandom_sampling(self, key, vec):
        """Randomly selects a subset of a specified size from the input vector."""
        random.shuffle(vec)
        vec[:] = vec[:key]
        
    def update_array_with_probabilities(self, size, input_array, probabilities):
        """Updates an array's elements based on their associated probabilities."""
        updated_array, counts = [], []
        counts = [round(prob*size) for prob in probabilities]
    
        for i, count in enumerate(counts):
            updated_array.extend([input_array[i]] * count)

        input_array[:] = updated_array 

    def is_valid_sudoku(self,board):
        """Checks if the sudoku board is valid."""
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
    
    def spiral_order_of_array(self, vec):
        """Returns the elements of a 2D array in spiral order as a 1D vector."""
        row = len(vec)
        column = len(vec[0])
        spiral_array = []

        left, right, top, bottom = 0, column - 1, 0, row - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                spiral_array.append(vec[top][i])
            top += 1

            for i in range(top, bottom + 1):
                spiral_array.append(vec[i][right])
            right -= 1

            for i in range(right, left - 1, -1):
                spiral_array.append(vec[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                spiral_array.append(vec[i][left])
            left += 1
        
        return spiral_array

    def rotating_2d_array(self, vec):
        """Rotates a 2D array 90 degrees clockwise."""
        row = len(vec)
        column = len(vec[0])

        rotated_array = [[0] * row for i in range(column)]

        for i in range(row):
            for j in range(column):
                rotated_array[j][row - i - 1] = vec[i][j]
        
        return rotated_array

    def generate_pascal_triangle(self, n, row, column):
        """Generates a specific row of Pascal's Triangle."""
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
    
    def replace_spaces(self, str, true_length):
        """Replaces spaces in a string with '%20'."""
        space_count = 0 
        for i in range(true_length):
            if str[i] == ' ':
                space_count += 1
        
        index = true_length + space_count * 2
        str = list(str)

        str += [' '] * space_count * 2

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
    
    def string_compression(self, str):
        """Compresses a string using the counts of repeated characters."""
        count = 1
        compressed = []
        for i in range(len(str)):
            if i + 1 < len(str) and str[i] == str[i + 1]:
                count += 1
            else:
                compressed.append(str[i])
                compressed.append(count)
                count = 1
        
        return compressed
 
    def is_sub_string(self, str1, str2):
        """Checks if one string is a rotation of another string."""
        if len(str1) != len(str2):
            return False

        return str2 in str1 + str1
