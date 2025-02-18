from typing import List
import sys

class SetOfStacks:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        
        self.capacity = capacity
        self.stacks: List[List[int]] = []

    def push(self, value: int) -> None:
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self) -> int:
        if not self.stacks:
            raise IndexError("Set of stacks is empty.")
        
        value = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return value

    def pop_at(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks):
            raise IndexError("Invalid stack index.")
        
        if not self.stacks[index]:
            raise IndexError("Specified stack is empty.")
        value = self.stacks[index].pop()
        
        if not self.stacks[index] and index == len(self.stacks) -1:
            self.stacks.pop()
        return value
    
    def is_empty(self) -> bool:
        return not self.stacks
    
    def __str__(self) -> str:
        """Returns a string representation of all stacks."""
        return "\n".join(f"Stack {i+1}: {stack}" for i, stack in enumerate(self.stacks))

    @staticmethod
    def sort_stack(stack: List[int]) -> None:
        """Sorts a stack in ascending order using an auxiliary stack."""
        temp_stack: List[int] = []

        while stack:
            current = stack.pop()
            while temp_stack and temp_stack[-1] > current:
                stack.append(temp_stack.pop())
            temp_stack.append(current)

        while temp_stack:
            stack.append(temp_stack.pop())

if __name__ == "__main__":
    try:
        stacks = SetOfStacks(3)

        # Push elements
        for num in [1, 2, 3, 4, 5, 6]:
            stacks.push(num)

        print("Initial stacks:")
        print(stacks)

        # Pop an element
        print(f"\nPopped: {stacks.pop()}")

        print("\nStacks after pop:")
        print(stacks)

        # Pop an element from a specific stack
        print(f"\nPopped from stack 1: {stacks.pop_at(0)}")

        print("\nStacks after pop_at(0):")
        print(stacks)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    print("-" * 40)

    # Sorting a stack
    s = [34, 3, 31, 98, 92, 23]
    print("Original Stack:", s)

    SetOfStacks.sort_stack(s)

    print("Sorted Stack:", s)