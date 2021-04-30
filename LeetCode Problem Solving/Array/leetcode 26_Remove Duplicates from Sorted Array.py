# solve it in O(1) extra memory
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i <= len(nums)-1:
            if nums[i-1] == nums[i]:
                del nums[i-1]
            else:
                i += 1
        return len(nums)
