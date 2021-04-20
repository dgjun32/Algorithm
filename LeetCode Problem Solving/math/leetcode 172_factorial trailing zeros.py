# Given an integer n, return the number of trailing zeroes in n!.

# 1. Recursive Solution
## 1 ~ n 까지의 모든 수에 5라는 인수가 몇개인지 세어보면 됨(as trailing zeros are created by product of 2*5, and there are much more 2 than 5)
### 1st recursive : 5라는 인수를 가진 원소를 셈
### 2nd recursive : 25라는 인수를 가진 원소를 셈
### 3rd recursive : 125라는 인수를 가진 원소를 셈
.
.
.
# 각각 구해진 원소의 개수를 모두 더함.
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = n // 5
        return ans + self.trailingZeroes(ans) if ans >= 5 else ans
