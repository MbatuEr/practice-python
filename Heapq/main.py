from Heaps import Heapq
from Heaps import Star

if __name__ == "__main__":
    # Merging arrays
    pq = Heapq()
    sequences = [
        [3, 5, 7],
        [0, 6],
        [0, 6, 28]
    ]
    merged_sequence = pq.merge_sorted_arrays(sequences)
    print("Merged Sorted Sequence:", merged_sequence)
    print("-" * 60)

    # Increasing-decreasing array
    arr = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    sorted_array = pq.sort_increasing_decreasing_array(arr)
    print("Sorted Array:", sorted_array)
    print("-" * 60)

    # An almost sorted array 
    k_sorted_arr = [3, -1, 2, 6, 4, 5, 8]
    k = 2
    sorted_arr = pq.sort_almost_sorted_array(k_sorted_arr, k)

    print("Sorted array: ", end= " ")
    for num in sorted_arr:
        print(num, end=" ")
    print()
    print("-" * 60)

    # Closest stars
    stars = [
        Star(1, 2, 3),
        Star(5, 5, 5),
        Star(0, 2, 1),
        Star(3, 3, 3),
        Star(0.5, 0.5, 1),
        Star(2, 0.5, 1.5),
        Star(3, 1, 4)
    ]

    closest_stars = pq.find_k_closest_stars(stars, 3)
    print(closest_stars)
    print("-" * 60)

    # Find median
    sequence = [1, 0, 3, 5, 2, 0, 1]
    median = pq.online_median(sequence)
    print(median, end=" ")
    print()
    print("-" * 60)
    
    # Max elements
    x = 3
    max_values = [16, 60, 73, 45, 52, 30, 81]

    values = pq.find_k_largest_elements(max_values, x)
    print(f"Highest {x} values are:", *values)
    print("-" * 60)

    # Most frequent word
    input_str = ["go", "coding" , "byte", "byte", "go", "interview", "go"]
    k = 2
    result = pq.most_frequent_strings(input_str, k)
    print(result, end=" ")
    print()
    print("-" * 60)

    # Combine linked list
    list1 = pq.create_linked_list([1, 4, 5])
    list2 = pq.create_linked_list([1, 3, 4])
    list3 = pq.create_linked_list([2, 6])

    lists = [list1, list2, list3]
    merged_head = pq.combine_sorted_linked_lists(lists)
    print(merged_head) 
    print("-" * 60)