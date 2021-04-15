# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# 1. My solution
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet_to_num = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
                     'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                     'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
                     'V':22,'W':23,'X':24,'Y':25,'Z':26}
        ans = ''
        i = 1
        while columnNumber > 0:
            idx = columnNumber % pow(26,i)
            idx = int(idx / (26**(i-1)))
            temp = list(alphabet_to_num.keys())[idx-1]
            ans += temp
            columnNumber -= alphabet_to_num[temp] * pow(26,i-1)
            i += 1
        return ans[::-1]
