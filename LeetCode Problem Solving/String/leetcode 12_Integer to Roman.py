# Given an integer, convert it to a roman numeral.

#Solution 1. 
class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_str = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        roman = ''
        for i in reversed(range(4)):
            n = num//pow(10, i)
            
            if n < 4:
                roman += int_to_str[pow(10,i)]*n
            elif n == 4:
                roman += int_to_str[pow(10,i)] + int_to_str[pow(10,i)*5]
            elif n > 4 and n < 9:
                roman += int_to_str[pow(10,i)*5]
                n -= 5
                roman += int_to_str[pow(10,i)]*n
            elif n == 9:
                roman += int_to_str[pow(10,i)] + int_to_str[pow(10,i+1)]
            
            num %= pow(10, i)
        return roman
        
#Solution 2.
class Solution:
  def intToRoman(self, num: int) -> str:
      mapping = {1000:'M', 900: 'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
      roman = ''
      for i in mapping.keys():
        roman += mapping[i] * (num // i)
        num %= i
       return roman
