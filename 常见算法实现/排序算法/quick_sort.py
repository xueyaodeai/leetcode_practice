# 快速排序
import random
from typing import List


def quickSort(arr: List, left: int, right: int) -> List:
    if left < right:
        partitionIndex = partition(arr, left, right)
        print(partitionIndex)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr


def partition(arr: List, left: int, right: int) -> int:
    key = random.randint(left, right)
    swap(arr, left, key)
    print("key: ", arr)
    i, j = left, right
    while i < j:
        while arr[j] >= arr[left] and i < j:
            j -= 1
        while arr[i] <= arr[left] and i < j:
            i += 1
        swap(arr, i, j)
        print("change: ", arr)
    swap(arr, left, i)
    print("finish: ", arr)
    return i


def swap(arr: List, i: int, j: int):
    if i == j:
        pass
    else:
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr = [5, 9, 1, 9, 5, 3, 7, 6, 1]
    print("result: ", quickSort(arr, 0, len(arr)-1))
    arr_1 = [0]
    print("result: ", quickSort(arr_1, 0, len(arr_1)-1))
    arr_2 = [1, 0]
    print("result: ", quickSort(arr_2, 0, len(arr_2)-1))

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
# result:  [1, 1, 3, 5, 5, 6, 7, 9, 9]
# result:  [0]
# change:  [1, 0]
# finish:  [0, 1]
# 1
# result:  [0, 1]
