# solution 1. Time limit exceeded(complexity of O(n**3))
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums)-3):
            for j in range(i+3, len(nums)):
                l = i+1
                r = j-1
                sum = nums[i] + nums[l] + nums[r] + nums[j]
                while l < r:
                    if sum < target:
                        l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[l], nums[r], nums[j]])
                        while nums[l] == nums[l+1] and l < r:
                            l += 1
                        while nums[r] == nums[r-1] and l < r:
                            r -= 1
        return ans
      
# solution 2.
