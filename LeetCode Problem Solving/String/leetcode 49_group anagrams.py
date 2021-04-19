# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for str in strs:
            # sort every str in strs -> if 2 strs are anagrams, sorted result of 2 strs are same
            sorted_str = ''.join(sorted(str))
            if sorted_str in mapping:
                mapping[sorted_str].append(str)
            else:
                mapping[sorted_str] = [str]
        return list(mapping.values())
        
