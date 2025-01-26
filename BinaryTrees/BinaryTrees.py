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
    
        # Inserts a key into the BST.
    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
            return True

        # Helper function for insertion.
        def insertHelper(node, key):
            if key == node.val:
                return False

            if key < node.val:
                if node.left:
                    return insertHelper(node.left, key)
                else:
                    node.left = TreeNode(key)
                    node.left.parent = node
                    return True
            else:
                if node.right:
                    return insertHelper(node.right, key)
                else:
                    node.right = TreeNode(key)
                    node.right.parent = node
                    return True

        # Call the helper function.
        return insertHelper(self.root, key)
    
    # Looks up for the specified node in the BST.
    def lookUp(self, key):
        # Helper function for lookup.
        def lookUpHelper(node, key):
            if not node:
                return False
            if key == node.val:
                return True
            
            return lookUpHelper(node.left, key) if key < node.val else lookUpHelper(node.right, key)
    
        return lookUpHelper(self.root, key)
  
    # Removes a key from the BST.
    def remove(self, key):
        removed = [False]

        # Helper function for removal, nested inside `remove`.
        def removeHelper(node, key, removed):
            if not node:
                return None
            
            if key < node.val:
                node.left = removeHelper(node.left, key, removed)
            elif key > node.val:
                node.right = removeHelper(node.right, key, removed)
            else:
                removed[0] = True

                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                # Find the minimum node in the right subtree.
                def findMin(node):
                    while node.left:
                        node = node.left
                    return node

                successor = findMin(node.right)
                node.val = successor.val
                node.right = removeHelper(node.right, successor.val, removed)

            return node

        # Call the helper function.
        self.root = removeHelper(self.root, key, removed)
        return removed[0]
        
    # Checks if the tree is symmetric.
    def isSymmetric(self, root):
        if not root: 
            return False
        
        # Check if the tree's both sides mirroring each other.
        def isMirror(left, right):
            if not left and not right:
                return True
            if not right or not left or left.val != right.val:
                return False

            return (isMirror(left.left, right.right) and 
                   isMirror(left.right, right.left))

        return isMirror(root.left, root.right)
    
    # Finds the lowest common ancestor.
    def findLCA(self, root, p, q):
        if not root or root.val == p or root.val == q:
            return root
        
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right
        
    # Finds the binary numbers that represented by the tree.
    def sumRootToLeaf(self, root):
            
        # Apply depth-first search.
        def dfs(node, currentsum):
            if not node:
                return 0

            currentsum = (currentsum << 1) | node.val

            if not node.left and not node.right:
                return currentsum

            return dfs(node.left, currentsum) + dfs(node.right, currentsum)
        
        return dfs(root, 0)

    # Checks if there exists a leaf whose path weight equals the given integer.
    def hasPathWeight(self, node, targetweight, currentweight):
        if not node:
            return False
        
        currentweight += node.val

        if not node.left and not node.right:
            return currentweight == targetweight

        return (self.hasPathWeight(node.left, targetweight, currentweight) or 
                self.hasPathWeight(node.right, targetweight, currentweight))

    # Builds a tree from an inorder traversal without a recursion or parent references.
    def inorderTraversal(self, root, k):
        result = []
        if root is None:
            return result
        counter = 0
        nodeStack = []
        current = root

        while current or nodeStack:
            while current:
                nodeStack.append(current)
                current = current.left
            
            current = nodeStack.pop()
            result.append(current.val)

            counter += 1
            if counter == k:
                print(f"The {k}th node in the inorder traversal is: {current.val}")
            
            current = current.right
        
        return result

    # Builds a tree from a preorder traversal without a recursion or parent references.
    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
        
        nodestack = []
        nodestack.append(root)

        while nodestack:
            current = nodestack.pop()
            result.append(current.val)
            
            if current.right:
                nodestack.append(current.right)
            if current.left:
                nodestack.append(current.left)
        
        return result

    # Helper function to find a node by value.
    def findValue(self, value):
        current = self.root
        while current and current.val != value:
            if value < current.val:
                current = current.left
            else:
                current = current.right
        
        return current

    # Computes the successor of the node in an inorder traversal.
    def computeSuccessor(self, node):
        if not node:
            return None
        
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            
            return current

        current = node
        parent = node.parent

        while parent and parent.right == current:
            current = parent
            parent = parent.parent
        
        return parent
    
    # Does an inorder traversal with a O(1) space complexity.
    def inorderTraversalWithO1Space(self, root):
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

    # Main function to build a binary tree.
    def buildTree(self, preorder, inorder):
        in_map = {val: idx for idx, val in enumerate(inorder)}

        # Helper function to build a binary tree.
        def buildTreeHelper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            root_index = in_map[root_val]
            left_subtree_size = root_index - in_start

            root.left = buildTreeHelper(pre_start + 1, pre_start + left_subtree_size, in_start, root_index - 1)
            root.right = buildTreeHelper(pre_start + left_subtree_size + 1, pre_end, root_index + 1, in_end)

            return root

        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)
    
    # Builds a tree from a preorder traversal and uses null to mark empty children.
    def reconstructPreorder(self, node):
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

    # Creates a linked list from leaves of the tree.
    def createListFromLeaves(self, root):
        dummy = ListNode(-1)
        
        # Helper function to traverse the tree and collect leaves.
        def collectLeaves(root, current):
            if not root:
                return current  

            if not root.left and not root.right:
                current.next = ListNode(root.val)
                return current.next  

            current = collectLeaves(root.left, current)
            current = collectLeaves(root.right, current)

            return current
        
        collectLeaves(root, dummy)
        return dummy.next

    # Prints the linked list.
    def printLinkedList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
    
    # Computes the exterior of a binary tree.
    def exteriorOfBinaryTree(self, root):
        if not root:
            return
        
        current = root
        while current.left:
            print(current.val,end=" ")
            current = current.left
        
        leaves = self.createListFromLeaves(root)
        self.printLinkedList(leaves)

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
    
    # Sets the node to its level next right node.
    def rightSiblingTree(self, root):
        if not root or root.left or root.right:
            
            # Helper funtion to set the nodes to next level field.
            def setLevelNextField(left_tree, right_tree):
                if not left_tree or not right_tree:
                    return
                left_tree.level_next_right = right_tree

                setLevelNextField(left_tree.left, left_tree.right)
                setLevelNextField(right_tree.left, right_tree.right)
                setLevelNextField(left_tree.right, right_tree.left)
            
            return setLevelNextField(root.left, root.right)
        
    # Prints the nodes in order of their level.
    def printLevelNext(self, root):
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

    # Checks if any ancestors or descendants are locked.
    def canLockOrUnlock(self, node):
        if not node: return False
        ancestor = node.parent
        while ancestor:
            if ancestor.locked: return False
            ancestor = ancestor.parent
        
        if node.locked_descendant_count > 0: return False

        return True
    
    # Function to lock the node.
    def lock(self, node):
        if self.canLockOrUnlock(node):
            node.locked = True
            ancestor = node.parent

            while ancestor:
                ancestor.locked_descendant_count += 1
                ancestor = ancestor.parent
            return True
        
        return False

    # Function to unlock the node.
    def unlock(self, node):
        if self.canLockOrUnlock(node):
            node.locked = False
            ancestor = node.parent

            while ancestor:
                ancestor.locked_descendant_count -= 1
                ancestor = ancestor.parent
            return True
        
        return False
    
    # Checks if a binary tree satisfies the BST property.
    def is_BST(self):
        
        # Helper function to check if a binary tree satisfies the BST property.
        def isBSTHelper(node, min_value, max_value):
            if not node:
                return True

            if node.val <= min_value or node.val >= max_value:
                return False

            return (isBSTHelper(node.left, min_value, node.val) and
                    isBSTHelper(node.right, node.val, max_value))
        
        return isBSTHelper(self.root, float('-inf'), float('inf'))
    
    # Finds the first key greater than the input key.
    def firstKeyGreater(self, input_value):
    
        # Helper function for finding the first key greater than the input value.
        def firstKeyGreaterHelper(node, input_value, first_key_appeared):
            if not node:
                return first_key_appeared

            if node.val > input_value:
                first_key_appeared = min(first_key_appeared, node.val)

            if node.val > input_value:
                return firstKeyGreaterHelper(node.left, input_value, first_key_appeared)
            else:
                return firstKeyGreaterHelper(node.right, input_value, first_key_appeared)

        result = firstKeyGreaterHelper(self.root, input_value, float('inf'))
        return -1 if result == float('inf') else result

    # Recursive function to get inorder traversal.
    def recursiveInorderTraversal(self, root, result):
        if not root: return result

        self.recursiveInorderTraversal(root.left, result)

        result.append(root.val)

        self.recursiveInorderTraversal(root.right, result)

        return result 

    # Finds the k larger elements in a BST.
    def largestElement(self, root, k):
        if not root: return
        largest_element = []
        result = self.recursiveInorderTraversal(root, largest_element)

        for i in range(len(result) - 1, len(result) - k - 1, -1):
            print(result[i], end=" ")
        
    # Prints a binary tree in level-order.
    def levelOrderTraversal(self, root):
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
            