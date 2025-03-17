class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MultiLevelListNode:
    def __init__(self, val, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child