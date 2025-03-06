from typing import List
import math, itertools

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

        def backtrack(index: int, curr_subset: List[int]):
            if index == len(nums):
                res.append(curr_subset[:])
                return
            
            curr_subset.append(nums[index])
            backtrack(index + 1, curr_subset)
            curr_subset.pop()
            backtrack(index + 1, curr_subset)

        backtrack(0, [])
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

        def backtrack(i: int, curr_combination: List[str]) -> None:
            if len(curr_combination) == len(digits):
                res.append("".join(curr_combination))
                return
            
            for letter in keypad_map[digits[i]]:
                curr_combination.append(letter)
                backtrack(i + 1, curr_combination)
                curr_combination.pop()

        backtrack(0, [])
        return res

    def compute_tower_of_hanoi(self, n: int, source: str, destination: str, 
                       auxiliary: str) -> None:
        if n == 1:
            print(f"Move disk 1 from {source} to {destination}")
            return

        self.compute_tower_of_hanoi(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        self.compute_tower_of_hanoi(n - 1, auxiliary, destination, source)

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
    def palindrome_decompositions(s: str) -> List[List[str]]:
        res = []
        def bactrack(offset: int, partial_partition: List[str]) -> None:
            if offset == len(s):
                res.append(partial_partition[:])
                return
            
            for i in range(offset + 1, len(s) + 1):
                prefix = s[offset:i]
                if prefix == prefix[::-1]:
                    partial_partition.append(prefix)
                    bactrack(i, partial_partition)
                    partial_partition.pop()

        bactrack(0, [])
        return res
    
    def generate_all_binary_trees(self, num_nodes: int) -> List[BinaryTreeNode]:
        if num_nodes == 0:
            return [None]

        res = []
        for num_left_tree_nodes in range(num_nodes):
            num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes
            left_subtrees = self.generate_all_binary_trees(num_left_tree_nodes)
            right_subtrees = self.generate_all_binary_trees(num_right_tree_nodes)
            res += [BinaryTreeNode(0, left, right)
                    for left in left_subtrees for right in right_subtrees]
        return res

    @staticmethod
    def print_tree_level_order(root: BinaryTreeNode) -> None:
        if not root:
            return

        queue = [root]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node:
                    print(node.val, end=" ")
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    print("null", end=" ")  
            print()

    @staticmethod
    def solve_sudoku(board: List[List[int]]) -> bool:
        def solve_partial_sudoku(i: int, j: int) -> bool:
            if j == len(board):
                j = 0
                i += 1
                if i == len(board):  
                    return True
            
            if board[i][j] != 0:
                return solve_partial_sudoku(i, j + 1)
            
            def valid_to_add(i: int, j: int, val: int) -> bool:
                if val in board[i] or any(val == board[k][j] for k in range(len(board))):
                    return False

                region_size = int(math.sqrt(len(board)))
                region_start_row = (i // region_size) * region_size
                region_start_col = (j // region_size) * region_size
                
                for a, b in itertools.product(range(region_size), repeat=2):
                    if board[region_start_row + a][region_start_col + b] == val:
                        return False
                
                return True
            
            for val in range(1, len(board) + 1):
                if valid_to_add(i, j, val):
                    board[i][j] = val
                    if solve_partial_sudoku(i, j + 1):
                        return True
                    board[i][j] = 0
            
            return False

        return solve_partial_sudoku(0, 0)

    @staticmethod
    def print_sudoku(board: List[List[int]]) -> None:
        region_size = int(math.sqrt(len(board)))
        line_sep = "-" * (len(board) * 2 + region_size + 1)

        for i, row in enumerate(board):
            if i % region_size == 0 and i != 0:
                print(line_sep)  

            row_str = ""
            for j, num in enumerate(row):
                if j % region_size == 0 and j != 0:
                    row_str += "| " 
                row_str += f"{num} " if num != 0 else ". "  

            print(row_str.strip())  
    
    def gray_code(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        recursive_result = self.gray_code(n - 1)
        msb = 1 << (n - 1)

        return recursive_result + [num | msb for num in reversed(recursive_result)]
    
    @staticmethod
    def tree_diameter(adj: List[List[tuple[int, int]]]) -> int:
        n = len(adj)
        if n == 0:
            return 0
        
        def dfs(node: int, parent: int, adj: List[List[tuple[int, int]]]) -> tuple[int, int]:
            max_dist = 0
            for to, weight in adj[node]:
                if to != parent:
                    _, dist = dfs(to, node, adj)
                    max_dist = max(max_dist, dist + weight)
            
            return node, max_dist

        _, diameter = dfs(0, -1, adj)
        return diameter