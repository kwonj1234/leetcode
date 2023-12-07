class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = list(filter(lambda word: word, s))
        return " ".join(s[::-1])