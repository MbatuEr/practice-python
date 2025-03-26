from BinaryTrees import BinaryTree
from BinaryTrees import TreeNode

if __name__ == "__main__":
    tree = BinaryTree()

    # Insertion, lookup and removal.
    items_to_insert = [10,5,15,3,7,12,10]
    for values in items_to_insert:
        tree.insert(values)

    print(tree.lookup(3)) 
    print(tree.lookup(7)) 
    print(tree.remove(3))  
    print(tree.lookup(3))  
    print(tree.remove(7))
    print(tree.lookup(7))
    print("-" * 60)

    # Symmetrical tree
    root_symmetrical = TreeNode(1)
    root_symmetrical.left = TreeNode(2)
    root_symmetrical.right = TreeNode(2)
    root_symmetrical.left.left = TreeNode(3)
    root_symmetrical.left.right = TreeNode(4)
    root_symmetrical.right.left = TreeNode(4)
    root_symmetrical.right.right = TreeNode(3)

    if tree.is_symmetric(root_symmetrical):
        print("The tree is symmetric.")
    else:
        print("The tree is not symmetric.")
    print("-" * 60)

    # Lowest common ancestor
    tree_LCA = BinaryTree()
    order_of_tree = [8,4,12,2,6,10,14,3,9,11,13,16]
    for i in order_of_tree:
        tree_LCA.insert(i)

    p = 3
    q = 6

    lca = tree_LCA.find_lca(tree_LCA.root, p, q)
    if lca:
        print(f"The lowest common ancestor of {p} and {q} is {lca.val}")
    else:
        print(f"The lowest common ancestor of {p} and {q} is not found.")
    print("-" * 60)

    # Sum of root-to-leaf 
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
          tree.sum_root_to_leaf(rootsum))
    print("-" * 60)

    # Path weight 
    path_weight = BinaryTree()
    path_weight_order = [5,3,8,2,4,7,11,1,13]

    for i in path_weight_order:
        path_weight.insert(i)

    target_weight = 20
    current_value = 0

    if tree.has_path_weight(path_weight.root, target_weight, current_value):
        print(f"There exists a leaf whose path weight equals {target_weight}.")
    else:
        print(f"No leaf path weight equals {target_weight}.")
    print("-" * 60)    

    # Inorder traversal without recursion
    tree_order = BinaryTree()

    values = [8, 6, 10, 4, 7, 9, 13, 5, 12, 14]
    for val in values:
        tree_order.insert(val)

    k = 7
    inorder_traversal = tree_order.inorder_traversal(k)
    print("The inorder traversal of the binary tree:", inorder_traversal)
    print("-" * 60)

    # Preorder traversal without recursion
    preorder_traversal = tree_order.preorder_traversal()

    print("The preorder traversal of the binary tree:", preorder_traversal)
    print("-" * 60)
    
    # Successor of a root
    node = tree_order.find_value(10)
    if node:
        print(f"node found: {node.val}")
        successor = tree_order.compute_successor(node)

        if successor:
            print(f"Successor of {node.val} is: {successor.val}")
        else:
            print(f"No successor for {node.val}")
    else:
        print("Node is not found in the tree.")
    print("-" * 60)

    # Inorder traversal with O(1) space
    print("The inorder traversal of the binary tree: ",end="")
    tree_order.inorder_traversal_with_constant_space()
    print()
    print("-" * 60)

    # Building a binary tree
    inorder = [4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
    preorder = [8, 6, 4, 5, 7, 10, 9, 13, 12, 14]

    root_order = tree.build_tree(preorder, inorder)
    k = 3
    print("Inorder traversal of the reconstructed tree:")
    inorder_traversal_tree = []
    tree.recursive_inorder_traversal(root_order, inorder_traversal_tree)
    print(inorder_traversal_tree)

    print("Preorder traversal of the reconstructed tree:")
    preorder_traversal_tree = []
    tree.recursive_preorder_traversal(root_order, preorder_traversal_tree)
    print(preorder_traversal_tree, end="\n")
    print("-" * 60)

    # Reconstructing preorder traversal
    tree_order.reconstruct_preorder()
    print()
    print("-" * 60)

    # List from leaves
    leaflist = tree_order.create_list_from_leaves()
    print("Linked list of leaves: ", end=" ")
    tree_order.print_linked_list(leaflist)
    print()
    print("-" * 60)
    
    # exterior of a tree
    exterior = BinaryTree()
    root_exterior = [8,4,13,2,5,11,16,1,3,7,12,14,18,6]
    for i in root_exterior:
        exterior.insert(i)
    exterior.exterior_of_binary_tree()
    print()
    print("-" * 60)

    # Right sibling tree
    sibling = BinaryTree()
    right_sibling = [8,4,13,2,6,10,16,1,3,5,7,9,11,14,18]
    for values in right_sibling:
        sibling.insert(values)
    
    sibling.right_sibling_tree()
    sibling.print_level_next()
    print("-" * 60)

    # Locking nodes
    locked = BinaryTree()
    root_lock = [4,2,6,1,3,5,7]

    for values in root_lock:
        locked.insert(values)
    
    lock_node1 = locked.find_value(1)
    lock_node3 = locked.find_value(3)
    lock_node2 = locked.find_value(2)

    print(f"Locking node 1: {'Success' if locked.lock(lock_node1) else 'Failed'}")
    print(f"Locking node 3: {'Success' if locked.lock(lock_node3) else 'Failed'}")
    print(f"Locking node 2 (parent of 1 and 3): {'Success' if locked.lock(lock_node2) else 'Failed'}")
    print(f"Unlocking node 3: {'Success' if locked.unlock(lock_node3) else 'Failed'}")
    print(f"Locking node 2 after unlocking node 3: {'Success' if locked.lock(lock_node2) else 'Failed'}")
    print(f"Unlocking node 1: {'Success' if locked.unlock(lock_node1) else 'Failed'}")
    print(f"Locking node 2 after unlocking node 1: {'Success' if locked.lock(lock_node2) else 'Failed'}")
    print("-" * 60)

    # BST property
    bst = BinaryTree()
    root_bst = [8, 4, 12, 2, 6, 10, 14]

    for value in root_bst:
        bst.insert(value)

    if bst.is_bst():
        print("The tree satisfies the BST property.")
    else:
        print("The tree does NOT satisfy the BST property.")
    print("-" * 60)

    # First greater node
    input_key = 13
    first_key = bst.first_key_greater(input_key)

    if first_key != -1:
        print(f"The first key greater than {input_key} is {first_key}.")
    else:
        print(f"No key greater than {input_key} found.")
    print("-" * 60)

    # Largest elements
    number_of_largest_items = 3
    tree_order.largest_elements(number_of_largest_items)
    print()
    print("-" * 60)

    # Level order tree traversal
    tree_order.level_order_traversal()
    print("-" * 60)

    # Lower and upper bounds in binary search
    nums  = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
    target_value = 4
    bounds = tree.first_and_last_occurence(nums, target_value)
    print("Lower bound:", bounds[0])
    print("Upper bound:", bounds[1])
    print("-" * 60)