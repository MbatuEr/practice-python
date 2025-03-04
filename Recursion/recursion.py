from typing import List, Dict

class Recursion:
    def __init__(self):
        pass
    
    @staticmethod
    def find_all_permutations(nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums: List[int], n: int, res: List[List[int]]) -> None:
            if n == 1:
                res.append(nums[:])
                return
            
            for i in range(n):
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                backtrack(nums, n - 1, res)
                nums[i], nums[n - 1] = nums[n - 1], nums[i]

        backtrack(nums, len(nums), res)
        res.sort()
        return res
    
    @staticmethod
    def find_all_subsets(nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index: int, curr_subset: List[int], nums: List[int], 
                      res: List[List[int]]) -> None:
            if index == len(nums):
                res.append(curr_subset[:])
                return 
            
            curr_subset.append(nums[index])
            backtrack(index + 1, curr_subset, nums, res)
            curr_subset.pop()
            backtrack(index + 1, curr_subset, nums, res)

        backtrack(0, [], nums, res)
        return res
    
    @staticmethod
    def n_queens(n: int) -> int:
        res = 0
        def dfs(r: int, diagonal_set: set[int], anti_diagonal_set: set[int],
                cols_set: set[int]) -> None:
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                curr_diagonal = r - c
                curr_anti_diagonal = r + c
                if (c in cols_set or curr_diagonal in diagonal_set or 
                    curr_anti_diagonal in anti_diagonal_set):
                    continue

                cols_set.add(c)
                diagonal_set.add(curr_diagonal)
                anti_diagonal_set.add(curr_anti_diagonal)
                dfs(r + 1, diagonal_set, anti_diagonal_set, cols_set)
                cols_set.remove(c)
                diagonal_set.remove(curr_diagonal)
                anti_diagonal_set.remove(curr_anti_diagonal)


        dfs(0, set(), set(), set())
        return res
    
    @staticmethod
    def phone_keypad_combinations(digits: str) -> List[str]:
        res = []
        keypad_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        def backtrack(i: int, curr_combination: List[str], digits: str, 
                      keypad_map: Dict[str, str], res: List[str]) -> None:
            if len(curr_combination) == len(digits):
                res.append("".join(curr_combination))
                return
            
            for letter in keypad_map[digits[i]]:
                curr_combination.append(letter)
                backtrack(i + 1, curr_combination, digits, keypad_map, res)
                curr_combination.pop()

        backtrack(0, [], digits, keypad_map, res)
        return res
    
    def compute_tower_of_hanoi(self, n: int, source: str, destination: str, auxilary: str):
        if n == 1:
            print(f"Move disk 1 from {source} to {destination}")
            return
        
        self.compute_tower_of_hanoi(n - 1, source, auxilary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        self.compute_tower_of_hanoi(n - 1, auxilary, destination, source)

    @staticmethod
    def generate_all_subsets_of_size_k(n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i: int, curr_subset: List[int]) -> None:
            if len(curr_subset) == k:
                res.append(curr_subset[:])
                return
            if i > n:
                return
            
            backtrack(i + 1, curr_subset)
            curr_subset.append(i)
            backtrack(i + 1, curr_subset)
            curr_subset.pop()

        backtrack(1, [])
        return res

    @staticmethod
    def generate_parantheses(n: int) -> List[str]:
        res = []
        def backtrack(open: int, close: int, parantheses: str) -> None:
            if open == n and close == n:
                res.append(parantheses)
                return
            
            if open < n:
                backtrack(open + 1, close, parantheses + "(")
            if close < open:
                backtrack(open, close + 1, parantheses + ")")

        backtrack(0, 0, "")
        return res

    @staticmethod
    def palindrome_decompositions(input: str) -> List[List[str]]:
        def directed_palindrome_decompositions(offset: int, partial_partition: List[str]):
            if offset == len(input):
                result.append(partial_partition)
                return
            
            for i in range(offset + 1, len(input) + 1):
                prefix = input[offset:i]
                if prefix == prefix[::-1]:
                    directed_palindrome_decompositions(i, partial_partition + [prefix])

        result = []
        directed_palindrome_decompositions(0, [])
        return result
