from sorting import Sorting
from sorting import Event


if __name__ == "__main__":
    # Merge arrays.
    sort = Sorting()
    A = [1, 3, 5, 0, 0, 0]
    B = [2, 4, 6]
    m = n = 3
    sort.merge_sorted_arrays(A, m, B, n)

    for i in range(0, m + n):
        print(A[i], end=" ")
    print("\n--------------------------------------------------------------")
    
    # Anagrams next to each other.
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sort.group_anagrams(strs)

    for str in strs:
        print(str, end=" ")
    print("\n--------------------------------------------------------------")

    # Searching in an unsorted list.
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    target = 3

    result = sort.find_in_rotated_array(arr, target)

    if result != -1:
        print(f"Element {target} found at index: {result}")
    else:
        print(f"Element {target} not found in the array.")
    print("--------------------------------------------------------------")

    # Searching in a sorted list.
    sorts = Sorting([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    x = 9

    index = sorts.find_element(x)

    if index != -1:
        print(f"Element {x} found at index: {index}")
    else:
        print(f"Element {x} not found in the array.")
    print("--------------------------------------------------------------")

    # Sorting by heap sort.
    data = [
        "zebra", "apple", "orange", "mango", "banana",
        "kiwi", "grape", "pear", "peach", "strawberry",
        "cherry", "blueberry", "plum", "raspberry", "lemon",
        "lime", "watermelon", "blackberry", "pineapple", "coconut"]
    
    chunk_size = 5

    chunks = sort.split_into_chunks(data, chunk_size)
    sorted_data = sort.merge_chunks(chunks)
    print("Sorted data:\n", sorted_data)
    print("--------------------------------------------------------------")

    # Max number of concurrent events.
    events = [(1, 3), (2, 4), (5, 8), (6, 7), (8, 9), (14, 17), (4, 6), (1, 5), (13, 15)]

    event_objects = [Event(start, end) for start, end in events]
    result_of_events = sort.max_concurrent_events(event_objects)

    print(f"Maximum number of concurrent events: {result_of_events}")
    print("--------------------------------------------------------------")

    # Union of intervals.
    intervals = [
        Event(0, 3), Event(1, 1), Event(2, 4), Event(3, 4), Event(5, 7), Event(7, 8), Event(8, 11), 
        Event(9, 11), Event(12, 14), Event(12, 16), Event(12, 14), Event(13, 15), Event(16, 17)]

    unions = sort.compute_union(intervals)
    print(f"Union of intervals: ")
    for interval in unions:
        print(f"({interval.start}, {interval.end})", end=" ")
    print("\n--------------------------------------------------------------")
