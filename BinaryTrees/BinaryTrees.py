class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # Inserts a key into the BST.
    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
            return True
        return self.insertHelper(self.root, key)
    
    # Helper function for insertion.
    def insertHelper(self, node, key):
        if key == node.val:
            return False
        
        if key < node.val:
            if node.left:
                return self.insertHelper(node.left, key)
            else:
                node.left = TreeNode(key)
                return True
        else:
            if node.right:
                return self.insertHelper(node.right, key)
            else:
                node.right = TreeNode(key)
                return True
    
    # Looks up for the specified node in the BST.
    def lookUp(self, key):
        return self.lookUpHelper(self.root, key)

    # Helper function for lookup.
    def lookUpHelper(self, node, key):
        if not node:
            return False
        if key == node.val:
            return True
        
        return self.lookUpHelper(node.left, key) if key < node.val else self.lookUpHelper(node.right, key)
    
    # Removes a key from the BST.
    def remove(self, key):
        removed = [False]
        self.root = self.removeHelper(self.root, key, removed)
        return removed[0]
    
    # Helper function for removal.
    def removeHelper(self, node, key, removed):
        if not node:
            return None
        
        if key < node.val:
            node.left = self.removeHelper(node.left, key, removed)
        elif key > node.val:
            node.right = self.removeHelper(node.right, key, removed)
        else:
            removed[0] = True

            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            successor = self.findMin(node.right)
            node.val = successor.val
            node.right = self.removeHelper(node.right, successor.val, removed)

        return node
    
    # Finds the minimum value node in a subtree.
    def findMin(self, node):
        while node.left:
            node = node.left

        return node
    
    # Check if the tree's both sides mirroring each other.
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not right or not left or left.val != right.val:
            return False
        
        return (self.isMirror(left.left, right.right) and 
               self.isMirror(left.right, right.left))
    
    # Checks if the tree is symmetric.
    def isSymmetric(self, root):
        if not root: 
            return False
        return self.isMirror(root.left, root.right)
    
    # Finds the lowest common ancestor.
    def findLCA(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right
        
    # Finds the binary numbers that represented by the tree.
    def sumRootToLeaf(self, root):
        return self.dfs(root, 0)

    # Apply depth-first search.
    def dfs(self, node, currentsum):
        if not node:
            return 0
        
        currentsum = (currentsum << 1) | node.val

        if not node.left and not node.right:
            return currentsum
        
        return self.dfs(node.left, currentsum) + self.dfs(node.right, currentsum)

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
