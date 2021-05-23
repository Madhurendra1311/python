def selection_sort(arr):
    for i in range(len(arr)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(arr)-1):
            # Update the min_index if the element at j is lower than it
            if arr[j] < arr[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [3, 1, 41, 59, 26, 53, 59]

selection_sort(arr)

# Let's see the list after we run the Selection Sort
print(arr)