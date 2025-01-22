from BinaryTrees import BinaryTree
from BinaryTrees import TreeNode

if __name__ == "__main__":
    tree = BinaryTree()

    # Insertion, lookup and removal.
    tree.insert(5)
    tree.insert(3)
    tree.insert(8)
    tree.insert(1)
    tree.insert(4)

    print(tree.lookUp(3)) 
    print(tree.lookUp(6)) 

    print(tree.remove(3))  
    print(tree.lookUp(3))  
    print(tree.remove(6))  
    print("----------------------------------------------------------")

    # Check if the tree is symmetrical.
    root_symmetrical = TreeNode(1)
    root_symmetrical.left = TreeNode(2)
    root_symmetrical.right = TreeNode(2)
    root_symmetrical.left.left = TreeNode(3)
    root_symmetrical.left.right = TreeNode(4)
    root_symmetrical.right.left = TreeNode(4)
    root_symmetrical.right.right = TreeNode(3)

    if tree.isSymmetric(root_symmetrical):
        print("The tree is symmetric.")
    else:
        print("The tree is not symmetric.")
    print("----------------------------------------------------------")

    # Find the lowest common ancestor.
    rootLCA = TreeNode(8)
    rootLCA.left = TreeNode(4)
    rootLCA.right = TreeNode(12)
    rootLCA.left.left = TreeNode(2)
    rootLCA.left.right = TreeNode(6)
    rootLCA.right.left = TreeNode(10)
    rootLCA.right.right = TreeNode(14)
    rootLCA.left.left.right = TreeNode(3)
    rootLCA.right.left.left = TreeNode(9)
    rootLCA.right.left.right = TreeNode(11)
    rootLCA.right.right.left = TreeNode(13)
    rootLCA.right.right.right = TreeNode(16)

    p = rootLCA.left.left.right
    q = rootLCA.left.right

    lca = tree.findLCA(rootLCA, p, q)
    if lca:
        print(f"The lowest common ancestor of {p.val} and {q.val} is {lca.val}")
    else:
        print(f"The lowest common ancestor of {p.val} and {q.val} is not found.")
    print("----------------------------------------------------------")

    # Sum of binary numbers represented by root-to-leaf paths
    rootsum = TreeNode(1)
    rootsum.left = TreeNode(0)
    rootsum.right = TreeNode(1)
    rootsum.left.left = TreeNode(0)
    rootsum.left.right = TreeNode(1)
    rootsum.right.left = TreeNode(0)
    rootsum.right.right = TreeNode(0)
    rootsum.left.left.left = TreeNode(0)
    rootsum.left.left.right = TreeNode(1)
    rootsum.left.right.right = TreeNode(1)
    rootsum.right.left.right = TreeNode(0)
    rootsum.right.right.right = TreeNode(0)
    rootsum.left.right.right.left = TreeNode(0)
    rootsum.right.left.right.left = TreeNode(1)
    rootsum.right.left.right.right = TreeNode(0)
    rootsum.right.left.right.left.right = TreeNode(1)

    print("Sum of binary numbers represented by root-to-leaf paths:",
          tree.sumRootToLeaf(rootsum))
    print("----------------------------------------------------------")

    # Path weight equals a target value
    rootsumweight = TreeNode(5)
    rootsumweight.left = TreeNode(3)
    rootsumweight.right = TreeNode(8)
    rootsumweight.left.left = TreeNode(2)
    rootsumweight.left.right = TreeNode(4)
    rootsumweight.right.left = TreeNode(7)
    rootsumweight.right.right = TreeNode(11)
    rootsumweight.left.left.left = TreeNode(1)
    rootsumweight.right.right.right = TreeNode(13)

    target_weight = 20
    current_value = 0
    if tree.hasPathWeight(rootsumweight, target_weight, current_value):
        print(f"There exists a leaf whose path weight equals {target_weight}.")
    else:
        print(f"No leaf path weight equals {target_weight}.")
    print("----------------------------------------------------------")    

    # Inorder traversal without recursion.
    tree_order = BinaryTree()

    values = [8, 6, 10, 4, 7, 9, 13, 5, 12, 14]
    for val in values:
        tree_order.insert(val)

    k = 7
    inorder_traversal = tree_order.inorderTraversal(tree_order.root, k)
    print("The inorder traversal of the binary tree:", inorder_traversal)
    print("----------------------------------------------------------")

    # Preorder traversal without recursion.
    preorder_traversal = tree_order.preorderTraversal(tree_order.root)

    print("The preorder traversal of the binary tree:", preorder_traversal)
    print("----------------------------------------------------------")
    