# solve it in O(1) extra memory

def removeDuplicates(nums):
        idx = 1
        while idx < len(nums):
            if nums[idx-1] == nums[idx]:
                nums.pop(idx)
            else:
                idx += 1
        return nums
