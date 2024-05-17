def QuickSort(array, start, end):
    if start >= end:
        return
    
    pivot_index = start
    pivot = array[pivot_index]
    left = start + 1
    right = end
    
    while left <= right:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
            print(array)
    
    array[start], array[right] = array[right], array[start]
    print(array)
    
    QuickSort(array, start, right - 1)
    QuickSort(array, right + 1, end)

array = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print(f"Initial array: {array}")

QuickSort(array, 0, len(array) - 1)

print(f"Sorted array: {array}")