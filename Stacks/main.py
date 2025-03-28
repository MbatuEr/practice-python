from stacks import Stacks
from stacks import PostingListNode

if __name__ == "__main__":
    # Stack operations
    st = Stacks()
    for val in [3, 5, 2, 6, 7]:
        st.push(val)
    print("Current max:", st.max())
    st.pop()
    print("Current max after pop:", st.max())
    print("-" * 50)

    # Well-formed checker
    for test in ["([]){()}", "[()[]{()()}]", "{)", "[()[]{()()"]:
        print(f"{test}: {'Well Formed' if st.is_well_formed(test) else 'Not Well Formed'}")
    print("-" * 50)
    
    # Path simplification
    paths = ["/usr/bin/../bin/gcc", "scripts//./../scripts/awkscripts/././", "/a/./b/../../c/", "/../", "/home//foo/"]
    for path in paths:
        print(f"Simplified Path: {st.simplify_path(path)}")
    print("-" * 50)

    # Posting List processing
    nodes = [PostingListNode() for _ in range(5)]
    nodes[0].next, nodes[1].next, nodes[2].next, nodes[3].next = nodes[1], nodes[2], nodes[3], nodes[4]
    nodes[1].jump, nodes[2].jump, nodes[3].jump = nodes[3], nodes[2], nodes[4]
    
    print("Recursive Jump Order:")
    st.set_jump_order_recursive(nodes[0], [0])
    st.print_posting_list(nodes[0])
    print()
    print("Iterative Jump Order:")
    st.set_jump_order_iterative(nodes[0])
    st.print_posting_list(nodes[0])
    print("-" * 50)

    # Sunset view
    buildings = [7, 4, 8, 2, 9]
    print("Buildings with sunset views:", [buildings[i] for i in st.find_buildings_with_sunset_view(buildings)])
    print("-" * 50)

    # Next larger number
    nums = [5, 2, 4, 6, 1]
    res = st.next_larger_number_to_the_right(nums)
    print("Next larger number:", res)
    print("-" * 50)

    # Evaulating mathematical expression
    s = "18 -(7 + (2 - 4))"
    result = st.evaluate_expression(s)
    print(f"The result is: {result}")
    print("-" * 50)