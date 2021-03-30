class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        for left in range(len(height)-1):
            for right in range(left+1, len(height)):
                h = min(height[left], height[right])
                amt = h * (right - left)
                if amt > maximum:
                    maximum = amt
        return maximum
 #time limit exceeded 
