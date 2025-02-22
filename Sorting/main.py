from sorting import Sorting
from sorting import Event
from sorting import Student
from sorting import Team

if __name__ == "__main__":
    # Merge arrays.
    sort = Sorting()
    A = [1, 3, 5, 0, 0, 0]
    B = [2, 4, 6]
    m = n = 3
    sort.merge_two_sorted_arrays(A, m, B, n)

    for i in range(0, m + n):
        print(A[i], end=" ")
    print()
    print("-" * 60)
    
    # Anagrams next to each other.
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sort.group_anagrams(strs)

    for str in strs:
        print(str, end=" ")
    print()
    print("-" * 60)

    # Searching in an unsorted list.
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    target = 3

    result = sort.find_in_rotated_array(arr, target)

    if result != -1:
        print(f"Element {target} found at index: {result}")
    else:
        print(f"Element {target} not found in the array.")
    print("-" * 60)

    # Searching in a sorted list.
    sorts = Sorting([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    x = 9

    index = sorts.find_element(x)

    if index != -1:
        print(f"Element {x} found at index: {index}")
    else:
        print(f"Element {x} not found in the array.")
    print("-" * 60)

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
    print("-" * 60)

    # Max number of concurrent events.
    events = [(1, 3), (2, 4), (5, 8), (6, 7), (8, 9), (14, 17), (4, 6), (1, 5), (13, 15)]

    event_objects = [Event(start, end) for start, end in events]
    result_of_events = sort.max_concurrent_events(event_objects)

    print(f"Maximum number of concurrent events: {result_of_events}")
    print("-" * 60)

    # Union of intervals.
    intervals = [
        Event(0, 3), Event(1, 1), Event(2, 4), Event(3, 4), Event(5, 7), Event(7, 8), Event(8, 11), 
        Event(9, 11), Event(12, 14), Event(12, 16), Event(12, 14), Event(13, 15), Event(16, 17)]

    unions = sort.compute_union(intervals)
    print(f"Union of intervals: ")
    for interval in unions:
        print(f"({interval.start}, {interval.end})", end=" ")
    print()
    print("-" * 60)

    # Sorting string & int pairs by integers.
    students = [
        Student("Alice", 20), Student("Bob", 22), Student("Charlie", 20),
        Student("David", 21), Student("Eve", 22), Student("Frank", 21)
    ]

    print("Input vector:")
    print(students)

    sort.sorting_students_by_age(students)

    print("After sorting by age:")
    print(students)
    print("-" * 60)

    # Sorting into two different arrays.
    fenerbahce = [
        Team("Livakovic", 190), Team("Kadioglu", 180), Team("Djiku", 188),
        Team("Becao", 194), Team("Osayi", 184), Team("Ismail", 183), Team("Fred", 173),
        Team("Kahveci", 180), Team("Szymanski", 174), Team("Tadic", 181), Team("Dzeko", 193)
    ]

    galatasaray = [
        Team("Muslera", 188), Team("Baris", 183), Team("Davinson", 192),
        Team("Nelsson", 187), Team("Boey", 181), Team("Torreira", 169), Team("Demirbay", 182),
        Team("Ziyech", 182), Team("Mertens", 170), Team("Akturkoglu", 179), Team("Icardi", 185)
    ]

    sort.team_photo(fenerbahce, galatasaray)
    print("-" * 60)

    # Perform quick sort.
    qvec = [10, 80, 30, 90, 40, 50, 70]
    sorting = Sorting(qvec)
    sorting.quick_sort()

    print("Sorted Array:", end=" ")
    sorting.print_values()
    print("-" * 60)

    # Perform bucket sort.
    bucket_arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

    print("Original array:", bucket_arr)
    sort.bucket_sort(bucket_arr)
    print("Sorted array:", bucket_arr)
    print("-" * 60)

    # Perform radix sort.
    radix_arr = [17012, 45345, 75234, 90714, 12802, 234, 23, 4466]

    print("Original array:", radix_arr)
    sort.radix_sort(radix_arr)
    print("Sorted array:", radix_arr)
    print("-" * 60)