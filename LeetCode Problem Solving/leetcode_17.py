# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#  {'2':['a','b','c'], '3':['d','e','f'],
#   '4':['g','h','i'], '5':['j','k','l'],
#   '6':['m','n','o'], '7':['p','q','r','s'],
#   '8':['t','u','v'], '9':['w','x','y','z']}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        dict = {'2':['a','b','c'], '3':['d','e','f'],
                '4':['g','h','i'], '5':['j','k','l'],
                '6':['m','n','o'], '7':['p','q','r','s'],
                '8':['t','u','v'], '9':['w','x','y','z']}
        
        #recursion
        def recursion(idx, chrs): 
            # idx indicates index of current digit(integer)
            # chrs indicates current chr sequence from now on(List)
            if len(chrs) == len(digits):
                combinations.append("".join(chrs))
                return
            
            possible_letters = dict[digits[idx]]
            for chr in possible_letters:
                chrs.append(chr)
                #recursively generates all sequence of characters
                recursion(idx+1, chrs)
                chrs.pop()
                
        combinations = []
        backtrack(0, [])
        return combinations
