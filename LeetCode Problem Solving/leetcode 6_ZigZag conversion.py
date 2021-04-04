class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #if s is length of 1 or numRows ==1, output is still s.
        if len(s) == 1 or numRows == 1:
            return s
        else:
            ans = ''
            largest_gap = 2*(numRows-1)
            for i in range(numRows):
                #fist and last row has always equal gap between indices.
                if i == 0 or i == numRows-1:
                    ans += s[i::largest_gap]
                #however, in the case of rows other than first and last rows, gap between indices are changing
                else:
                    pointer = i
                    gap = 2*i
                    while pointer < len(s):
                        ans += s[pointer]
                        gap = largest_gap - gap
                        pointer = pointer + gap
            return ans
