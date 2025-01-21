class PostingListNode:
    def __init__(self):
        self.order = -1
        self.next = None
        self.jump = None

class Stacks:
    def __init__(self):
        self.mainstack = []
        self.maxstack = []
        self.wellformed = []
        self.stackpath = []
        self.sunsetview = []

    # Push a value onto the stack.
    def push(self, value):
        self.mainstack.append(value)

        if not self.maxstack or value >= self.mainstack[-1]:
            self.maxstack.append(value)
        else:
            self.maxstack.append(self.maxstack[-1])

    # Pop the top value from the stack.
    def pop(self):
        if not self.mainstack:
            raise IndexError("Stack is empty.")

        self.mainstack.pop()
        self.maxstack.pop()

    # Returns the maximum value in the stock.
    def max(self):
        if not self.maxstack:
            raise IndexError("Stack is empty.")
        
        return self.maxstack[-1]
    
    # Checks strings if they are well-formed.
    def isWellFormed(self, s):
        bracket_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in "({[":
                self.wellformed.append(ch)
            elif ch in ")}]":
                if not self.wellformed or self.wellformed[-1] != bracket_pairs[ch]:
                    return False
                
                self.wellformed.pop()
        
        return not self.wellformed

    # Simplifies the given paths.
    def simplifyPath(self, path):
        self.stackpath.clear()
        tokens = path.split('/')

        for token in tokens:
            if token == "." or not token:
                continue
            elif token == "..":
                if self.stackpath:
                    self.stackpath.pop()
            else:
                self.stackpath.append(token)
        
        simplified_path = "/" + "/".join(self.stackpath)

        return simplified_path
    
    # Recursive solution for setting jump order.
    @staticmethod
    def setJumpOrderRecursive(node, order):
        if not node or node.order != -1:
            return
        
        node.order = order[0]
        order[0] += 1
        
        Stacks.setJumpOrderRecursive(node.jump, order)
        Stacks.setJumpOrderRecursive(node.next, order)

    # Iterative solution for setting jump order.
    @staticmethod
    def setJumpOrderIterative(head):
        if not head:
            return
        
        stackorder = [head]
        order = 0

        while stackorder:
            node = stackorder.pop()

            if node and node.order == -1:
                node.order = order
                order += 1
                
                if node.next:
                    stackorder.append(node.next)
                if node.jump:
                    stackorder.append(node.jump)
    
    # Prints the postings list with orders.
    @staticmethod
    def printPostingList(head):
        node = head
        while node:
            print(f"Node Order: {node.order}")
            node = node.next

    # Finds the windows that have a sunset view.
    def findBuildingsWithSunsetView(self, buildings):
        for i in range(len(buildings) - 1, -1, -1):
            while self.sunsetview and buildings[self.sunsetview[-1]] <= buildings[i]:
                self.sunsetview.pop()

            self.sunsetview.append(i)

        result = []

        while self.sunsetview:
            result.append(self.sunsetview.pop())

        return result