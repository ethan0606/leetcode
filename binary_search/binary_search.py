def get(arr, target):
    if not arr:
        return -1
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return -1


a = [1, 3, 4, 5, 6, 7]


print(a[get(a, 9)])

# 二分就是查看左右边界，然后进行缩放

