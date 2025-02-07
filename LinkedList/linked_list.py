from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Appends a new node to the end of the list."""
        if not self.head:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = Node(data)

    def print_list(self):
        """Prints the nodes in the list."""
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    def find_kth_to_last(self, key):
        """Finds the k-th to last element."""
        if not self.head:
            raise ValueError("List is empty!")
        
        first = second = self.head
        
        for i in range(key - 1):
            if not first:
                raise ValueError("k is larger than the list size.")
            first = first.next
        
        while first:
            first, second = first.next, second.next
        
        return second.data if second else None
        
    def delete_middle_node(self):
        """Deletes the middle node of the list."""
        if not self.head or not self.head.next: 
            print("The list is too short to have a middle node.")

        fast = slow = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        if prev:
            prev.next = slow.next
        
    def partition(self, value):
        """Reaaranges the list according to a pivot value."""
        if not self.head or not self.head.next: return

        less_head = less = Node(0)
        equal_head = equal = Node(0)
        greater_head = greater = Node(0)
        
        current = self.head
        
        while current:
            if current.data < value:
                less.next = current
                less = less.next
            elif current.data == value:
                equal.next = current
                equal = equal.next
            else:
                greater.next = current
                greater = greater.next

            current = current.next
        
        greater.next = None
        equal.next = greater_head.next
        less.next = equal_head.next or greater_head.next
        self.head = less_head.next

    def reverse(self, head):
        """Rearranges the list by reversing it."""
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev

    def add_reverse_order(self, l1, l2):
        """Adds numbers in the list in reverse order."""
        result = LinkedList()
        carry = 0

        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.data
                l1 = l1.next
            if l2:
                sum += l2.data
                l2 = l2.next
            result.append(sum % 10)
            carry = sum // 10

        result.head = self.reverse(result.head)
        return result        
    
    def add_forward_order(self, l1, l2):
        """Adds the numbers in the list in forward order."""
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        reversed_result = self.add_reverse_order(l1, l2)
        reversed_result.head = self.reverse(reversed_result.head)

        return reversed_result

    def remove_duplicates(self):
        """Removes duplicates from the list."""
        if not self.head: return

        uniques = set()
        prev = None
        current = self.head

        while current:
            if current.data in uniques:
                prev.next = current.next
            else:
                uniques.add(current.data)
                prev = current
            
            current = prev.next
        
    def is_palindrome(self):
        """Checks if the list is palindrome."""
        if not self.head: return 

        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse(slow)
        first_half = self.head

        while second_half:
            if first_half.data != second_half.data:
                return False

            first_half = first_half.next
            second_half = second_half.next
        
        return True
    
    def get_length(self, head):
        """Returns the length of a list."""
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        return length

    def first_intersection(self, l1, l2):
        """Finds a interaction between two list if it exists."""
        len1 = self.get_length(l1)
        len2 = self.get_length(l2)

        longer, shorter = (l1, l2) if len1 > len2 else (l2, l1)
        
        length_diff = abs(len1 - len2)

        for i in range(length_diff):
            longer = longer.next

        while shorter and longer:
            if longer.data == shorter.data:
                return longer
            
            shorter = shorter.next
            longer = longer.next

        return None  

    def detect_loop(self, head):
        """Detects loop in the list if any"""
        slow = fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            
        if not fast or not fast.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow