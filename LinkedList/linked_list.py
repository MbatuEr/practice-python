from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def _del_(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node
    
    # Append a new node to the end of the list.
    def append(self,data):
        if not self.head:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)

    # Print the list.
    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    # Find kth to last element.
    def find_kth_to_last(self, k):
        if not self.head:
            raise ValueError("List is empty")
        
        first = self.head
        second = self.head

        for i in range(k):
            if not first:
                raise ValueError("k is larger than the list size")
            first = first.next
        
        while first:
            first = first.next
            second =second.next
        
        return second.data

    # Delete middle node.
    def delete_middle_node(self):
        if not self.head or not self.head.next:
            print("List is too short to have a middle node")
            return
        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = slow.next
            del slow

    # Partition.
    def partition(self,x):
        if not self.head and not self.head.next:
            return
        
        less_head = Node(0)
        greater_head = Node(0)
        less = less_head
        greater = greater_head
        current = self.head

        while current:
            if current.data < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        greater.next = None
        less.next = greater_head.next
        self.head = less_head.next
        del less_head
        del greater_head

    # Reverse the list.
    def reverse(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    # Add numbers in reverse order.
    def add_reverse_order(self, l1, l2):
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

    # Add numbers in forward order.
    def add_numbers_forward(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        reversed_result = self.add_reverse_order(l1, l2)
        reversed_result.head = self.reverse(reversed_result.head)

        return reversed_result
        
    # Remove duplicates.
    def remove_duplicates(self):
        if not self.head:
            return
        
        seen = set()
        current = self.head
        prev = None

        while current:
            if current.data in seen:
                prev.next = current.next
                del current
            else:
                seen.add(current.data)
                prev = current
            current = prev.next 

    # check if the list is a palindrome.
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True # Empty or single element list is a palindrome

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse(slow)
        first_half = self.head

        is_palindrome = True

        while second_half:
            if first_half.data != second_half.data:
                is_palindrome = False
                break
            first_half = first_half.next
            second_half = second_half.next

        return is_palindrome    

    # to get the length of the list.
    def get_length(self, head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    # Find the intersection of two lists.
    def first_intersection(self, head1, head2):
        if not head1 or not head2:
            return None

        len1 = self.get_length(head1)
        len2 = self.get_length(head2)

        longer = head1 if len1 > len2 else head2
        shorter = head2 if len1 > len2 else head1

        length_diff = abs(len1 - len2)

        for _ in range(length_diff):
            longer = longer.next

        while longer and shorter:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next

        return None
    
    # Detect loop in the list if any.
    def detect_loop(self, head):
        if not head or not head.next:
            return None
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            
        if not fast or not fast.next:           # If no loop was found, return None
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next   
        
        return slow