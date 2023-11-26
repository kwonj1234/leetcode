class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo = {}
        used = {}
        for i in range(len(s)):
            if memo.get(s[i], None):
                if memo[s[i]] != t[i]:
                    return False
            else:
                if used.get(t[i], None):
                    return False
                memo[s[i]] = t[i]
                used[t[i]] = True
        return True