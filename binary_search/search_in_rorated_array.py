arr = [3, 4, 5, 1, 2]

# 主要是判定左右顺序

def search(arr, target):
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif arr[mid] > arr[right]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search(arr, 4))

