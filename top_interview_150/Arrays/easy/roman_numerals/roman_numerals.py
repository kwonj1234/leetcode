class Solution:
    def __init__(self):
        self.numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        ans = 0

        for i, char in enumerate(s):
            if i > 0 \
            and (((char == "V" or char == "X") and s[i-1] == "I") \
            or ((char == "L" or char == "C") and s[i-1] == "X") \
            or ((char == "D" or char == "M") and s[i-1] == "C")):
                ans += self.numerals[char] - (2*self.numerals[s[i-1]])

            else:
                ans += self.numerals[char]

        return ans