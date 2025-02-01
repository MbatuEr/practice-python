class Heapq:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self.sift_up(self.get_size() - 1)

    def sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index] > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else: 
                break  
    
    def get_max(self):
        if self.is_empty():
            raise RuntimeError("Heap is empty!")
        return self.data[0]

    def get_size(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def extract_max(self):
        if self.is_empty():
            raise RuntimeError("Heap is empty!")
        
        max_value = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.sift_down(0)

        return max_value

    def sift_down(self, index):
        size = self.get_size()

        while index < size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index

            if left_child < size and self.data[left_child] > self.data[largest]:
                largest = left_child
            if right_child < size and self.data[right_child] > self.data[largest]:
                largest = right_child
            
            if largest != index:
                self.data[index], self.data[largest] = self.data[largest], self.data[index]
                index = largest
            else:
                break 
    
    def remove(self, index):
        if index < 0 or index > self.get_size():
            raise IndexError("Index is out of range!")

        self.data[index] = self.data[-1]
        self.data.pop()

        if index < self.get_size():
            self.sift_up(index)
            self.sift_down(index)

    def heapify(self, array):
        self.data = array[:]
        for i in range((self.get_size() // 2) - 1, -1, -1):
            self.sift_down(i)

    def heap_sort(self, array):
        self.heapify(array)

        for i in range(len(array) - 1, -1, -1):
            array[i] = self.extract_max()
        
        return array 
    

if __name__ == "__main__":
    heap = Heapq()

    # Insert elements
    heap.insert(10)
    heap.insert(20)
    heap.insert(15)
    heap.insert(30)

    print(f"Max element: {heap.get_max()}")

    # Extract the maximum element
    print(f"Extracted max: {heap.extract_max()}")

    # Remove an element
    heap.remove(1)
    print(f"Max element after removal: {heap.get_max()}")

    # Check if the heap is empty
    print(f"Is heap empty? {'Yes' if heap.is_empty() else 'No'}")

    # Heapify an array
    array = [5, 3, 8, 4, 2, 7, 1]
    heap.heapify(array)

    print("Heap after heapify: ", end="")
    while not heap.is_empty():
        print(heap.extract_max(), end=" ")
    print()

    # Heap sort
    unsorted = [9, 4, 7, 1, 3, 8, 5]
    sorted_array = heap.heap_sort(unsorted)

    print("Sorted array: ", end="")
    print(" ".join(map(str, sorted_array)))

