# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #change input list into deque
        digits = collections.deque(digits)
        digits[-1] += 1
        #from last digits, if digit == 10, change it into 0 and add 1 to preceding digit.
        for i in reversed(range(len(digits))):
            if digits[i] == 10 and i > 0:
                digits[i] = 0
                digits[i-1] += 1
            elif i == 0 and digits[0] == 10:
                digits[i] = 0
                digits.appendleft(1)
        return list(digits)
