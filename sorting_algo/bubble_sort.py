def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp



arr = [10,20,15,50,35,45]
bubbleSort(arr)

print(arr)

# Time complexity = O(n^2)
# Space complexity = O(1)
