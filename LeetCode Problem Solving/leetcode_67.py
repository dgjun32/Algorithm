# Given two binary strings a and b, return their sum as a binary string

#sol 1.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #transform binary string into demical number
        a = sum([pow(2,len(a)-i-1)*int(a[i]) for i in reversed(range(len(a)))])
        b = sum([pow(2,len(b)-i-1)*int(b[i]) for i in reversed(range(len(b)))])
        c = a+b
        #change demical number into binary string.
        ans = []
        if c == 0:
            return('0')
        else:
            while c != 0:
                ans.append(str(c%2))
                c = c//2
            return ''.join(ans[::-1])

#sol 2. Simple approach using bin function.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = bin(int(a,2) + int(b,2))
        return str(ans)[2:]
