class SetofStacks:
    def __init__(self, capacity = 0):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            raise IndexError("Set of stacks is empty.")
        
        value = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return value
    
    def pop_at(self, index):
        if index < 0 or index >= len(self.stacks):
            raise IndexError("Invalid stack index.")
        
        if not self.stacks[index]:
            raise IndexError("Specified stack is empty.")
        value = self.stacks[index].pop()
        
        if not self.stacks[index] and index == len(self.stacks) -1:
            self.stacks.pop()
        return value
    
    def is_empty(self):
        return not self.stacks
    
    def print_stacks(self):
        for i, stack in enumerate(self.stacks):
            print(f"Stack {i+1}: {stack}")

    @staticmethod
    def sort_stack(stack):
        temp_stack = []

        while stack:
            current = stack.pop()
            while temp_stack and temp_stack[-1] > current:
                stack.append(temp_stack.pop())
            temp_stack.append(current)

        while temp_stack:
            stack.append(temp_stack.pop())

