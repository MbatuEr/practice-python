from BinaryTrees import BinaryTree
from BinaryTrees import TreeNode

if __name__ == "__main__":
    tree = BinaryTree()

    # Insertion, lookup and removal.
    items_to_insert = [10,5,15,3,7,12,10]
    for values in items_to_insert:
        tree.insert(values)

    print(tree.lookUp(3)) 
    print(tree.lookUp(7)) 
    print(tree.remove(3))  
    print(tree.lookUp(3))  
    print(tree.remove(7))
    print(tree.lookUp(7))  
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
    tree_LCA = BinaryTree()
    order_of_tree = [8,4,12,2,6,10,14,3,9,11,13,16]
    for i in order_of_tree:
        tree_LCA.insert(i)

    p = 3
    q = 6

    lca = tree_LCA.findLCA(tree_LCA.root, p, q)
    if lca:
        print(f"The lowest common ancestor of {p} and {q} is {lca.val}")
    else:
        print(f"The lowest common ancestor of {p} and {q} is not found.")
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
    path_weight = BinaryTree()
    path_weight_order = [5,3,8,2,4,7,11,1,13]

    for i in path_weight_order:
        path_weight.insert(i)

    target_weight = 20
    current_value = 0

    if tree.hasPathWeight(path_weight.root, target_weight, current_value):
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
    
    # Successor of a root.
    node = tree_order.findValue(10)
    if node:
        print(f"node found: {node.val}")
        successor = tree_order.computeSuccessor(node)

        if successor:
            print(f"Successor of {node.val} is: {successor.val}")
        else:
            print(f"No successor for {node.val}")
    else:
        print("Node is not found in the tree.")
    print("----------------------------------------------------------")

    # Inorder travelsal with O(1) space complexity.
    print("The inorder traversal of the binary tree: ",end="")
    tree_order.inorderTraversalWithO1Space(tree_order.root)
    print("\n----------------------------------------------------------")

    # Build a binary tree.
    inorder = [4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
    preorder = [8, 6, 4, 5, 7, 10, 9, 13, 12, 14]

    root_order = tree.buildTree(preorder, inorder)
    k = 3
    print("Inorder traversal of the reconstructed tree:")
    inorder_traversal_tree = tree.inorderTraversal(root_order, k)
    print(inorder_traversal_tree)

    print("Preorder traversal of the reconstructed tree:")
    preorder_traversal_tree = tree.preorderTraversal(root_order)
    print(preorder_traversal_tree)
    print("\n----------------------------------------------------------")

    # Reconstruct preorder traversal.
    tree_order.reconstructPreorder(tree_order.root)
    print("\n----------------------------------------------------------")

    # Create list from leaves.
    leaflist = tree_order.createListFromLeaves(tree_order.root)
    print("Linked list of leaves: ", end=" ")
    tree_order.printLinkedList(leaflist)
    print("\n----------------------------------------------------------")
    
    # Compute exterior. 
    exterior = BinaryTree()
    root_exterior = [8,4,13,2,5,11,16,1,3,7,12,14,18,6]
    for i in root_exterior:
        exterior.insert(i)
    exterior.exteriorOfBinaryTree(exterior.root)
    print("\n----------------------------------------------------------")

    # Right sibling tree.
    sibling = BinaryTree()
    right_sibling = [8,4,13,2,6,10,16,1,3,5,7,9,11,14,18]
    for values in right_sibling:
        sibling.insert(values)
    
    sibling.rightSiblingTree(sibling.root)
    sibling.printLevelNext(sibling.root)
    print("----------------------------------------------------------")

    # Lock the node.
    locked = BinaryTree()
    root_lock = [4,2,6,1,3,5,7]

    for values in root_lock:
        locked.insert(values)
    
    lock_node1 = locked.findValue(1)
    lock_node3 = locked.findValue(3)
    lock_node2 = locked.findValue(2)

    print(f"Locking node 1: {'Success' if locked.lock(lock_node1) else 'Failed'}")
    print(f"Locking node 3: {'Success' if locked.lock(lock_node3) else 'Failed'}")
    print(f"Locking node 2 (parent of 1 and 3): {'Success' if locked.lock(lock_node2) else 'Failed'}")
    print(f"Unlocking node 3: {'Success' if locked.unlock(lock_node3) else 'Failed'}")
    print(f"Locking node 2 after unlocking node 3: {'Success' if locked.lock(lock_node2) else 'Failed'}")
    print(f"Unlocking node 1: {'Success' if locked.unlock(lock_node1) else 'Failed'}")
    print(f"Locking node 2 after unlocking node 1: {'Success' if locked.lock(lock_node2) else 'Failed'}")
    print("----------------------------------------------------------")

    # Check if the tree satisfies the BST property
    bst = BinaryTree()
    root_bst = [8, 4, 12, 2, 6, 10, 14]

    for value in root_bst:
        bst.insert(value)

    if bst.is_BST():
        print("The tree satisfies the BST property.")
    else:
        print("The tree does NOT satisfy the BST property.")
    print("----------------------------------------------------------")
    # Find the first key greater than the input key
    input_key = 13
    first_key = bst.firstKeyGreater(input_key)

    if first_key != -1:
        print(f"The first key greater than {input_key} is {first_key}.")
    else:
        print(f"No key greater than {input_key} found.")
    print("----------------------------------------------------------")

    # Largest elements.
    number_of_largest_items = 3
    tree.largestElement(tree_order.root, number_of_largest_items)
    print("\n----------------------------------------------------------")

    # Level order tree traversal.
    tree.levelOrderTraversal(tree_order.root)
    print("----------------------------------------------------------")