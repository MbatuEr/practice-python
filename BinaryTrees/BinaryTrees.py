import sys
from collections import deque

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
    

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
            return True

        def insert_helper(node, key):
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

    def lookup(self, key):
        def lookup_helper(node, key):
            if not node:
                return False
            if key == node.val:
                return True
            
            return lookup_helper(node.left, key) if key < node.val else lookup_helper(node.right, key)
    
        return lookup_helper(self.root, key)
  
    def remove(self, key):
        removed = [False]

        def remove_helper(node, key, removed):
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
                def find_min(node):
                    while node.left:
                        node = node.left
                    return node

                successor = find_min(node.right)
                node.val = successor.val
                node.right = remove_helper(node.right, successor.val, removed)

            return node

        self.root = remove_helper(self.root, key, removed)
        return removed[0]

    def is_symmetric(self, root):
        if not root: 
            return False
        
        def is_mirror(left, right):
            if not left and not right:
                return True
            if not right or not left or left.val != right.val:
                return False

            return (is_mirror(left.left, right.right) and 
                   is_mirror(left.right, right.left))

        return is_mirror(root.left, root.right)

    def find_lca(self, root, p, q):
        if not root or root.val == p or root.val == q:
            return root
        
        left = self.find_lca(root.left, p, q)
        right = self.find_lca(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right

    def sum_root_to_leaf(self, root):
            
        # Apply depth-first search.
        def dfs(node, currentsum):
            if not node:
                return 0

            currentsum = (currentsum << 1) | node.val

            if not node.left and not node.right:
                return currentsum

            return dfs(node.left, currentsum) + dfs(node.right, currentsum)
        
        return dfs(root, 0)

    def has_path_weight(self, node, targetweight, currentweight):
        if not node:
            return False
        
        currentweight += node.val

        if not node.left and not node.right:
            return currentweight == targetweight

        return (self.has_path_weight(node.left, targetweight, currentweight) or 
                self.has_path_weight(node.right, targetweight, currentweight))

    def inorder_traversal(self, root, k):
        result = []
        if root is None:
            return result
        counter = 0
        nodeStack = []
        current = root

        while current or nodeStack:
            if current:
                nodeStack.append(current)
                current = current.left
            else:
                current = nodeStack.pop()
                result.append(current.val)
    
                counter += 1
                if counter == k:
                    print(f"The {k}th node in the inorder traversal is: {current.val}")
                
                current = current.right
        
        return result

    def preorder_traversal(self, root):
        result = []
        if root is None:
            return result
        
        nodestack = [root]
        while nodestack:
            current = nodestack.pop()
            if current:
                result.append(current.val)
                nodestack += [current.right, current.left]

        return result

    def find_value(self, value):
        current = self.root
        while current and current.val != value:
            if value < current.val:
                current = current.left
            else:
                current = current.right
        
        return current

    def compute_successor(self, node):
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

    def inorder_traversal_with_constant_space(self, root):
        if root is None:
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

    def build_tree(self, preorder, inorder):
        in_map = {val: idx for idx, val in enumerate(inorder)}

        def build_tree_helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            root_index = in_map[root_val]
            left_subtree_size = root_index - in_start

            root.left = build_tree_helper(pre_start + 1, pre_start + left_subtree_size, in_start, root_index - 1)
            root.right = build_tree_helper(pre_start + left_subtree_size + 1, pre_end, root_index + 1, in_end)

            return root

        return build_tree_helper(0, len(preorder) - 1, 0, len(inorder) - 1)

    def reconstruct_preorder(self, node):
        if node is None:
            return

        nodestack = []
        nodestack.append(node)

        while nodestack:
            current = nodestack.pop()
            print(current.val, end=" ")

            if current.right:
                nodestack.append(current.right)
            else:
                print("NONE", end=" ")

            if current.left:
                nodestack.append(current.left)
            else:
                print("NONE", end=" ")

    def create_list_from_leaves(self, root):
        dummy = ListNode(-1)

        def collect_leaves(root, current):
            if not root:
                return current  

            if not root.left and not root.right:
                current.next = ListNode(root.val)
                return current.next  

            current = collect_leaves(root.left, current)
            current = collect_leaves(root.right, current)

            return current
        
        collect_leaves(root, dummy)
        return dummy.next

    def print_linked_list(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next

    def exterior_of_binary_tree(self, root):
        if not root:
            return
        
        current = root
        while current.left:
            print(current.val,end=" ")
            current = current.left
        
        leaves = self.create_list_from_leaves(root)
        self.print_linked_list(leaves)

        right_subtree = root
        nodestack = []
        nodestack.append(right_subtree)

        while right_subtree.right:
            right_subtree = right_subtree.right
            nodestack.append(right_subtree)
        
        while nodestack:
            last_part_of_tree = nodestack.pop()
            if last_part_of_tree.left or last_part_of_tree.right:
                print(last_part_of_tree.val,end=" ")

    def right_sibling_tree(self, root):
        if not root or root.left or root.right:

            def set_level_next_field(left_tree, right_tree):
                if not left_tree or not right_tree:
                    return
                left_tree.level_next_right = right_tree

                set_level_next_field(left_tree.left, left_tree.right)
                set_level_next_field(right_tree.left, right_tree.right)
                set_level_next_field(left_tree.right, right_tree.left)
            
            return set_level_next_field(root.left, root.right)

    def print_level_next(self, root):
        if not root : return

        current = root
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

    def can_lock_or_unlock(self, node):
        if not node: return False
        ancestor = node.parent
        while ancestor:
            if ancestor.locked: return False
            ancestor = ancestor.parent
        
        if node.locked_descendant_count > 0: return False

        return True

    def lock(self, node):
        if self.can_lock_or_unlock(node):
            node.locked = True
            ancestor = node.parent

            while ancestor:
                ancestor.locked_descendant_count += 1
                ancestor = ancestor.parent
            return True
        
        return False

    def unlock(self, node):
        if self.can_lock_or_unlock(node):
            node.locked = False
            ancestor = node.parent

            while ancestor:
                ancestor.locked_descendant_count -= 1
                ancestor = ancestor.parent
            return True
        
        return False
    

    def is_bst(self):
        def is_bst_helper(node, min_value, max_value):
            if not node:
                return True

            if node.val <= min_value or node.val >= max_value:
                return False

            return (is_bst_helper(node.left, min_value, node.val) and
                    is_bst_helper(node.right, node.val, max_value))
        
        return is_bst_helper(self.root, float('-inf'), float('inf'))

    def first_key_greater(self, input_value):
        first_so_far = None
        current = self.root
        while current:
            if current.val > input_value:
                first_so_far, current = current, current.left
            else:
                current = current.right
        
        return first_so_far.val

    def recursive_inorder_traversal(self, root, result):
        if not root: return result

        self.recursive_inorder_traversal(root.left, result)

        result.append(root.val)

        self.recursive_inorder_traversal(root.right, result)

        return result 

    def largest_element(self, root, k):
        if not root: return
        largest_element = []
        result = self.recursive_inorder_traversal(root, largest_element)

        for i in range(len(result) - 1, len(result) - k - 1, -1):
            print(result[i], end=" ")

    def level_order_traversal(self, root):
        if not root: return

        q = deque([root])

        while q:
            levelsize = len(q)
            current_level = []

            for i in range(levelsize):
                currentnode = q.popleft()
                current_level.append(currentnode.val)

                if currentnode.left: q.append(currentnode.left)
                if currentnode.right: q.append(currentnode.right)
            
            print(" ".join(map(str, current_level)))
            