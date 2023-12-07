class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")

        for i in range(len(s)-1, -1, -1):
          if s[i]:
            return len(s[i])
        
        # Case where the entire sentence is empty spaces
        return 0