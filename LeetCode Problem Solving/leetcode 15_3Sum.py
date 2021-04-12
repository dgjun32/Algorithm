# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

#1. solution using two pointer(complexity of O(n^2))
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            # if nums[i] == nums[i-1] -> duplicate must be passed
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # if temp sum < target -> move left pointer to right (increasing the sum)
                if sum < 0:
                    left += 1
                # elif temp sum < target -> move right pointer to left (decreasing the sum)
                elif sum > 0:
                    right -= 1
                # if temp sum == target -> append [nums[i], nums[left], nums[right]] to the answer list
                # and move left and right pointer until duplicate stops show up
                # if there are no duplicates, move left pointer and right pointer respectively.
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1
        return ans  
