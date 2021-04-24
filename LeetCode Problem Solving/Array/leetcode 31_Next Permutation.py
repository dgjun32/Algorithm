class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        keep = True
        i = len(nums) - 2
        if len(nums) >= 2:
            while keep == True:
                if i < 0:
                    nums.sort()
                    keep = False
                elif nums[i:] == sorted(nums[i:], reverse = True):
                    i -= 1
                else:
                    a = nums[i] # current head
                    b = min([x for x in nums[i:] if x > a]) # next head
                    idx = nums[(i+1):].index(b)
                    nums[i+1+idx], nums[i] = a, b
                    nums[(i+1):] = sorted(nums[(i+1):])
                    keep = False
