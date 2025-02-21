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
    print("-----------------------------------------------------------")

    # Sorting an increasing-decreasing array
    arr = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    sorted_array = pq.sort_increasing_decreasing_array(arr)
    print("Sorted Array:", sorted_array)
    print("-----------------------------------------------------------")

    # Sorting an array which is k away at most.
    k_sorted_arr = [3, -1, 2, 6, 4, 5, 8]
    k = 2
    sorted_arr = pq.sort_k_sorted_array(k_sorted_arr, k)

    print("Sorted array: ", end= " ")
    for num in sorted_arr:
        print(num, end=" ")
    print("\n-----------------------------------------------------------")

    # Closest stars.
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
    print("-----------------------------------------------------------")

    # Calculating median at each step.
    sequence = [1, 0, 3, 5, 2, 0, 1]
    median = pq.online_median(sequence)
    print(median, end=" ")
    print("\n-----------------------------------------------------------")
    
    # Max elements
    x = 3
    max_values = [16, 60, 73, 45, 52, 30, 81]

    values = pq.find_k_largest_elements(max_values, x)
    print(f"Highest {x} values are:", *values)
    print("-----------------------------------------------------------")

    # Most frequent word
    input_str = ["go", "coding" , "byte", " byte", " go", "interview", "go"]
    k = 2
    result = pq.most_frequent_strings(input_str, k)
    print(result, end=" ")
    print()