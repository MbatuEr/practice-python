from linked_list import LinkedList
from node import Node

if __name__ == "__main__":
    list = LinkedList()
    arr = (3, 5, 8, 5, 8, 5, 3)
    for i in arr:
        list.append(i)

    # Find kth to last.
    print("\nOriginal list:")
    list.print_list()

    k = int(input("\nEnter k to find kth to last element: "))
    try:
        result = list.find_kth_to_last(k)
        print(f"\n{k}th to last element is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-------------------------------------------------")

    # Delete middle node.
    print("Deleting middle node...")
    list.delete_middle_node()
    print("\nList after deleting middle node:")
    list.print_list()
    print("-------------------------------------------------")    

    # Partition.
    print("Original list:")
    list.print_list()
    partition = int(input("\nEnter partition value: "))
    list.partition(partition)
    print("\nList after partition:")
    list.print_list()
    print("-------------------------------------------------")

    # Add numbers in reverse order.
    list1 = LinkedList()
    list1.append(3)
    list1.append(4)
    list1.append(3)

    list2 = LinkedList()
    list2.append(4)
    list2.append(6)
    list2.append(5)
    
    print("First lists:")
    list1.print_list()
    print("\nSecond list:")
    list2.print_list()
    result = list.add_reverse_order(list1.head, list2.head)
    print("\nThe sum of the two lists in reverse order is:")
    result.print_list()
    print("-------------------------------------------------")

    # Add numbers in forward order.
    result_forward = list.add_forward_order(list1.head, list2.head)
    print("The sum of the two lists in forward order is:")
    result_forward.print_list()
    print("-------------------------------------------------")

    # Remove duplicates.
    print("Original list:")
    list.print_list()

    list.remove_duplicates()
    print("\nList after removing duplicates:")
    list.print_list()
    print("-------------------------------------------------")

    # Check if list is palindrome.
    list_palindrome = LinkedList()
    list_palindrome.append(3)
    list_palindrome.append(5)
    list_palindrome.append(8)
    list_palindrome.append(5)
    list_palindrome.append(3)

    print("Is the list a Palindrome? " + ("Yes" if list_palindrome.is_palindrome() else "No"))
    print("-------------------------------------------------")

    # find the first intersection node.
    firstlist = Node(1)
    firstlist.next = Node(2)
    firstlist.next.next = Node(3)
    
    secondlist = Node(4)
    secondlist.next = firstlist.next.next

    interaction_node = LinkedList()
    intersection = interaction_node.first_intersection(firstlist, secondlist)
    
    
    if intersection:
        print(f"The first intersection node data is: {intersection.data}")
    else:
        print("No intersection found")
    print("-------------------------------------------------")

    # find the loop node.
    loop_node = Node(1)
    loop_node.next = Node(2)
    loop_node.next.next = Node(3)
    loop_node.next.next.next = Node(4)
    loop_node.next.next.next.next = Node(5)
    loop_node.next.next.next.next = loop_node.next.next

    loop = LinkedList()
    loop_start = loop.detect_loop(loop_node)

    if loop_start:
        print(f"The loop starts at node with data: {loop_start.data}")
    else:
        print("No loop detected") 
    print("-------------------------------------------------")