def quickSort(arr, start,end):
    if(start < end):
        index = partition(arr, start,end)
        quickSort(arr, start, index-1)
        quickSort(arr, index+1, end)
    
    return arr


def partition(arr,start, end):
    i = start
    j = end
    piv = arr[end]

    while(i<j):
        while (arr[i] < piv and i<end):
            i = i + 1
        while(arr[j] >= piv and j >0):
            j = j - 1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[end] = arr[end], arr[i]
    return i

arr = [8, 7, 2, 1, 0, 9, 6]

size = len(arr) - 1

quickSort(arr, 0, size)

print('Sorted Array in Ascending Order:')
print(arr)