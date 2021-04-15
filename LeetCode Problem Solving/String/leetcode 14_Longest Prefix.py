# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        zipped = list(zip(*strs))
        for li in zipped:
            if len(set(li)) == 1:
                prefix += li[0]
            else:
                break
        return prefix
