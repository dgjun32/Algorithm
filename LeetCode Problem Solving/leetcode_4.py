#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #concatenate two lists and sort them
        nums = nums1 + nums2
        nums.sort()
        
        #until the number of elements in list reduced to 2, pop first element and last element
        while len(nums) > 2:
            nums.pop()
            nums.pop(0)
        #if length is even number, return averaged value 
        if len(nums) == 2:
            return nums[0]/2 + nums[1]/2
        else:
            return nums[0]
