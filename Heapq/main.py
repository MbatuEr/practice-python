from Heaps import Heapq
from Heaps import Element

if __name__ == "__main__":
    # Merging arrays
    merger = Heapq()
    sequences = [
        [3, 5, 7],
        [0, 6],
        [0, 6, 28]
    ]
    merged_sequence = merger.merge_sorted_arrays(sequences)
    print("Merged Sorted Sequence:", merged_sequence)
    print("-----------------------------------------------------------")

    # Sorting an increasing-decreasing array
    sorted_queues = Heapq()
    arr = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    sorted_array = sorted_queues.sort_increasing_decreasing_array(arr)
    print("Sorted Array:", sorted_array)
    print("-----------------------------------------------------------")