# (a) Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# (b) Binary Search (requires sorted array)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# (c) Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# (d) Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# (e) Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- Testing the Functions ---
sample_list = [64, 25, 12, 22, 11]

print("Original List:", sample_list)
print("Linear Search for 22 (Index):", linear_search(sample_list, 22))
print("Selection Sort:", selection_sort(sample_list.copy()))
print("Bubble Sort:", bubble_sort(sample_list.copy()))
print("Insertion Sort:", insertion_sort(sample_list.copy()))

sorted_list = insertion_sort(sample_list)
print("Binary Search for 25 in sorted list (Index):", binary_search(sorted_list, 25))