# Given n and k, return the kth permutation sequence.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        ans = ''
        k -= 1
        n -= 1
        #k는 현재까지 만들어진 ans 이후에 더 추가해야 할 경우의 수를 나타냄
        while k > 0:
            kinds = math.factorial(n)
            idx = k // kinds
            pop = nums.pop(idx) # nums에서 해당 idx에 있는 원소 추출 후 ans에 추가
            ans += str(pop)
            #update k and n
            k = k % kinds
            n = n - 1
        #더 추가해야 할 경우의 수가 없다면, nums에서 남은 원소 하나를 더함.
        ans += ''.join(map(str,nums))
        return ans
