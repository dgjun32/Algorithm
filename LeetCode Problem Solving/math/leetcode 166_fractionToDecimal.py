class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #defining the sign
        if 1 - int(numerator*denominator < 0)*2 < 0:
            sign = '-'
        else:
            sign = ''
        numerator, denominator = abs(numerator), abs(denominator)
        ans = ''
        ans += str(int(numerator // denominator))
        numerator %= denominator
        # if result is integer, just return integer shape str
        if numerator == 0:
            return sign + ans
        # else, append demical point
        else:
            ans += '.'
            
        found = False
        numerators = []
        dems = []
        while found == False and numerator > 0:
            #procedure of dividing
            numerator *= 10
            if numerator in numerators:
                found = True
                idx = numerators.index(numerator)
                ans += ''.join(dems[:idx])
                ans += '(' + ''.join(dems[idx:]) + ')'
            numerators.append(numerator)
            dem = str(int(numerator // denominator))
            dems.append(dem)
            numerator %= denominator
            if numerator == 0:
                ans += ''.join(dems)
        return sign + ans 
