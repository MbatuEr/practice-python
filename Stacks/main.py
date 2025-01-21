from stacks import Stacks
from stacks import PostingListNode

if __name__ == "__main__":
    # Max value in the stack.
    st = Stacks()

    st.push(3)
    st.push(5)
    st.push(2)
    st.push(7)
    st.push(6)

    print("Current max:", st.max())
    st.pop()
    print("Current max after pop:", st.max())
    st.pop()
    print("Current max after pop:", st.max())
    print("-------------------------------------------------------")

    # If the string well-formed.
    formed = Stacks()

    test1 = "([]){()}"
    test2 = "[()[]{()()}]"
    test3 = "{)"
    test4 = "[()[]{()()"

    print(f"Test 1: {'Well Formed' if formed.isWellFormed(test1) else 'Not Well Formed'}")
    print(f"Test 2: {'Well Formed' if formed.isWellFormed(test2) else 'Not Well Formed'}")
    print(f"Test 3: {'Well Formed' if formed.isWellFormed(test3) else 'Not Well Formed'}")
    print(f"Test 4: {'Well Formed' if formed.isWellFormed(test4) else 'Not Well Formed'}")
    print("-------------------------------------------------------")

    # Simplified path.
    simplified = Stacks() 

    path1 = "/usr/bin/../bin/gcc"
    path2 = "scripts//./../scripts/awkscripts/././"
    path3 = "/a/./b/../../c/"
    path4 = "/../"
    path5 = "/home//foo/"

    print(f"Simplified Path 1: {simplified.simplifyPath(path1)}")
    print(f"Simplified Path 2: {simplified.simplifyPath(path2)}")
    print(f"Simplified Path 3: {simplified.simplifyPath(path3)}")
    print(f"Simplified Path 4: {simplified.simplifyPath(path4)}")
    print(f"Simplified Path 5: {simplified.simplifyPath(path5)}")
    print("-------------------------------------------------------")

    # Posting List.
    L = PostingListNode()
    a = PostingListNode()
    b = PostingListNode()
    c = PostingListNode()
    d = PostingListNode()

    L.next = a 
    a.next = b 
    b.next = c 
    c.next = d
    a.jump = c 
    c.jump = b 
    b.jump = d 
    d.jump = None

    print("Recursive Method:")
    order = [0]
    Stacks.setJumpOrderRecursive(L, order)
    Stacks.printPostingList(L)
    L.order = a.order = b.order = c.order = d.order = -1

    print("\nIterative Method:")
    Stacks.setJumpOrderIterative(L)
    Stacks.printPostingList(L)
    print("-------------------------------------------------------")

    # Sunset view.
    view = Stacks()
    buildings = [7, 4, 8, 2, 9]
    
    result = view.findBuildingsWithSunsetView(buildings)

    print("Buildings with sunset views (heights):", [buildings[i] for i in result])
    print("-------------------------------------------------------")