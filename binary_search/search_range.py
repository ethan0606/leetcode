# 1, 2, 2, 2, 3


def left_get(arr, target):
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] >= target:
            right = mid - 1

    if left >= len(arr) or arr[left] != target:
        return -1
    return left


arr = [1, 2, 2, 2, 3]
print(left_get(arr, 1))
