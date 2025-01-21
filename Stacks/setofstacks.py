class SetofStacks:
    # Constuctor.
    def __init__(self, capacity = 0):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        
        self.capacity = capacity
        self.stacks = []

    # Push an element onto the stack.
    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    # Pop an element from the stack.
    def pop(self):
        if not self.stacks:
            raise IndexError("Set of stacks is empty.")
        
        value = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return value
    
    # Pop an element from a specific stack.
    def pop_at(self, index):
        if index < 0 or index >= len(self.stacks):
            raise IndexError("Invalid stack index.")
        
        if not self.stacks[index]:
            raise IndexError("Specified stack is empty.")
        value = self.stacks[index].pop()
        
        if not self.stacks[index] and index == len(self.stacks) -1:
            self.stacks.pop()
        return value
    
    # Check if the set of stacks is empty.
    def is_empty(self):
        return not self.stacks
    
    # Print all stacks for debugging purposes.
    def print_stacks(self):
        for i, stack in enumerate(self.stacks):
            print(f"Stack {i+1}: {stack}")

    
    @staticmethod
    # Sorts the stack smallest to highest value.
    def sort_stack(stack):
        temp_stack = []

        while stack:
            current = stack.pop()
            while temp_stack and temp_stack[-1] > current:
                stack.append(temp_stack.pop())
            temp_stack.append(current)

        while temp_stack:
            stack.append(temp_stack.pop())

if __name__ == "__main__":
    try:
        stacks = SetofStacks(3)

        # Push elements.
        stacks.push(1)
        stacks.push(2)
        stacks.push(3)
        stacks.push(4)
        stacks.push(5)
        stacks.push(6)

        print("Initial stacks:")
        stacks.print_stacks()

        # Pop an element.
        print(f"Popped: {stacks.pop()}")

        print("Stacks after pop:")
        stacks.print_stacks()

        # Pop an element from a specific stack.
        print(f"Popped from stack 1: {stacks.pop_at(0)}")

        print("Stacks after popAt(0):")
        stacks.print_stacks()

    except Exception as e:
        print(f"Error: {e}")

    print("---------------------------------------------------")

    # Sorting a stack.
    s = [34, 3, 31, 98, 92, 23]
    print("Original Stack:", s)

    SetofStacks.sort_stack(s)

    print("Sorted Stack:", s)