from collections import deque
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        self.level_next_right = None
        self.locked = False
        self.locked_descendant_count = 0

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key: int) -> bool:
        if not self.root:
            self.root = TreeNode(key)
            return True

        def insert_helper(node, key: int) -> bool:
            if key == node.val:
                return False

            if key < node.val:
                if node.left:
                    return insert_helper(node.left, key)
                else:
                    node.left = TreeNode(key)
                    node.left.parent = node
                    return True
            else:
                if node.right:
                    return insert_helper(node.right, key)
                else:
                    node.right = TreeNode(key)
                    node.right.parent = node
                    return True

        return insert_helper(self.root, key)

    def lookup(self, key: int) -> bool:
        def lookup_helper(node, key: int) -> bool:
            if not node:
                return False
            
            if key == node.val:
                return True
            
            return (lookup_helper(node.left, key) if key < node.val else 
                    lookup_helper(node.right, key))
    
        return lookup_helper(self.root, key)
  
    def remove(self, key: int) -> bool:
        removed = [False]
        def remove_helper(node, key: int, removed: List[bool]) -> TreeNode:
            if not node:
                return None
            
            if key < node.val:
                node.left = remove_helper(node.left, key, removed)
            elif key > node.val:
                node.right = remove_helper(node.right, key, removed)
            else:
                removed[0] = True

                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                # Find the minimum node in the right subtree.
                def find_min(node: TreeNode) -> TreeNode:
                    while node.left:
                        node = node.left
                    return node

                successor = find_min(node.right)
                node.val = successor.val
                node.right = remove_helper(node.right, successor.val, removed)

            return node

        self.root = remove_helper(self.root, key, removed)
        return removed[0]

    def is_symmetric(self, root: TreeNode) -> TreeNode:
        if not root: 
            return False
        
        def is_mirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not right or not left or left.val != right.val:
                return False

            return (is_mirror(left.left, right.right) and 
                   is_mirror(left.right, right.left))

        return is_mirror(root.left, root.right)

    def find_lca(self, root: TreeNode, p: int, q: int) -> TreeNode:
        if not root or root.val == p or root.val == q:
            return root
        
        left = self.find_lca(root.left, p, q)
        right = self.find_lca(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right

    def sum_root_to_leaf(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, current_sum: int) -> int:         # Apply depth-first search.
            if not node:
                return 0

            current_sum = (current_sum << 1) | node.val
            if not node.left and not node.right:
                return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)

    def has_path_weight(self, node: TreeNode, target_weight: int, 
                        current_weight: int) -> bool:
        if not node:
            return False
        
        current_weight += node.val

        if not node.left and not node.right:
            return current_weight == target_weight

        return (self.has_path_weight(node.left, target_weight, current_weight) or 
                self.has_path_weight(node.right, target_weight, current_weight))

    def inorder_traversal(self, k: int) -> List[int]:
        result = []
        if self.root is None:
            return result
        
        counter = 0
        node_stack = []
        current = self.root

        while current or node_stack:
            if current:
                node_stack.append(current)
                current = current.left
            else:
                current = node_stack.pop()
                result.append(current.val)
    
                counter += 1
                if counter == k:
                    print(f"The {k}th node in the inorder traversal is: {current.val}")
                
                current = current.right
        
        return result

    def preorder_traversal(self) -> List[int]:
        result = []
        if not self.root:
            return result
        
        node_stack = [self.root]
        while node_stack:
            current = node_stack.pop()
            if current:
                result.append(current.val)
                node_stack += [current.right, current.left]

        return result

    def compute_successor(self, node: TreeNode) -> TreeNode:
        if not node:
            return None
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            
            return node

        while node.parent and node.parent.right == node:
            node = node.parent
        
        return node.parent

    def inorder_traversal_with_constant_space(self) -> None:
        if not self.root:
            return
        
        current = self.root
        prev = None

        while current:
            if current.parent == prev:
                if current.left:
                    prev = current
                    current = current.left
                else:
                    print(current.val, end=" ")
                    prev = current
                    current = current.right if current.right else current.parent
            elif prev == current.left:
                print(current.val, end=" ")
                prev = current
                current = current.right if current.right else current.parent
            else:
                prev = current
                current = current.parent

    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        in_map = {val: idx for idx, val in enumerate(inorder)}

        def build_tree_helper(pre_start: int, pre_end: int, 
                              in_start: int, in_end: int) -> TreeNode:
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            root_index = in_map[root_val]
            left_subtree_size = root_index - in_start

            root.left = build_tree_helper(pre_start + 1, pre_start + 
                                          left_subtree_size, in_start, root_index - 1)
            root.right = build_tree_helper(pre_start + left_subtree_size + 1, pre_end, 
                                           root_index + 1, in_end)

            return root

        return build_tree_helper(0, len(preorder) - 1, 0, len(inorder) - 1)

    def recursive_inorder_traversal(self, root: TreeNode, result: List[int]) -> None:
        if not root: 
            return result

        self.recursive_inorder_traversal(root.left, result)
        result.append(root.val)
        self.recursive_inorder_traversal(root.right, result)

        return result 

    def recursive_preorder_traversal(self, root: TreeNode, result: List[int]) -> None:
        if not root:
            return result
        
        result.append(root.val)
        self.recursive_preorder_traversal(root.left, result)
        self.recursive_preorder_traversal(root.right, result)

        return result
    
    def reconstruct_preorder(self) -> None:
        if not self.root:
            return

        node_stack = [self.root]
        while node_stack:
            current = node_stack.pop()
            print(current.val, end=" ")

            if current.right:
                node_stack.append(current.right)
            else:
                print("NONE", end=" ")

            if current.left:
                node_stack.append(current.left)
            else:
                print("NONE", end=" ")

    def create_list_from_leaves(self) -> ListNode:
        dummy = ListNode(-1)

        def collect_leaves(root: TreeNode, current: ListNode):
            if not root:
                return current  

            if not root.left and not root.right:
                current.next = ListNode(root.val)
                return current.next  

            current = collect_leaves(root.left, current)
            current = collect_leaves(root.right, current)

            return current
        
        collect_leaves(self.root, dummy)
        return dummy.next

    def print_linked_list(self, head: ListNode) -> None:
        while head:
            print(head.val, end=" ")
            head = head.next

    def exterior_of_binary_tree(self) -> None:
        if not self.root:
            return
        
        current = self.root
        while current.left:
            print(current.val,end=" ")
            current = current.left
        
        leaves = self.create_list_from_leaves()
        self.print_linked_list(leaves)

        right_subtree = self.root
        node_stack = []

        while right_subtree.right:
            right_subtree = right_subtree.right
            node_stack.append(right_subtree)
        
        while node_stack:
            last_part_of_tree = node_stack.pop()
            if last_part_of_tree.left or last_part_of_tree.right:
                print(last_part_of_tree.val,end=" ")

    def right_sibling_tree(self) -> None:
        if not self.root:
            return None
        
        if self.root.left or self.root.right:
            def connect_siblings(left: TreeNode, right: TreeNode) -> None:
                if not left or not right:
                    return

                left.level_next_right = right

                connect_siblings(left.left, left.right)
                connect_siblings(right.left, right.right)
                connect_siblings(left.right, right.left)

            return connect_siblings(self.root.left, self.root.right)

    def print_level_next(self) -> None:
        if not self.root:
            return

        current = self.root
        while current:
            temp = current
            print(temp.val, end=" ")

            while temp:
                if temp.level_next_right:
                    print(f"-> {temp.level_next_right.val}", end=" ")
                else:
                    print("-> NONE")
            
                temp = temp.level_next_right

            if current.left:
                current = current.left
            elif current.right:
                current = current.right
            else:
                current = None
    
    def find_value(self, value: int) -> TreeNode:
        current = self.root
        while current and current.val != value:
            if value < current.val:
                current = current.left
            else:
                current = current.right
        
        return current
    
    @staticmethod
    def can_lock_or_unlock(node: TreeNode) -> bool:
        if not node: 
            return False
        
        ancestor = node.parent
        while ancestor:
            if ancestor.locked: 
                return False
            ancestor = ancestor.parent
        
        if node.locked_descendant_count > 0: 
            return False

        return True

    def lock(self, node: TreeNode) -> bool:
        if not self.can_lock_or_unlock(node):
            return False
        
        node.locked = True
        ancestor = node.parent
        while ancestor:
            ancestor.locked_descendant_count += 1
            ancestor = ancestor.parent
        
        return True
        

    def unlock(self, node: TreeNode) -> bool:
        if not self.can_lock_or_unlock(node):
            return False
        
        node.locked = False
        ancestor = node.parent
        while ancestor:
            ancestor.locked_descendant_count -= 1
            ancestor = ancestor.parent
        
        return True

    def is_bst(self) -> bool:
        def is_bst_helper(node, min_value: int, max_value: int) -> bool:
            if not node:
                return True

            if node.val <= min_value or node.val >= max_value:
                return False

            return (is_bst_helper(node.left, min_value, node.val) and
                    is_bst_helper(node.right, node.val, max_value))
        
        return is_bst_helper(self.root, float('-inf'), float('inf'))

    def first_key_greater(self, input_value: int) -> int:
        first_so_far = None
        current = self.root
        while current:
            if current.val > input_value:
                first_so_far, current = current, current.left
            else:
                current = current.right
        
        return first_so_far.val

    def largest_elements(self, k: int) -> None:
        if not self.root: 
            return
        
        largest_elements = []
        result = self.recursive_inorder_traversal(self.root, largest_elements)

        for i in range(len(result) - 1, len(result) - k - 1, -1):
            print(result[i], end=" ")

    def level_order_traversal(self) -> None:
        if not self.root:
            return

        q = deque([self.root])
        while q:
            level_size = len(q)
            current_level = []

            for i in range(level_size):
                current_node = q.popleft()
                current_level.append(current_node.val)

                if current_node.left: 
                    q.append(current_node.left)
                if current_node.right: 
                    q.append(current_node.right)
            
            print(" ".join(map(str, current_level)))
            
    def first_and_last_occurence(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.lower_bound_binary_search(nums, target)
        upper_bound = self.upper_bound_binary_search(nums, target)
        return [lower_bound, upper_bound]
    
    @staticmethod
    def lower_bound_binary_search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid

        return left if nums and nums[left] == target else -1
    
    @staticmethod
    def upper_bound_binary_search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        return right if nums and nums[right] == target else -1