# My solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i <= j:
            if not s[i].isalnum() or not s[j].isalnum():
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1
                continue
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        
        return True