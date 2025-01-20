from setofstacks import SetofStacks

if __name__ == "__main__":
    try:
        stacks = SetofStacks(3)

        # Push elements
        stacks.push(1)
        stacks.push(2)
        stacks.push(3)
        stacks.push(4)
        stacks.push(5)
        stacks.push(6)

        print("Initial stacks:")
        stacks.print_stacks()

        # Pop an element
        print(f"Popped: {stacks.pop()}")

        print("Stacks after pop:")
        stacks.print_stacks()

        # Pop an element from a specific stack
        print(f"Popped from stack 1: {stacks.pop_at(0)}")

        print("Stacks after popAt(0):")
        stacks.print_stacks()

    except Exception as e:
        print(f"Error: {e}")

    print("---------------------------------------------------")

    # Sorting a stack
    s = [34, 3, 31, 98, 92, 23]
    print("Original Stack:", s)

    SetofStacks.sort_stack(s)

    print("Sorted Stack:", s)