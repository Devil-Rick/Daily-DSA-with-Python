"""
Merge Sort Algorithm using Recursion
"""


def merge(arr1, arr2, arr):
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr[k] = arr2[j]
            k += 1
            j += 1
            
    while i < len(arr1):
        arr[k] = arr1[i]
        k += 1
        i += 1
        
    while j < len(arr2):
        arr[k] = arr2[j]
        k += 1
        j += 1


def merge_Sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    
    mid = len(arr) // 2
    arr1 = arr[0:mid]
    arr2 = arr[mid:]
    
    merge_Sort(arr1)
    merge_Sort(arr2)

    merge(arr1, arr2, arr)

a = [2, 3, 1, 6, 7, 5, 3]
merge_Sort(a)

print(a)
