from typing import Dict, List, Tuple
from collections import deque, defaultdict
import string, heapq

class GraphNode:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []

class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
    def union(self, x: int, y: int) -> bool:
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]
            return True
        
        return False
    
    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]
  
class MergingCommunities:
    def __init__(self, n: int):
        self.uf = UnionFind(n)
    
    def connect(self, x: int, y: int) -> None:
        return self.uf.union(x, y)
    
    def get_community_size(self, x: int) -> int:
        return self.uf.get_size(x)

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
    
    def count_island(self, matrix : List[List[int]]) -> int:
        if not matrix:
            return 0
        
        def dfs(r: int, c: int, matrix: List[List[int]]) -> None:
            matrix[r][c] = -1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                next_r, next_c = r + dr, c+ dc
                if self.is_within_bounds(next_r, next_c, matrix) and matrix[next_r][next_c] == 1:
                    dfs(next_r, next_c, matrix)    
        
        count = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    dfs(r, c, matrix)
                    count += 1
        
        return count

    @staticmethod
    def is_within_bounds(r: int , c: int, matrix: List[List[int]]) -> bool:
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

        def dfs(r: int, c: int, matrix: List[List[int]], memo: List[List[int]]) -> int:
            if memo[r][c] != 0:
                return memo[r][c]

            max_path = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                next_r, next_c = r + dr, c+ dc
                if self.is_within_bounds(next_r, next_c, matrix) and matrix[next_r][next_c] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(next_r, next_c, matrix, memo))

            memo[r][c] = max_path
            return max_path

        res = 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c, matrix, memo))
        
        return res
    
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
    
    @staticmethod
    def connect_the_dots(points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = (abs(points[i][0] - points[j][0]) +
                        abs(points[i][1] - points[j][1]))
                edges.append((cost, i, j))
            
        edges.sort()
        uf = UnionFind(n)
        total_cost = edges_added = 0

        # Implement Kruskal's Algorithm.
        for cost, p1, p2 in edges:
            if uf.union(p1, p2):
                total_cost += cost
                edges_added += 1
                if edges_added == n - 1:
                    return total_cost
    
    @staticmethod
    def prerequisites(n: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degrees = [0] * n
        for prerequsite, course in prerequisites:
            graph[prerequsite].append(course)
            in_degrees[course] += 1
        
        queue = deque()
        for i in range(n):
            if in_degrees[i] == 0:
                queue.append(i)
        enrolled_courses = 0

        # Perform topological sort (Kahn's Algorithm).
        while queue:
            node = queue.popleft()
            enrolled_courses += 1
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return enrolled_courses == n
    
    @staticmethod
    def dijkstra_s_algorithm(n: int, edges: List[int], start: int) -> List[int]:
        graph = defaultdict(list)
        distances = [float("inf")] * n
        distances[start] = 0

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        min_heap = [(0, start)]
        while min_heap:
            curr_dist, curr_node = heapq.heappop(min_heap)
            if curr_dist > distances[curr_node]:
                continue
            
            for neighbor, weight in graph[curr_node]:
                neighbor_dist = curr_dist + weight
                if neighbor_dist < distances[neighbor]:
                    distances[neighbor] = neighbor_dist
                    heapq.heappush(min_heap, (neighbor_dist, neighbor))

        return [-1 if dist == float("inf") else dist for dist in distances]
    
    @staticmethod
    def bellman_ford(num_vertices: int, edges: List[Tuple[int, int, int]], src: int) -> List[float]:
        dist = [float("inf")] * num_vertices
        dist[src] = 0

        # Relax all edges v - 1 times
        for _ in range(num_vertices - 1):
            for u, v, w in edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # Check for negative cycles
        for u,v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains a negative weighted cycle!")
                return None
        
        return dist

    @staticmethod
    def floyd_warshall(graph: List[List[float]]) -> List[List[float]]:
        num_vertices = len(graph)
        dist = [row[:] for row in graph]
        for k in range(num_vertices):    
            for i in range(num_vertices):    
                for j in range(num_vertices): 
                    if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        return dist