function quickSort(arr, start,end){
    if(start < end){
        index = partition(arr, start,end)
        quickSort(arr, start, index-1)
        quickSort(arr, index+1, end)
    }
    return arr
}

function partition(arr,start, end){
    let i = start
    let j = end
    let piv = arr[end]
    while(i<j) {
        while(arr[i] < piv && i<end){
            i++
        }
         while(arr[j] >= piv && j >0){
            j--
        }
        if(i<j){
            arr[i], arr[j] = arr[j], arr[i]
        }
    }
    arr[i], arr[end] = arr[end], arr[i]
    return i
}


let arr = [8, 7, 2, 1, 0, 9, 6]

let size = arr.length - 1

quickSort(arr, 0, size)

console.log(arr)
