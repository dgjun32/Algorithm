class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if len(nums) == 0 -> target cannot be found
        if len(nums) == 0:
            return [-1, -1]
        else:
            l, r = 0, len(nums)-1
            found = False
            c = int(l/2+r/2)
            # binary search for target
            while l < r and found == False:
                if nums[c] < target:
                    l = c+1
                    c = int(l/2+r/2)
                elif nums[c] > target:
                    r = c-1
                    c = int(l/2+r/2)
                else:
                    found = True
            # while number different from target appears, expand left and right pointer
            if nums[c] != target: # if target is not found
                return [-1,-1]
            else:                 # if target is found
                l,r = c,c
                while l > 0 and nums[l-1] == nums[l]:
                    l -= 1
                while r < len(nums)-1 and nums[r+1] == nums[r]:
                    r += 1
                return [l,r]
