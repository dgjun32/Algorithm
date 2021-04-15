# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'.
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# 1. Solution using hash table and stack
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(',
                   '}':'{',
                   ']':'['}
        close = mapping.keys()
        open = mapping.values()
        
        #if len(s)==1 or first character is closing bracket or last character is opening bracket, s is not valid
        if len(s) == 1 or s[0] in close or s[-1] in open:
            return False
        else:
            #stack indicates 'unprocessed bracket'
            stack = []
            for chr in s:
                #if stack is empty, just push chr into stack(need to be processed)
                if len(stack) == 0:
                    stack.append(chr)
                #if chr is closing bracket and it processes last element in stack, we erase out last element in stack with current chr(pop())
                elif chr in close and stack[-1] == mapping[chr]:
                    stack.pop()
                #if current chr didn't process any element in stack, just push current chr into the stack.
                else:
                    stack.append(chr)
            return len(stack) == 0
