# My shitty solution

# from collections import Counter

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         memo = {}

#         for word in strs:
#             key = "".join(sorted(word))
#             if key in memo:
#                 memo[key].append(word)
#             else:
#                 memo[key] = [word]

#         return memo.values()

# Nice introduction to defaultdict
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())