


def subsets(nums):
    res = list()
    def backtrack(nums, start, track):
        res.append(track[:]) # 浅拷贝
        for i in range(start, len(nums)):
            track.append(nums[i])
            backtrack(nums, i + 1, track)
            track.pop()
    track = list()
    backtrack(nums, 0, track)
    return res

res = subsets([2, 3, 4, 5])
print(res)



