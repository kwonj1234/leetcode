class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        memo = {}
        used = {}
        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            j = i % len(pattern)
            if pattern[j] in memo:
                if memo[pattern[j]] != s[i]:
                    return False
            else:
                if s[i] in used:
                    return False
                memo[pattern[j]] = s[i]
                used[s[i]] = True

        return True