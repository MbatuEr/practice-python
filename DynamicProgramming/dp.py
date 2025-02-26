from typing import List, Dict

class Dp:
    def __init__(self):
        self.memo = {}

    def climbing_stairs_top_down(self, n: int) -> int:
        if n <= 2:
            return n
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = (
            self.climbing_stairs_top_down(n - 1) +
            self.climbing_stairs_top_down(n - 2)
        )
        return self.memo[n]
    
    @staticmethod
    def climbing_stairs_bottom_up(n: int) -> int:
        if n <= 2:
            return n
        one_step_before, two_step_before = 2, 1
        for i in range(3, n + 1):
            current = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = current
        
        return current
    
    @staticmethod
    def min_coin_combination_top_down(coins: List[int], target: int) -> int:
        def top_down_up_dp(coins: List[int], target: int, memo: Dict[int, int]) -> int:
            if target == 0:
                return 0
            if target in memo:
                return memo[target]
            min_coins = float("inf")
            for coin in coins:
                if coin <= target:
                    min_coins = min(min_coins, 1 + top_down_up_dp(coins, target - coin, memo))

            memo[target] = min_coins
            return memo[target]
        res = top_down_up_dp(coins, target, {})
        return -1 if res == float("inf") else res
    
    @staticmethod
    def min_coin_combination_bottom_up(coins: List[int], target: int) -> int:
        dp = [float("inf")] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            for coin in coins:
                if coin <= t:
                    dp[t] = min(dp[t], 1 + dp[t - coin])
        
        return dp[target] if dp[target] != float("inf") else -1
    
    @staticmethod
    def matrix_pathways(m: int, n: int) -> int:
        prev_row = [1] * n
        for row in range(1, m):
            current_row = [1] * n
            for col in range(1, n):
                current_row[col] = current_row[col - 1] + prev_row[col]
            prev_row = current_row
        
        return prev_row[n - 1]
    
    @staticmethod
    def neighbor_burglary(houses: List[int]) -> int:
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        
        prev_max_frofit = max(houses[0], houses[1])
        prev_prev_max_frofit = houses[0]
        for i in range(2, len(houses)):
            current_profit = max(prev_max_frofit, houses[i] + prev_prev_max_frofit)
            prev_prev_max_frofit = prev_max_frofit
            prev_max_frofit = current_profit

        return current_profit
    
    @staticmethod
    def longest_common_subsequence(s1: str, s2: str) -> int:
        prev_row = [0] * (len(s2) + 1)
        for i in range(len(s1) - 1, -1, -1):
            current_row = [0] * (len(s2) + 1)
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    current_row[j] = 1 + prev_row[j + 1]
                else:
                    current_row[j] = max(prev_row[j], current_row[j + 1])
            prev_row = current_row
        
        return prev_row[0]
    
    def largest_palindrome_in_a_string(self, s: str) -> str:
        n = len(s)
        start, max_len = 0, 0
        for center in range(n):
            odd_start, odd_length = self.expand_palindrome(center, center, s)
            if odd_length > max_len:
                start, max_len = odd_start, odd_length
            if center < n - 1 and s[center] == s[center + 1]:
                even_start, even_length = self.expand_palindrome(center, center + 1, s)
                if even_length > max_len:
                    start, max_len = even_start, even_length

        return s[start: start + max_len]

    @staticmethod
    def expand_palindrome(left: int, right: int, s: str) -> tuple[int, int]:
        while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1

        return left, right - left + 1
    
    @staticmethod
    def maximum_subarray_sum(nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        current_sum = max_sum = nums[0]
        for i in range(1, n):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
            
        return max_sum

    @staticmethod
    def knapsack(cap: int, weights: List[int], values: List[int]) -> int:
        n = len(values)
        prev_row = [0] * (cap + 1)
        for i in range(n - 1, -1, -1):
            current_row = [0] * (cap + 1)
            for c in range(1, cap + 1):
                if weights[i] <= c:
                    current_row[c] = max(values[i] + prev_row[c - weights[i]], prev_row[c])
                else:
                    current_row[c] = prev_row[c]
            prev_row = current_row

        return prev_row[cap]

    @staticmethod
    def largest_square_in_a_matrix(matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        prev_row = [0] * n
        max_len = 0

        for i in range(m):
            current_row = [0] * n
            for j in range(n):
                if i == 0 or j == 0:
                    current_row[j] = matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        current_row[j] = 1 + min(current_row[j - 1], prev_row[j - 1], prev_row[j])
                max_len = max(max_len, current_row[j])
            prev_row, current_row = current_row, [0] * n

        return max_len ** 2