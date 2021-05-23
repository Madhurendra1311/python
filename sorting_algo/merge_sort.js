function processData(arr) {
    var sort = MergeSort (arr)
    console.log(sort.join(" "))
}

function MergeSort(arr){
  let len= arr.length;                  
  if (len == 1) {
    return arr
  }
    let middle = Math.floor(len/2)
  
    let left = arr.slice(0, middle)   
    let right = arr.slice(middle,arr.length)
    MergeSort(left)
    MergeSort(right)
    return  merge(arr,left,right)
}

function merge(arr,left,right){
    let i = 0
    let j = 0
    let k = 0
    while(i< left.length && j< right.length){
        if (left[i] <right[j]){
            arr[k] = left[i]
            i++
            k++
        }else{
            arr[k] = right[j] 
            j++
            k++
        }
    }
    while(i<left.length){
        arr[k] = left[i]
        i++
        k++
     }
    while(j<right.length){
        arr[k] = right[j] 
        j++
        k++
    }
    return arr
}

let res = processData([2, 5, 8, 1, 4])
console.log(res)
