class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = target + sys.maxsize
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return sum
                    break
                elif abs(target - sum) < abs(target - closest):
                    closest = sum
                
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
        return closest
