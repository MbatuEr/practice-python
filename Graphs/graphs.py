from typing import Dict, List
from collections import deque
import string
class GraphNode:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []

class Graphs:
    @staticmethod
    def graph_deep_copy(node : GraphNode) -> GraphNode:
        if not node:
            return None
        def dfs(node: GraphNode, clone_map: Dict[GraphNode, GraphNode]) -> GraphNode:
            if node in clone_map:
                return clone_map[node]

            cloned_node = GraphNode(node.val)
            clone_map[node] = cloned_node

            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor, clone_map)
                cloned_node.neighbors.append(cloned_neighbor)

            return cloned_node
        return dfs(node, {})

    def count_island(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
                        
        count = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    self.dfs_for_count_island(r, c, matrix)
                    count += 1
        return count    
    
    def dfs_for_count_island(self, r: int, c: int, matrix: List[List[int]]) -> None:
        matrix[r][c] = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            next_r, next_c = r + dr, c + dc
            if (self.is_within_bounds(next_r, next_c, matrix) 
                and matrix[next_r][next_c] == 1):
                self.dfs_for_count_island(next_r, next_c, matrix)

    @staticmethod
    def is_within_bounds(r: int, c: int, matrix: List[List[int]]) -> bool:
        return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])                

    def matrix_infection(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        ones = seconds = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    ones += 1
                elif matrix[r][c] == 2:
                    queue.append((r, c))
        
        while queue and ones > 0:
            seconds += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    next_r, next_c = r + dr, c + dc
                    if (self.is_within_bounds(next_r, next_c, matrix) 
                        and matrix[next_r][next_c] == 1):
                        matrix[next_r][next_c] = 2
                        ones -= 1
                        queue.append((next_r, next_c))
    
        return seconds if ones == 0 else -1
    
    @staticmethod
    def bipartite_graph_validation(graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)

        def dfs(node: int, color: int) -> bool:
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
        
            return True

        for i in range(len(graph)):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        
        return True    

    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        res = 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                res = max(res, self.dfs_for_longest_increasing_path(r, c, matrix, memo))
        
        return res
    
    def dfs_for_longest_increasing_path(self, r: int, c: int, matrix: List[List[int]], 
                                        memo: List[List[int]]) -> int:
        if memo[r][c] != 0:
            return memo[r][c]
        
        max_path = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            next_r, next_c = r + dr, c + dc
            if(self.is_within_bounds(next_r, next_c, matrix) 
               and matrix[next_r][next_c] > matrix[r][c]):
                max_path = max(max_path, 1 + self.dfs_for_longest_increasing_path(next_r, next_c, matrix, memo))       
        
        memo[r][c] = max_path
        return max_path

    def shortest_transformation_sequence(self, start: str, end: str, dictionary: List[str]) -> int:
        dictionary_set = set(dictionary)
        if end not in dictionary_set:
            return 0
        if start == end:
            return 1
        
        start_queue = deque([start])
        start_visited = {start}
        end_queue = deque([end])
        end_visited = {end}
        level = 0

        while start_queue and end_queue:
            level += 1
            if self.explore_level(start_queue, start_visited, end_visited, dictionary_set):
                return level

            level += 1
            if self.explore_level(end_queue, end_visited, start_visited, dictionary_set):
                return level

        return 0 
    
    @staticmethod
    def explore_level(queue: deque, visited: set, other_visited: set, dictionary_set: set) -> bool:
        for _ in range(len(queue)):
            current_word = queue.popleft()
            for i in range(len(current_word)):
                for c in string.ascii_lowercase:  
                    next_word = current_word[:i] + c + current_word[i + 1:]
                    if next_word in other_visited:  
                        return True
                    if next_word in dictionary_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append(next_word)
                        dictionary_set.remove(next_word) 
        
        return False