from typing import List
from collections import deque

class PostingListNode:
    def __init__(self):
        self.order = -1
        self.next = None
        self.jump = None

class Stacks:
    def __init__(self):
        self._main_stack: List[int] = []
        self._max_stack: List[int] = []

    def push(self, value: int) -> None:
        self._main_stack.append(value)
        max_value = max(value, self._max_stack[-1] if self._max_stack else value)
        self._max_stack.append(max_value)

    def pop(self) -> None:
        if not self._main_stack:
            raise IndexError("Stack is empty.")

        self._max_stack.pop()
        self._main_stack.pop()

    def max(self) -> int:
        if not self._max_stack:
            raise IndexError("Stack is empty.")
        
        return self._max_stack[-1]
    
    @staticmethod
    def is_well_formed(s: str) -> bool:
        stack = deque()
        bracket_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]":
                if not stack or stack[-1] != bracket_pairs[ch]:
                    return False
                
                stack.pop()
        
        return not stack
 
    @staticmethod
    def simplify_path(path: str) -> str:
        stack = deque()

        for token in path.split('/'):
            if token == "." or not token:
                continue
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
    
        return "/" + "/".join(stack)
    
    @staticmethod
    def set_jump_order_recursive(node: PostingListNode, order: List[int]) -> None:
        if not node or node.order != -1:
            return
        
        node.order = order[0]
        order[0] += 1
        
        Stacks.set_jump_order_recursive(node.jump, order)
        Stacks.set_jump_order_recursive(node.next, order)

    @staticmethod
    def set_jump_order_iterative(head: PostingListNode) -> None:
        if not head:
            return
        
        stack_order = [head]
        order = 0

        while stack_order:
            node = stack_order.pop()
            if node and node.order == -1:
                node.order = order
                order += 1
                if node.next:
                    stack_order.append(node.next)
                if node.jump:
                    stack_order.append(node.jump)
    
    @staticmethod
    def print_posting_list(head: PostingListNode) -> None:
        node = head
        while node:
            print(f"Node Order: {node.order}")
            node = node.next

    @staticmethod
    def find_buildings_with_sunset_view(buildings: List[int]) -> List[int]:
        stack = deque()
        for i in range(len(buildings) - 1, -1, -1):
            while stack and buildings[stack[-1]] <= buildings[i]:
                stack.pop()
            stack.append(i)

        return list(reversed(stack))