# 快速排序
from typing import List


def quickSort(arr: List, left: int, right: int) -> List:
    if left < right:
        partitionIndex = partition(arr, left, right)
        print(partitionIndex)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr


def partition(arr: List, left: int, right: int) -> int:
    key = arr[left]
    i, j = left, right
    while i < j:
        while arr[j] >= key and i < j:
            j -= 1
        while arr[i] <= key and i < j:
            i += 1
        swap(arr, i, j)
        print("change: ", arr)
    swap(arr, left, i)
    print("finish: ", arr)
    return i


def swap(arr: List, left: int, right: int):
    if left == right:
        pass
    arr[left], arr[right] = arr[right], arr[left]


if __name__ == "__main__":
    arr = [5, 9, 1, 9, 5, 3, 7, 6, 1]
    print(quickSort(arr, 0, len(arr)-1))

# change:  [5, 1, 1, 9, 5, 3, 7, 6, 9]
# change:  [5, 1, 1, 3, 5, 9, 7, 6, 9]
# change:  [5, 1, 1, 3, 5, 9, 7, 6, 9]
# finish:  [3, 1, 1, 5, 5, 9, 7, 6, 9]
# 3
# change:  [3, 1, 1, 5, 5, 9, 7, 6, 9]
# finish:  [1, 1, 3, 5, 5, 9, 7, 6, 9]
# 2
# change:  [1, 1, 3, 5, 5, 9, 7, 6, 9]
# finish:  [1, 1, 3, 5, 5, 9, 7, 6, 9]
# 0
# change:  [1, 1, 3, 5, 5, 9, 7, 6, 9]
# finish:  [1, 1, 3, 5, 5, 9, 7, 6, 9]
# 4
# change:  [1, 1, 3, 5, 5, 9, 7, 6, 9]
# finish:  [1, 1, 3, 5, 5, 6, 7, 9, 9]
# 7
# change:  [1, 1, 3, 5, 5, 6, 7, 9, 9]
# finish:  [1, 1, 3, 5, 5, 6, 7, 9, 9]
# 5
# [1, 1, 3, 5, 5, 6, 7, 9, 9]
