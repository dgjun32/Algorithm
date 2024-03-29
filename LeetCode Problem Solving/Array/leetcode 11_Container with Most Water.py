# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

#1. Bruto Force Approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        #for all left / right index pairs which satisfy left < right, compute Area and update maximum value
        for left in range(len(height)-1):
            for right in range(left+1, len(height)):
                h = min(height[left], height[right])
                amt = h * (right - left)
                if amt > maximum:
                    maximum = amt
        return maximum
 #time limit exceeded(Intuitive but inefficient) 

#2. Solution Using Two Pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #setting left pointer at start of the list, right pointer at end of the list 
        maximum = 0
        left, right = 0, len(height)-1
        while left < right:
            amt = min(height[left], height[right]) * (right - left)
            #update maximum value
            if amt > maximum:
                maximum = amt
            #move each pointer
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1 
            else:
                left += 1
                right -= 1
        return maximum
